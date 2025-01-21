

# PDF to Audio Converter

### Overview
The **PDF to Audio Converter** is a user-friendly application developed to enhance accessibility by converting PDF documents into high-quality, natural-sounding audio. Built using **Python**, this tool supports multiple languages, voice options, and customizable audiobook settings, making it ideal for users with visual impairments or anyone who prefers audio over text.


### Features
- **PDF to Speech Conversion**: Converts text from PDF files into natural-sounding audio files.
- **Multi-Language Support**: Offers a variety of language options and regional accents.
- **Customizable Settings**:
  - Voice selection (male, female, accents)
  - Tone adjustment for personalized audio playback
- **Accessibility-Focused**: Designed to cater to visually impaired users.
- **Audio Download**: Allows users to listen or download the generated audio file.
- **Loading Animation**: Displays a responsive animation during audio conversion for an enhanced user experience.


### Technology Stack
- **Front-End**: HTML, CSS (for the responsive and user-friendly interface)
- **Back-End**: Python (text-to-speech conversion and file handling)
- **Libraries**: Pyttsx3, PyPDF2, Flask, and gTTS

### How It Works
1. **File Upload**: Users upload a PDF document through a clean and intuitive interface.
2. **Audio Conversion**: The application extracts text from the PDF and converts it into speech.
3. **Custom Settings**: Users can customize voice, language, and tone before generating the audio.
4. **Output**: The audio is played directly or made available for download.


### Installation
1. Clone the repository:
   git clone https://github.com/yourusername/PDF-to-Audio-Converter.git
   
2. Install the required dependencies:
   pip install -r requirements.txt
  
3. Run the application:  
   python app.py
  
4. Access the web interface at:
   http://localhost:5000

### Folder Structure
- **`static/`**: Contains front-end assets like CSS and JavaScript files.
- **`templates/`**: HTML files for the web interface.
- **`uploads/`**: Stores uploaded PDF files temporarily.


### Future Enhancements
- Integration with cloud storage for uploaded PDFs and generated audio.
- Real-time voice modulation for greater customization.
- Support for additional document formats like DOCX and TXT.


### Contributions
Contributions are welcome! If you have ideas to improve the project or would like to fix bugs, feel free to fork the repository and submit a pull request.
