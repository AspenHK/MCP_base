# MCP (Model Context Protocol) Multi-Agent Demo

This project demonstrates how the Model Context Protocol (MCP) enables communication between different AI agents. It provides a step-by-step example of how agents can work together using MCP.

## 🎯 What is MCP?

**Model Context Protocol (MCP)** is a standardized protocol that allows AI agents to:
- 🔧 **Share tools** - Agents can expose functionality for others to use
- 📂 **Share resources** - Agents can provide access to data and files  
- 🤝 **Communicate seamlessly** - Standardized message format for interoperability
- 🔗 **Work together** - Multiple agents can collaborate on complex tasks

## 📁 Project Structure

```
├── mcp_server.py          # MCP Server Agent (provides tools & resources)
├── mcp_client.py          # MCP Client Agent (uses tools & resources)  
├── mcp_orchestrator.py    # Multi-agent orchestrator
├── run_demo.py           # Simple demo runner
└── README.md             # This file
```

## 🚀 How MCP Works Between Agents

### Step 1: Agent Registration
```
🔷 Server Agent starts up
🔷 Client Agent starts up  
🔷 Orchestrator registers both agents
```

### Step 2: Capability Discovery
```
📋 Client asks Server: "What tools do you have?"
📂 Client asks Server: "What resources can you provide?"
✅ Server responds with available capabilities
```

### Step 3: Connection Establishment
```
🔗 Client connects to Server
✅ Connection established - agents can now communicate
```

### Step 4: Tool Usage
```
🔧 Client: "Please use your calculator tool to add 10 + 5"
⚙️  Server: Executes calculator tool
📤 Server: Returns result "15"
```

### Step 5: Resource Access
```
📖 Client: "Please give me the user data resource"
📄 Server: Reads and returns user data
📤 Server: Sends data back to client
```

## 🔄 MCP Message Flow

Here's what happens when agents communicate:

```
CLIENT                    SERVER
  |                         |
  |  {"method": "tools/list"}  |
  |------------------------>|
  |                         |
  |  {"tools": [...]}       |
  |<------------------------|
  |                         |
  |  {"method": "tools/call", |
  |   "params": {...}}      |
  |------------------------>|
  |                         |
  |  {"content": [...]}     |
  |<------------------------|
```

## 🛠️ Available Tools in Demo

### Calculator Tool
- **Purpose**: Perform basic math operations
- **Operations**: add, subtract, multiply, divide
- **Example**: `{"operation": "add", "a": 10, "b": 5}`

### Text Processor Tool  
- **Purpose**: Process text strings
- **Operations**: uppercase, lowercase, reverse
- **Example**: `{"text": "hello", "operation": "uppercase"}`

## 📂 Available Resources in Demo

### User Database
- **URI**: `data/users.json`
- **Content**: Sample user data with names and roles
- **Access**: Any connected client can read this resource

## 🎮 Running the Demo

### Option 1: Run Individual Components
```bash
# Run just the server demo
python mcp_server.py

# Run client connecting to server
python mcp_client.py

# Run full multi-agent orchestrator
python mcp_orchestrator.py
```

### Option 2: Run Interactive Demo
```bash
python run_demo.py
```

## 📊 Demo Scenarios

### 1. Basic Client-Server Communication
- Client connects to server
- Client uses calculator and text processing tools
- Client reads user data resource

### 2. Multi-Agent Collaboration
- Multiple specialized servers (math-only, text-only)
- Multiple clients working on shared task
- Coordinated workflow across agents
- Resource sharing between multiple clients

### 3. Real-World Workflow Example
The demo simulates a business scenario:
1. **Client 1** formats document titles using text processing
2. **Client 2** calculates sales metrics using math tools
3. **Both clients** access shared user database
4. **Coordinated result** - complete sales report

## 🔍 Key MCP Concepts Demonstrated

### 1. **Tool Sharing**
```python
# Server exposes tools
server.tools = {"calculator": {...}, "text_processor": {...}}

# Client discovers and uses tools
tools = await client.list_tools()
result = await client.use_tool("calculator", {"operation": "add", "a": 5, "b": 3})
```

### 2. **Resource Sharing**
```python
# Server provides resources
server.resources = {"data/users.json": {...}}

# Client accesses resources
data = await client.read_resource("data/users.json")
```

### 3. **Agent Coordination**
```python
# Orchestrator manages multiple agents
orchestrator.register_agent("client1", client1)
orchestrator.register_agent("server1", server1)
orchestrator.connect_agents("client1", "server1")
```

## 🎯 Learning Outcomes

After running this demo, you'll understand:

✅ **How MCP enables agent-to-agent communication**
✅ **The request/response pattern in MCP**  
✅ **How agents discover each other's capabilities**
✅ **How multiple agents can work together on complex tasks**
✅ **The difference between tools and resources in MCP**
✅ **How to orchestrate multi-agent workflows**

## 🔧 Technical Details

### MCP Message Types
- `tools/list` - Discover available tools
- `tools/call` - Execute a tool with parameters
- `resources/list` - Discover available resources  
- `resources/read` - Read a specific resource

### Agent Types
- **Server Agents** - Provide tools and resources
- **Client Agents** - Use tools and resources from servers
- **Orchestrator** - Manages and coordinates multiple agents

### Communication Pattern
1. **Synchronous** - Request-response pairs
2. **Asynchronous** - Non-blocking operations
3. **Structured** - JSON-based message format
4. **Typed** - Schema validation for tool parameters

## 🚀 Next Steps

To extend this demo:
1. Add more specialized tools (file operations, API calls, etc.)
2. Implement authentication and security
3. Add real network communication (TCP/HTTP)
4. Create more complex multi-agent workflows
5. Add error handling and retry mechanisms

---

*This demo provides a foundation for understanding MCP and building more sophisticated multi-agent systems.* 