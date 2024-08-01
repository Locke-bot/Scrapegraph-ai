"""
Example of Search Graph
"""

import os
from dotenv import load_dotenv
load_dotenv()

from scrapegraphai.graphs import SearchGraph
from scrapegraphai.utils import convert_to_csv, convert_to_json, prettify_exec_info

from pydantic import BaseModel, Field
from typing import List

# ************************************************
# Define the output schema for the graph
# ************************************************

class Dish(BaseModel):
    name: str = Field(description="The name of the dish")
    description: str = Field(description="The description of the dish")

class Dishes(BaseModel):
    dishes: List[Dish]

# ************************************************
# Define the configuration for the graph
# ************************************************

deepseek_key = os.getenv("DEEPSEEK_APIKEY")

graph_config = {
    "llm": {
        "model": "deepseek-chat",
        "openai_api_key": deepseek_key,
        "openai_api_base": 'https://api.deepseek.com/v1',
    },
    "verbose": True,
}

# ************************************************
# Create the SearchGraph instance and run it
# ************************************************

search_graph = SearchGraph(
    prompt="List me Chioggia's famous dishes",
    config=graph_config,
    schema=Dishes
)

result = search_graph.run()
print(result)

# ************************************************
# Get graph execution info
# ************************************************

graph_exec_info = search_graph.get_execution_info()
print(prettify_exec_info(graph_exec_info))

# Save to json and csv
convert_to_csv(result, "result")
convert_to_json(result, "result")
