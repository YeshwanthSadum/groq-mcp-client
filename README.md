### Installation Process for Pullers

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd groqcloud-mcp-client
   ```

2. Create virtual environment and activate it:
   ```bash
   uv venv  # Creates .venv directory
   source .venv/bin/activate  # Linux/Mac
   # or .\.venv\Scripts\activate on Windows
   ```
   If you don't have uv, you can follow [these](https://docs.astral.sh/uv/getting-started/installation/) steps and install it.

4. Install dependencies (uv will read from pyproject.toml and uv.lock):
   ```bash
   uv pip install -e .  # For editable install
   # or
   uv pip install .     # For regular install
   ```
5. Add .env file:
   ```bash
   GROQ_API_KEY='gsk_**'
   CLIENT_MODEL='deepseek-r1-distill-llama-70b'
   ```
   You can obtain the GROQ_API_KEY from https://console.groq.com/keys after you login.

### Usage

   1. activate venv:
   ```
   source .venv/bin/activate
   ```

   3. Update the `server_config.json` with required MCP servers.

   Example:
   ```
      {
      "stdio_servers": [
         "/home/dell/Documents/mcp/weather/weather.py"
      ],
      "sse_servers": [
         "https://btc.maratech.com/",
         "https://insurancemcpserver.up.railway.app/"
      ]
      }
   ```

   - stdio_servers are the servers that are available locally. Leave the list empty if you
   don't have any. You can follow the
   [MCP server docs](https://modelcontextprotocol.io/quickstart/server) to create a
   local MCP server
   - Explore active SSE servers registered at https://ui.nanda-registry.com/explorer

   2. Run the CLI chat tool:
   ```
   python src/main.py
   ```
