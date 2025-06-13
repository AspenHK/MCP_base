#!/usr/bin/env python3
"""
Interactive MCP Demo Runner
Choose different scenarios to see how MCP works between agents.
"""

import asyncio
import sys

def print_header():
    """Print a nice header for the demo"""
    print("🚀" + "="*70 + "🚀")
    print("🤖" + " "*20 + "MCP MULTI-AGENT DEMO" + " "*20 + "🤖")
    print("🚀" + "="*70 + "🚀")
    print()
    print("This demo shows how different AI agents communicate")
    print("using the Model Context Protocol (MCP)")
    print()

def print_menu():
    """Print the demo menu options"""
    print("📋 Choose a demo scenario:")
    print()
    print("1️⃣  Basic Server Demo")
    print("   → See how an MCP server provides tools and resources")
    print()
    print("2️⃣  Client-Server Communication")  
    print("   → Watch a client connect to and use a server")
    print()
    print("3️⃣  Multi-Agent Orchestration")
    print("   → See multiple agents working together")
    print()
    print("4️⃣  All Demos (Sequential)")
    print("   → Run all scenarios one after another")
    print()
    print("❌ Type 'quit' or 'q' to exit")
    print()

async def run_server_demo():
    """Run the basic server demo"""
    print("🟦 SCENARIO 1: Basic MCP Server Demo")
    print("="*50)
    print("This shows how an MCP server exposes tools and resources")
    print()
    
    from mcp_server import main as server_main
    await server_main()

async def run_client_demo():
    """Run the client-server communication demo"""
    print("🟩 SCENARIO 2: Client-Server Communication Demo")
    print("="*50)
    print("This shows how a client connects to and uses an MCP server")
    print()
    
    from mcp_client import main as client_main
    await client_main()

async def run_orchestrator_demo():
    """Run the multi-agent orchestration demo"""
    print("🟨 SCENARIO 3: Multi-Agent Orchestration Demo")
    print("="*50)
    print("This shows multiple agents working together in coordination")
    print()
    
    from mcp_orchestrator import main as orchestrator_main
    await orchestrator_main()

async def run_all_demos():
    """Run all demos sequentially"""
    print("🌈 RUNNING ALL DEMOS")
    print("="*50)
    print("This will run all scenarios in sequence...")
    print()
    
    input("Press Enter to start with the Server Demo...")
    await run_server_demo()
    
    print("\n" + "="*60)
    input("Press Enter to continue with Client-Server Demo...")
    await run_client_demo()
    
    print("\n" + "="*60)
    input("Press Enter to continue with Multi-Agent Demo...")
    await run_orchestrator_demo()
    
    print("\n🎉 All demos completed!")

async def main():
    """Main interactive demo runner"""
    print_header()
    
    while True:
        print_menu()
        choice = input("👉 Enter your choice (1-4, or 'quit'): ").strip().lower()
        print()
        
        if choice in ['quit', 'q', 'exit']:
            print("👋 Thanks for exploring MCP! Goodbye!")
            break
        
        try:
            if choice == '1':
                await run_server_demo()
            elif choice == '2':
                await run_client_demo()
            elif choice == '3':
                await run_orchestrator_demo()
            elif choice == '4':
                await run_all_demos()
            else:
                print("❌ Invalid choice. Please select 1-4 or 'quit'")
                continue
                
        except KeyboardInterrupt:
            print("\n\n⏹️  Demo interrupted by user")
        except Exception as e:
            print(f"\n❌ Error running demo: {e}")
        
        print("\n" + "="*60)
        input("Press Enter to return to main menu...")
        print("\n")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Demo interrupted. Goodbye!") 