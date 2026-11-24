from mcp.server.mcpserver import MCPServer

# 1. Create the server and give it a name
mcp = MCPServer("hello-mcp")

# 2. Tools: functions the model can call
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@mcp.tool()
def greet(name: str) -> str:
    """Greet a person by name."""
    return f"Hello, {name}!"

# 3. Resources: read-only data the app can load as context
@mcp.resource("info://about")
def about() -> str:
    """Information about this server."""
    return "hello-mcp: a learning project exposing tools, resources, and prompts."

@mcp.resource("greeting://{name}")
def greeting_resource(name: str) -> str:
    """A personalized greeting for the given name."""
    return f"Welcome to hello-mcp, {name}!"

# 4. Prompts: reusable templates the user can pick
@mcp.prompt()
def explain_code(code: str) -> str:
    """Ask the model to explain a piece of code simply."""
    return f"Explain what this code does in simple terms, step by step:\n\n{code}"

# 5. Start the server
if __name__ == "__main__":
    mcp.run()  # uses the stdio transport by default