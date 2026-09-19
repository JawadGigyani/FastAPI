from pydantic import BaseModel

from app.config import DEFAULT_VOICE_ID


# Request body for POST /story
class StoryRequest(BaseModel):
    topic: str                          # e.g. "a robot who learns to paint"
    voice_id: str = DEFAULT_VOICE_ID    # optional: any ElevenLabs voice id
