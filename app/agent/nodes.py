from langchain_core.messages import HumanMessage, SystemMessage

from app.agent.llm import get_llm
from app.agent.prompts import SYSTEM_PROMPT
from app.agent.state import StoryState
from app.tts import text_to_speech

llm = get_llm()


# NODE 1: Claude writes a short story about the topic
def write_story(state: StoryState):
    messages = [SystemMessage(SYSTEM_PROMPT), HumanMessage(state["topic"])]
    response = llm.invoke(messages)
    return {"story": response.text}


# NODE 2: ElevenLabs reads the story out loud and saves it as an mp3
def narrate_story(state: StoryState):
    audio_file = text_to_speech(state["story"], state["voice_id"])
    return {"audio_file": audio_file}
