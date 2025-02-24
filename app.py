from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from gtts import gTTS
import os
import PyPDF2
from PyPDF2 import PdfReader
from io import BytesIO

app = Flask(__name__)

# Define the folder for uploaded files
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# Maximum file size for upload (8 MB)
MAX_CONTENT_LENGTH = 8 * 1024 * 1024  # 8 MB
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Home route (renders your HTML page)
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the PDF upload and TTS conversion
@app.route('/convert', methods=['POST'])
def convert_to_audio():
    # Retrieve file from the form
    pdf_file = request.files['pdf-upload']
    language = request.form['language']
    voice_tone = request.form['voice-tone']  # select voice tones

    # Validate file size
    if pdf_file.content_length > MAX_CONTENT_LENGTH:
        flash('File size exceeds the 8 MB limit. Please upload a smaller file.', 'error')
        return redirect(url_for('home'))

    # Save the uploaded file
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename)
    pdf_file.save(pdf_path)

    # Extract text from PDF
    extracted_text = extract_text_from_pdf(pdf_path)

    # Convert the extracted text to speech
    if extracted_text:
        # Select the best language code based on user input
        lang_code = select_language_code(language, voice_tone)

        # Adjust speed of speech by using a slightly faster voice
        tts = gTTS(text=extracted_text, lang=lang_code, slow=False)  # 'slow=False' speeds up the audio

        # Save the audio file in memory
        audio_io = BytesIO()
        tts.write_to_fp(audio_io)
        audio_io.seek(0)  # Set the pointer back to the beginning after writing

        # Prepare the file for download
        audio_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.mp3')
        with open(audio_file_path, 'wb') as audio_file:
            audio_file.write(audio_io.read())

        return redirect(url_for('result'))

    return redirect(url_for('home'))

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as pdf_file:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text() or ""  # Ensure we handle None returns
    return text

# Function to select the language code based on input
def select_language_code(language, voice_tone):
    # Define language codes for different accents and tones
    language_codes = {
        'english': {
            'male': 'en-us',    # American English
            'female': 'en-gb',  # British English
            'kids': 'en-au'     # Australian English (soft, playful tone for kids)
        },
        'spanish': {
            'male': 'es-us',    # Latin American Spanish
            'female': 'es-es',  # European Spanish
            'kids': 'es-mx'     # Mexican Spanish for a playful, informal tone
        },
        'french': {
            'male': 'fr-ca',    # Canadian French
            'female': 'fr-fr',  # French from France
            'kids': 'fr-ca'     # Using Canadian French, which has a slightly softer tone
        }
        # Add more languages and tones as needed
    }

    # Default to 'en' if the language or tone is not found
    return language_codes.get(language, {}).get(voice_tone, 'en')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/download')
def download():
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], 'output.mp3'), as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
