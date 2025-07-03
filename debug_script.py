#!/usr/bin/env python3
"""
Debug script to identify and fix common issues in CrewAI product analysis system
"""

import os
import sys
from dotenv import load_dotenv

def check_environment():
    """Check environment variables and dependencies"""
    print("🔍 Checking environment setup...")
    
    # Load environment variables
    load_dotenv()
    
    # Check for API key
    api_key = os.getenv("LLM_API_KEY")
    if not api_key:
        print("❌ LLM_API_KEY not found in environment variables")
        print("   Please set LLM_API_KEY in your .env file")
        return False
    else:
        print(f"✅ LLM_API_KEY found (length: {len(api_key)})")
    
    # Check required packages
    required_packages = [
        'crewai',
        'python-dotenv',
        'matplotlib',
        'seaborn',
        'pandas',
        'numpy',
        'plotly'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ {package} installed")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} not installed")
    
    if missing_packages:
        print(f"\n📦 Install missing packages with:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    return True

def test_llm_connection():
    """Test LLM connection"""
    print("\n🔗 Testing LLM connection...")
    
    try:
        from crewai import LLM
        
        api_key = os.getenv("LLM_API_KEY")
        llm = LLM(
            model="gemini/gemini-1.5-flash",
            temperature=0.7,
            api_key=api_key,
            max_tokens=2000
        )
        
        print("✅ LLM instance created successfully")
        return llm
        
    except Exception as e:
        print(f"❌ LLM connection failed: {e}")
        print("\n💡 Troubleshooting tips:")
        print("   - Verify your Google API key is valid")
        print("   - Check if Generative AI API is enabled in Google Cloud")
        print("   - Ensure you have sufficient quota")
        return None

def test_agent_creation():
    """Test agent creation"""
    print("\n🤖 Testing agent creation...")
    
    try:
        from crewai import Agent
        
        llm = test_llm_connection()
        if not llm:
            return False
        
        agent = Agent(
            role="Test Agent",
            goal="Test agent creation",
            backstory="This is a test agent for debugging purposes.",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
        
        print("✅ Agent created successfully")
        return True
        
    except Exception as e:
        print(f"❌ Agent creation failed: {e}")
        return False

def test_simple_task():
    """Test a simple task execution"""
    print("\n📋 Testing simple task execution...")
    
    try:
        from crewai import Agent, Task, Crew, Process
        
        llm = test_llm_connection()
        if not llm:
            return False
        
        # Create a simple agent
        agent = Agent(
            role="Test Agent",
            goal="Answer simple questions",
            backstory="You are a helpful assistant for testing purposes.",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
        
        # Create a simple task
        task = Task(
            description="Say hello and confirm you're working properly.",
            expected_output="A simple greeting message confirming the system is working.",
            agent=agent
        )
        
        # Create and run crew
        crew = Crew(
            agents=[agent],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )
        
        result = crew.kickoff()
        print(f"✅ Task completed successfully: {result}")
        return True
        
    except Exception as e:
        print(f"❌ Task execution failed: {e}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        return False

def create_fixed_env_file():
    """Create a template .env file"""
    print("\n📄 Creating .env template...")
    
    env_content = """# Google API Key for Gemini
LLM_API_KEY=your_google_api_key_here

# Alternative API keys (if needed)
# OPENAI_API_KEY=your_openai_key_here
# ANTHROPIC_API_KEY=your_anthropic_key_here
"""
    
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ .env template created")
        print("   Please add your actual API key to the .env file")
    else:
        print("✅ .env file already exists")

def main():
    """Main debug function"""
    print("🔧 CrewAI Product Analysis Debug Tool")
    print("=" * 50)
    
    # Check environment
    if not check_environment():
        print("\n❌ Environment check failed")
        create_fixed_env_file()
        return
    
    # Test LLM connection
    if not test_llm_connection():
        print("\n❌ LLM connection test failed")
        return
    
    # Test agent creation
    if not test_agent_creation():
        print("\n❌ Agent creation test failed")
        return
    
    # Test simple task
    if not test_simple_task():
        print("\n❌ Task execution test failed")
        return
    
    print("\n🎉 All tests passed! Your CrewAI setup should be working.")
    print("\n🚀 You can now run your main product analysis script.")

if __name__ == "__main__":
    main()
