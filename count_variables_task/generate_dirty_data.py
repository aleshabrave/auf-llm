from pathlib import Path

from openai import OpenAI

import dependencies

client = OpenAI(
    api_key=dependencies.get_settings().deepseek_api_key,
    base_url=dependencies.get_settings().deepseek_api_url,
)

system_content = """
You're a code snippet generator.
Generate only input the number of different Python code snippets. 
It is important that the snippets are varied.
Output only snippets without comments and etc.
"""
user_content = """
10
"""

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content},
    ],
)

for i in range(10):
    dirty_data_path = (
        Path(__file__).absolute().parents[0].joinpath("data/dirty_data.txt")
    )

    with open(dirty_data_path, "a") as dirty_data:
        dirty_data.write(response.choices[0].message.content)
