from pathlib import Path

from dotenv import load_dotenv

# Load ANTHROPIC_API_KEY and ELEVENLABS_API_KEY from the .env file
load_dotenv()

# Claude model that writes the story
LLM_MODEL = "qwen/qwen3.8-27b"

# ElevenLabs model and voice that read the story out loud
TTS_MODEL = "eleven_v3"
DEFAULT_VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"  # default voice used in ElevenLabs examples

# Folder where the generated mp3 files are saved
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)
