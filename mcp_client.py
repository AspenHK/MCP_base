#!/usr/bin/env python3
"""
Simple MCP Client Agent
This agent connects to an MCP server and uses its tools and resources.
"""

import asyncio
import json
from typing import Dict, Any, List

class MCPClient:
    """A simple MCP client that uses tools and resources from a server"""
    
    def __init__(self):
        self.server_tools = []
        self.server_resources = []
        self.connected = False
    
    async def connect_to_server(self, server):
        """Connect to an MCP server and discover its capabilities"""
        print("🔗 MCP Client connecting to server...")
        self.server = server
        
        # Discover available tools
        tools_response = await server.handle_request({"method": "tools/list"})
        self.server_tools = tools_response.get("tools", [])
        
        # Discover available resources
        resources_response = await server.handle_request({"method": "resources/list"})
        self.server_resources = resources_response.get("resources", [])
        
        self.connected = True
        print("✅ Successfully connected to MCP server")
        print(f"📋 Available tools: {[tool['name'] for tool in self.server_tools]}")
        print(f"📂 Available resources: {[resource['name'] for resource in self.server_resources]}")
    
    async def use_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Use a tool from the connected server"""
        if not self.connected:
            return {"error": "Not connected to server"}
        
        print(f"🔧 Client requesting tool: {tool_name}")
        request = {
            "method": "tools/call",
            "params": {
                "name": tool_name,
                "arguments": arguments
            }
        }
        
        response = await self.server.handle_request(request)
        return response
    
    async def read_resource(self, uri: str) -> Dict[str, Any]:
        """Read a resource from the connected server"""
        if not self.connected:
            return {"error": "Not connected to server"}
        
        print(f"📖 Client requesting resource: {uri}")
        request = {
            "method": "resources/read",
            "params": {
                "uri": uri
            }
        }
        
        response = await self.server.handle_request(request)
        return response
    
    async def perform_workflow(self):
        """Demonstrate a workflow using multiple tools and resources"""
        print("\n🎯 Starting MCP Client Workflow")
        print("=" * 50)
        
        # Step 1: Use calculator tool
        print("\nStep 1: Performing calculations")
        calc_result = await self.use_tool("calculator", {
            "operation": "multiply",
            "a": 15,
            "b": 4
        })
        print(f"Calculator result: {calc_result}")
        
        # Step 2: Process some text
        print("\nStep 2: Processing text")
        text_result = await self.use_tool("text_processor", {
            "text": "Model Context Protocol",
            "operation": "reverse"
        })
        print(f"Text processing result: {text_result}")
        
        # Step 3: Read user data
        print("\nStep 3: Reading user data")
        user_data = await self.read_resource("data/users.json")
        print(f"User data: {user_data}")
        
        # Step 4: Combine operations (more complex workflow)
        print("\nStep 4: Complex workflow - calculating user count")
        user_count_calc = await self.use_tool("calculator", {
            "operation": "add",
            "a": 3,  # We know from the data there are 3 users
            "b": 2   # Adding 2 more hypothetical users
        })
        print(f"Total user count calculation: {user_count_calc}")
        
        print("\n✅ Workflow completed successfully!")

async def main():
    """Run the MCP client demonstration"""
    from mcp_server import MCPServer
    
    # Create server and client
    server = MCPServer()
    client = MCPClient()
    
    print("🚀 Starting MCP Communication Demo")
    print("=" * 50)
    
    # Connect client to server
    await client.connect_to_server(server)
    
    # Run demonstration workflow
    await client.perform_workflow()
    
    print("\n🎉 MCP Demo completed!")

if __name__ == "__main__":
    asyncio.run(main()) 