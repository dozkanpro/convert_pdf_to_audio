from google.cloud import texttospeech
import PyPDF2

with open('Hello Deniz.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

with open('output.txt', 'w') as text_file:
    text_file.write(text)

client = texttospeech.TextToSpeechClient()


with open('output.txt', 'r') as text_file:
    text = text_file.read()

synthesis_input = texttospeech.SynthesisInput(text=text)


voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
