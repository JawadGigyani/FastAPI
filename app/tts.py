from datetime import datetime

from elevenlabs.client import ElevenLabs

from app.config import OUTPUT_DIR, TTS_MODEL

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

    # Write the chunks into an mp3 file and return its name
    file_name = f"story_{datetime.now():%Y%m%d_%H%M%S}.mp3"
    with open(OUTPUT_DIR / file_name, "wb") as f:
        for chunk in audio:
            f.write(chunk)
    return file_name
