from mcp.server.mcpserver import MCPServer

# 1. Create the server and give it a name
mcp = MCPServer("hello-mcp")

# 2. Register a tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@mcp.tool()
def greet(name: str) -> str:
    """Greet a person by name."""
    return f"Hello, {name}!"

# 3. Start the server
if __name__ == "__main__":
    mcp.run()  # uses the stdio transport by default