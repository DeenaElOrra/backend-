import yt_dlp
import openai
import os

# Ensure you set your OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

def baixar_audio_youtube(url, audio_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': '/opt/homebrew/bin/ffmpeg',  # Updated path
        'outtmpl': audio_path,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def transcrever_audio_whisper(audio_path):
    # Use openai.Audio.transcribe with the new API format
    with open(audio_path, "rb") as audio_file:
        response = openai.Audio.create(
            model="whisper-1",
            file=audio_file
        )
    return response['text']

url = 'https://www.youtube.com/watch?v=uNFcFfc-sno'
audio_path = 'audio.mp3'
audio_wav_path = 'audio.wav'  # Update this path if necessary

baixar_audio_youtube(url, audio_path)

# Convert mp3 to wav if needed for transcription
os.system(f'/opt/homebrew/bin/ffmpeg -i {audio_path} {audio_wav_path}')

transcricao = transcrever_audio_whisper(audio_wav_path)
print(transcricao)
