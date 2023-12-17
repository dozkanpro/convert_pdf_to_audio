# Introduction
This is the repository demostrate how to convert a pdf file to audio file using **Google Cloud**. 

## Getting Started
- **Fork the repository:** You should **fork the repository** and then **clone it** so you can manage your own repo and use this only as a template.
  ```
  $ git clone https://github.com/your_username/your-flask-project.git
  ```
- **Install dependencies:**

    ```
    pip install -r requirements.txt
    ```

- **Create your google credential** using [here](https://cloud.google.com/docs/authentication/provide-credentials-adc#how-to).

## Features

- **PyPDF2:** Read .pdf file and write a .txt file.
- **texttospeech from Google Cloud:** Read .txt file and convert .mp3 file. To  do this:
    1. Initiate client:
        ```
          client = texttospeech.TextToSpeechClient()
        ```
    2. Select the input type to synthesis:
        ```
          synthesis_input = texttospeech.SynthesisInput(text=text)
        ```
    3. Build the voice request, select the language code and the voice gender:
        ```
         voice = texttospeech.VoiceSelectionParams(language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
        ```
    4. Select the output audio type:
        ```
          audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
        ```
        
       
