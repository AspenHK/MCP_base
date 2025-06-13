#!/usr/bin/env python3
"""
MCP Multi-Agent Orchestrator
This demonstrates how multiple MCP agents can work together in a coordinated workflow.
"""

import asyncio
import json
from typing import Dict, Any, List
from mcp_server import MCPServer
from mcp_client import MCPClient

class MCPOrchestrator:
    """Orchestrates multiple MCP agents working together"""
    
    def __init__(self):
        self.agents = {}
        self.workflows = []
    
    async def register_agent(self, agent_name: str, agent_type: str, agent_instance):
        """Register an agent with the orchestrator"""
        self.agents[agent_name] = {
            "type": agent_type,
            "instance": agent_instance,
            "capabilities": []
        }
        
        if agent_type == "server":
            # Discover server capabilities
            tools_response = await agent_instance.handle_request({"method": "tools/list"})
            resources_response = await agent_instance.handle_request({"method": "resources/list"})
            
            self.agents[agent_name]["capabilities"] = {
                "tools": tools_response.get("tools", []),
                "resources": resources_response.get("resources", [])
            }
        
        print(f"🔷 Registered {agent_type} agent: {agent_name}")
    
    async def connect_agents(self, client_name: str, server_name: str):
        """Connect a client agent to a server agent"""
        if client_name not in self.agents or server_name not in self.agents:
            print(f"❌ Cannot connect: agents not found")
            return False
        
        client = self.agents[client_name]["instance"]
        server = self.agents[server_name]["instance"]
        
        await client.connect_to_server(server)
        print(f"🔗 Connected {client_name} to {server_name}")
        return True
    
    async def execute_distributed_workflow(self):
        """Execute a complex workflow across multiple agents"""
        print("\n🌐 Starting Distributed MCP Workflow")
        print("=" * 60)
        
        # Get references to our agents
        math_server = self.agents["math_server"]["instance"]
        text_server = self.agents["text_server"]["instance"] 
        client1 = self.agents["client1"]["instance"]
        client2 = self.agents["client2"]["instance"]
        
        # Scenario: Two clients working on a collaborative task
        print("\n📝 Scenario: Collaborative document processing")
        print("-" * 40)
        
        # Client 1: Process document title
        print("\n👤 Client 1: Processing document title")
        title_result = await client1.use_tool("text_processor", {
            "text": "quarterly sales report 2024",
            "operation": "uppercase"
        })
        print(f"Title processed: {title_result}")
        
        # Client 2: Calculate some metrics  
        print("\n👤 Client 2: Calculating sales metrics")
        q1_sales = await client2.use_tool("calculator", {
            "operation": "multiply",
            "a": 150000,  # Units sold
            "b": 25       # Price per unit
        })
        print(f"Q1 Sales: {q1_sales}")
        
        q2_sales = await client2.use_tool("calculator", {
            "operation": "multiply", 
            "a": 180000,
            "b": 25
        })
        print(f"Q2 Sales: {q2_sales}")
        
        # Client 2: Calculate total sales
        total_sales = await client2.use_tool("calculator", {
            "operation": "add",
            "a": 3750000,  # Q1 result
            "b": 4500000   # Q2 result  
        })
        print(f"Total Sales: {total_sales}")
        
        # Client 1: Format the final report summary
        print("\n👤 Client 1: Creating report summary")
        summary = await client1.use_tool("text_processor", {
            "text": "total sales: $8,250,000",
            "operation": "uppercase"
        })
        print(f"Final summary: {summary}")
        
        # Both clients access shared user data
        print("\n👥 Both clients accessing shared resources")
        user_data1 = await client1.read_resource("data/users.json") 
        user_data2 = await client2.read_resource("data/users.json")
        
        print("✅ Both clients successfully accessed shared user database")
        
        print("\n🎯 Distributed workflow completed!")
        print("📊 Results:")
        print("  - Document title formatted")
        print("  - Sales calculations performed")
        print("  - Final report summary created")
        print("  - Shared resources accessed by multiple clients")

class SpecializedServer(MCPServer):
    """A specialized MCP server with specific capabilities"""
    
    def __init__(self, server_type: str):
        super().__init__()
        self.server_type = server_type
        
        if server_type == "math":
            # Math server only provides calculator
            self.tools = {
                "calculator": self.tools["calculator"]
            }
        elif server_type == "text":
            # Text server only provides text processing
            self.tools = {
                "text_processor": self.tools["text_processor"]
            }

async def main():
    """Run the multi-agent MCP demonstration"""
    print("🚀 Starting Multi-Agent MCP Demo")
    print("=" * 60)
    
    # Create orchestrator
    orchestrator = MCPOrchestrator()
    
    # Create specialized servers
    math_server = SpecializedServer("math")
    text_server = SpecializedServer("text")
    
    # Create clients
    client1 = MCPClient()
    client2 = MCPClient()
    
    # Register all agents
    await orchestrator.register_agent("math_server", "server", math_server)
    await orchestrator.register_agent("text_server", "server", text_server)
    await orchestrator.register_agent("client1", "client", client1)
    await orchestrator.register_agent("client2", "client", client2)
    
    # Connect clients to servers
    print("\n🔗 Setting up agent connections...")
    await orchestrator.connect_agents("client1", "text_server")  # Client 1 -> Text Server
    await orchestrator.connect_agents("client2", "math_server")  # Client 2 -> Math Server
    
    # Execute distributed workflow
    await orchestrator.execute_distributed_workflow()
    
    print("\n🎉 Multi-Agent MCP Demo completed!")
    print("\n📋 What happened:")
    print("  1. Created specialized MCP servers (math & text)")
    print("  2. Created multiple MCP clients")
    print("  3. Connected clients to different servers")
    print("  4. Executed coordinated workflow across agents")
    print("  5. Demonstrated resource sharing between agents")

if __name__ == "__main__":
    asyncio.run(main()) 