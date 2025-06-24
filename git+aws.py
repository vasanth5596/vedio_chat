import asyncio, os
from textwrap import dedent
from dotenv import load_dotenv
from agno.agent import Agent
from agno.tools.mcp import MCPTools
from mcp import StdioServerParameters
from agno.models.openai import OpenAIChat
from pathlib import Path
load_dotenv()

async def run_agent():

    file_path = Path(r"C:\Users\vasanth\Desktop\MCP")
    if not file_path.exists():
        print(f"Error: Directory {file_path} does not exist.")
        return
    print(f"Accessing directory: {file_path}\n")

    fs_params  = StdioServerParameters(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem", str(file_path)],
        stderr=open("mcp_server.log", "w"))


    # GitHub MCP setup (yours)
    gh_params = StdioServerParameters(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-github"],
        env={"GITHUB_PERSONAL_ACCESS_TOKEN": os.getenv("GITHUB_PAT")}
    )
    # AWS MCP via Docker
    aws_params = StdioServerParameters(
        command="docker",
        args=[
            "run","--rm","-i",
            "-e","AWS_PROFILE","-e","AWS_REGION",
            "-v",f"{os.path.expanduser('~')}/.aws:/home/appuser/.aws:ro",
            "ghcr.io/alexei-led/aws-mcp-server:latest"
        ],
        env=os.environ
    )

    async with MCPTools(server_params=gh_params) as gh, \
               MCPTools(server_params=fs_params) as fs, \
               MCPTools(server_params=aws_params) as aws:
        
        agent = Agent(
            model=OpenAIChat(id="gpt-4.1-nano-2025-04-14", api_key=os.getenv("OPENAI_API_KEY")),
            tools=[gh, fs, aws],
            instructions=dedent("""\
            You have three toolkits:
            1) Filesystem: read/write files in this project.
            2) GitHub: commit and push code.
            3) AWS: create EC2, deploy code, manage services.
            Use files API to load or edit, then commit changes to GitHub.
                """),
            markdown=True,
            show_tool_calls=True,
            add_history_to_messages=True,
            num_history_responses=5,
        )

        print("🚀 Agent ready—type your commands (or 'exit')")
        while True:
            inp = input("You: ")
            if inp.lower() in ("exit","quit"):
                break
            await agent.aprint_response(inp, stream=True)

if __name__ == "__main__":
    asyncio.run(run_agent())