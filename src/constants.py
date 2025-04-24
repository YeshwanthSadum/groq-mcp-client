import os

# Groq client
CLIENT_MODEL = os.environ.get("CLIENT_MODEL", "llama-3.1-8b-instant")
TOOL_RESPONSE_LIMIT = 1000

# CLI chat
SERVER_CONFIG_PATH = "server_config.json"
CLI_CLIENT_SYSTEM_PROMPT = (
    "You need to answer questions using the" + " available tools. Use bullet points."
)
CLI_CLIENT_STOP_WORDS = ["stop", "exit", "quit"]
