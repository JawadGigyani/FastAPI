from typing import TypedDict


# The data that flows through the graph.
# Each node reads what it needs and fills in its part.
class StoryState(TypedDict):
    topic: str       # input from the user
    voice_id: str    # input from the user
    story: str       # filled by the write_story node
    audio: str       # filled by the narrate_story node (base64 mp3)
