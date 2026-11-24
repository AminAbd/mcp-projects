# MCP Projects

A series of hands-on projects for learning the **Model Context Protocol (MCP)**, the open standard that lets AI applications connect to external tools, data, and services.

Each project is self-contained in its own folder, with its own README explaining what it builds, how to run it, and things worth knowing.

## Projects

| # | Project | Description | Status |
|---|---------|-------------|--------|
| 01 | [Build a small server and connect](./01-build-a-small-server-and-connect/) | Build a minimal MCP server with tools, resources, and a prompt, test it with MCP Inspector, and connect it to a real MCP client. | ✅ Done |

## What is MCP?

MCP standardizes how AI applications (the **host**, such as Claude Desktop or an IDE) talk to external capabilities. The host runs an MCP **client** that connects to one or more MCP **servers**. Each server can expose:

- **Tools**: functions the model can call (for example, "get the weather")
- **Resources**: data the application can read (for example, files or records)
- **Prompts**: reusable prompt templates

Messages between the client and server use JSON-RPC 2.0, sent over a transport such as `stdio` (local processes) or Streamable HTTP (remote servers).

## Repository structure

```
mcp-projects/
├── README.md                              # This file: overview of the series
└── 01-build-a-small-server-and-connect/   # Project 1
```

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io)
- [MCP specification](https://modelcontextprotocol.io/specification)
- [MCP SDKs on GitHub](https://github.com/modelcontextprotocol)
