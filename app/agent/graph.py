from langgraph.graph import END, START, StateGraph

from app.agent.nodes import narrate_story, write_story
from app.agent.state import StoryState


def build_graph():
    graph = StateGraph(StoryState)

    # Nodes
    graph.add_node("write_story", write_story)      # LLM
    graph.add_node("narrate_story", narrate_story)  # ElevenLabs API

    # Edges: START -> write_story -> narrate_story -> END
    graph.add_edge(START, "write_story")
    graph.add_edge("write_story", "narrate_story")
    graph.add_edge("narrate_story", END)

    return graph.compile()
