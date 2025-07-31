from mcp.server import FastMCP
from agent import register_tools

mcp = FastMCP("EM Dispatch Agent")

def main():
    register_tools(mcp)
    mcp.run(transport="streamable-http")

if __name__ == "__main__":
    main()