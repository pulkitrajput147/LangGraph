from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage, BaseMessage
from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver    # store conversation in memory(RAM)
from dotenv import load_dotenv
import os

load_dotenv()

# Define the state graph
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage],add_messages]    

llm= ChatOpenAI(api_key=os.getenv("api_key"), temperature=0,model="gpt-4o-mini")

def chat_node(state: ChatState):

    # take user query from state
    messages=state["messages"]

    # send it to llm
    response=llm.invoke(messages)

    # store repsonse back to state
    return {"messages":[response]}


# Building the Graph
checkpointer = MemorySaver()

graph = StateGraph(ChatState)
graph.add_node('chat_node',chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot=graph.compile(checkpointer=checkpointer)

