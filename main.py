"""The module runs a CLI ChatBot that uses groqclient
"""

import json
from dataclasses import dataclass
from constants import (
    SERVER_CONFIG_PATH,
    CLI_CLIENT_SYSTEM_PROMPT,
    CLI_CLIENT_STOP_WORDS,
)
from groqclient import MCPClient


@dataclass
class ServerConfig:
    stdio_servers: list[str]
    sse_servers: list[str]

    def list_servers(self):
        return self.stdio_servers + self.stdio_servers


async def main():
    with open(SERVER_CONFIG_PATH, "r") as file:
        data = json.load(file)

    server_config = ServerConfig(**data)

    client = MCPClient()

    for i, server in enumerate(server_config.stdio_servers):
        await client.connect_to_stdio_server("stdio" + str(i), server)

    for i, server in enumerate(server_config.sse_servers):
        await client.connect_to_sse_server("sse" + str(i), server + "sse")

    messages = [
        {
            "role": "system",
            "content": CLI_CLIENT_SYSTEM_PROMPT,
        }
    ]

    print("Welcome to the CLI chat bot. You can type stop to exit.")

    while True:
        user_input = input("User: ").strip()

        if user_input.lower() in CLI_CLIENT_STOP_WORDS:
            print("Exiting chat...")
            break

        messages = await client.process_query(messages, user_input)

        # Assume last message is the assistant's response
        assistant_message = messages[-1]

        print(10 * "-", "Assistant", 10 * "-")
        print(assistant_message["content"])
        print(30 * "-")

        if len(messages) > 5:
            messages = messages[-5:]

    # Close connection
    await client.exit_stack.aclose()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())

# TODO:
# refactor the code
# use groq agent
