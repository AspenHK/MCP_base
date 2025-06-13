#!/usr/bin/env python3
"""
Simple MCP Server Agent
This agent provides tools and resources for other agents to use.
"""

import asyncio
import json
import sys
from typing import Dict, Any, List

class MCPServer:
    """A simple MCP server that provides tools and resources"""
    
    def __init__(self):
        self.tools = {
            "calculator": {
                "name": "calculator",
                "description": "Perform basic arithmetic operations",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "operation": {"type": "string", "enum": ["add", "subtract", "multiply", "divide"]},
                        "a": {"type": "number"},
                        "b": {"type": "number"}
                    },
                    "required": ["operation", "a", "b"]
                }
            },
            "text_processor": {
                "name": "text_processor", 
                "description": "Process text - uppercase, lowercase, or reverse",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string"},
                        "operation": {"type": "string", "enum": ["uppercase", "lowercase", "reverse"]}
                    },
                    "required": ["text", "operation"]
                }
            }
        }
        
        self.resources = {
            "data/users.json": {
                "uri": "data/users.json",
                "name": "User Database",
                "description": "Sample user data",
                "mimeType": "application/json"
            }
        }
    
    async def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle incoming MCP requests"""
        method = request.get("method")
        params = request.get("params", {})
        
        print(f"🔄 MCP Server received request: {method}")
        
        if method == "tools/list":
            return {
                "tools": list(self.tools.values())
            }
        
        elif method == "tools/call":
            tool_name = params.get("name")
            arguments = params.get("arguments", {})
            return await self.call_tool(tool_name, arguments)
        
        elif method == "resources/list":
            return {
                "resources": list(self.resources.values())
            }
        
        elif method == "resources/read":
            uri = params.get("uri")
            return await self.read_resource(uri)
        
        else:
            return {"error": f"Unknown method: {method}"}
    
    async def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a tool with given arguments"""
        print(f"🛠️  Executing tool: {tool_name} with args: {arguments}")
        
        if tool_name == "calculator":
            operation = arguments["operation"]
            a = arguments["a"]
            b = arguments["b"]
            
            if operation == "add":
                result = a + b
            elif operation == "subtract":
                result = a - b  
            elif operation == "multiply":
                result = a * b
            elif operation == "divide":
                if b == 0:
                    return {"error": "Division by zero"}
                result = a / b
            else:
                return {"error": f"Unknown operation: {operation}"}
            
            return {
                "content": [
                    {
                        "type": "text",
                        "text": f"Result: {a} {operation} {b} = {result}"
                    }
                ]
            }
        
        elif tool_name == "text_processor":
            text = arguments["text"]
            operation = arguments["operation"]
            
            if operation == "uppercase":
                result = text.upper()
            elif operation == "lowercase":
                result = text.lower()
            elif operation == "reverse":
                result = text[::-1]
            else:
                return {"error": f"Unknown operation: {operation}"}
            
            return {
                "content": [
                    {
                        "type": "text", 
                        "text": f"Processed text: {result}"
                    }
                ]
            }
        
        return {"error": f"Unknown tool: {tool_name}"}
    
    async def read_resource(self, uri: str) -> Dict[str, Any]:
        """Read a resource by URI"""
        print(f"📄 Reading resource: {uri}")
        
        if uri == "data/users.json":
            # Simulate user data
            sample_data = {
                "users": [
                    {"id": 1, "name": "Alice", "role": "admin"},
                    {"id": 2, "name": "Bob", "role": "user"},
                    {"id": 3, "name": "Charlie", "role": "user"}
                ]
            }
            return {
                "contents": [
                    {
                        "type": "text",
                        "text": json.dumps(sample_data, indent=2)
                    }
                ]
            }
        
        return {"error": f"Resource not found: {uri}"}

async def main():
    """Run the MCP server"""
    server = MCPServer()
    print("🚀 MCP Server Agent started")
    print("Available tools:", list(server.tools.keys()))
    print("Available resources:", list(server.resources.keys()))
    
    # Simulate handling requests (in real scenario, this would be via stdio/transport)
    test_requests = [
        {"method": "tools/list"},
        {"method": "tools/call", "params": {"name": "calculator", "arguments": {"operation": "add", "a": 10, "b": 5}}},
        {"method": "tools/call", "params": {"name": "text_processor", "arguments": {"text": "Hello World", "operation": "uppercase"}}},
        {"method": "resources/read", "params": {"uri": "data/users.json"}}
    ]
    
    for request in test_requests:
        print(f"\n📥 Processing request: {request['method']}")
        response = await server.handle_request(request)
        print(f"📤 Response: {json.dumps(response, indent=2)}")

if __name__ == "__main__":
    asyncio.run(main()) 