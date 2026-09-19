import base64

from elevenlabs.client import ElevenLabs

from app.config import TTS_MODEL

# Reads ELEVENLABS_API_KEY from the environment automatically
client = ElevenLabs()


def text_to_speech(text: str, voice_id: str) -> str:
    # Ask ElevenLabs to turn the text into speech (the audio comes back in chunks)
    audio = client.text_to_speech.convert(
        text=text,
        voice_id=voice_id,
        model_id=TTS_MODEL,
        output_format="mp3_44100_128",
    )

    # Join the chunks and return the mp3 as base64 text.
    # We don't save a file because Vercel's filesystem is read-only.
    mp3_bytes = b"".join(audio)
    return base64.b64encode(mp3_bytes).decode()
