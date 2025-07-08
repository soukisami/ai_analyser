#!/usr/bin/env python3
"""
Fixed main script for AI-Powered Comprehensive Product Analysis System
"""

import os
import sys
import traceback
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

def check_prerequisites():
    """Check if all prerequisites are met"""
    print("🔍 Checking prerequisites...")
    
    # Check environment variables
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ OPENROUTER_API_KEY not found in environment variables")
        print("   Please create a .env file with your Google API key:")
        print("   OPENROUTER_API_KEY=your_google_api_key_here")
        return False
    
    # Check required imports
    try:
        from crewai import Crew, Process, Agent, Task
        print("✅ CrewAI imported successfully")
    except ImportError as e:
        print(f"❌ CrewAI import failed: {e}")
        print("   Install with: pip install crewai")
        return False
    
    return True

def get_product_idea():
    """Get product idea from user with validation"""
    print("Welcome to AI-Powered Comprehensive Product Analysis System")
    print("~" * 60)
    
    while True:
        idea = input("Please enter your product idea: ").strip()
        if idea:
            return idea
        print("❌ Please enter a valid product idea.")

def test_single_agent():
    """Test a single agent before running full analysis"""
    print("\n🧪 Testing single agent...")
    
    try:
        from agent_config import create_product_idea_intake_agent
        from tasks import create_product_idea_structuring_task
        from crewai import Crew, Process
        
        # Create agent
        agent = create_product_idea_intake_agent()
        print("✅ Agent created successfully")
        
        # Create simple task
        task = create_product_idea_structuring_task("test product idea", agent)
        print("✅ Task created successfully")
        
        # Test crew creation
        crew = Crew(
            agents=[agent],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )
        print("✅ Crew created successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Single agent test failed: {e}")
        traceback.print_exc()
        return False

def run_simplified_analysis(product_idea):
    """Run a simplified analysis focusing on the first agent only"""
    print(f"\n🚀 Running simplified analysis for: '{product_idea}'")
    
    try:
        from agent_config import create_product_idea_intake_agent
        from tasks import create_product_idea_structuring_task
        from crewai import Crew, Process
        
        # Create agent
        print("Creating Product Idea Intake Agent...")
        agent = create_product_idea_intake_agent()
        
        # Create task
        print("Creating product idea structuring task...")
        task = create_product_idea_structuring_task(product_idea, agent)
        
        # Create and run crew
        print("Creating and running crew...")
        crew = Crew(
            agents=[agent],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )
        
        result = crew.kickoff()
        
        print("\n" + "~" * 82)
        print("🎉 SIMPLIFIED ANALYSIS COMPLETED")
        print("~" * 82)
        print(result)
        print("~" * 82)
        
        return result
        
    except Exception as e:
        print(f"❌ Analysis failed: {e}")
        print("\nDetailed error information:")
        traceback.print_exc()
        return None

def run_full_analysis(product_idea):
    """Run the full comprehensive analysis"""
    print(f"\n🚀 Running full analysis for: '{product_idea}'")
    
    try:
        from agent_config import (
            create_product_idea_intake_agent,
            create_market_research_analyst_agent,
            create_competitive_analyst_agent,
            create_strategic_analyst_agent,
            create_financial_analyst_agent,
            create_technical_feasibility_assessor_agent,
            create_customer_insights_analyst_agent,
            create_marketing_strategist_agent,
            create_kpi_metrics_definer_agent,
            create_report_synthesizer_agent
        )
        from tasks import (
            create_product_idea_structuring_task,
            create_market_research_task,
            create_competitive_analysis_task,
            create_swot_analysis_task,
            create_financial_projections_task,
            create_technical_feasibility_task,
            create_customer_segmentation_task,
            create_marketing_strategy_task,
            create_kpi_definition_task,
            create_report_synthesis_task
        )
        from crewai import Crew, Process
        
        # Initialize agents
        print("Initializing agents...")
        agents = {
            'product_idea_intake': create_product_idea_intake_agent(),
            'market_research': create_market_research_analyst_agent(),
            'competitive_analyst': create_competitive_analyst_agent(),
            'strategic_analyst': create_strategic_analyst_agent(),
            'financial_analyst': create_financial_analyst_agent(),
            'technical_feasibility': create_technical_feasibility_assessor_agent(),
            'customer_insights': create_customer_insights_analyst_agent(),
            'marketing_strategist': create_marketing_strategist_agent(),
            'kpi_metrics': create_kpi_metrics_definer_agent(),
            'report_synthesizer': create_report_synthesizer_agent()
        }
        
        # Helper to run a single task with its agent
        def run_task(task, agent, task_name):
            try:
                print(f"Running {task_name}...")
                crew = Crew(
                    agents=[agent],
                    tasks=[task],
                    process=Process.sequential,
                    verbose=True
                )
                return crew.kickoff()
            except Exception as e:
                print(f"❌ Error in {task_name}: {e}")
                return f"Error in {task_name}: {str(e)}"
        
        # Run each task sequentially
        results = {}
        
        # 1. Product Idea Structuring
        task = create_product_idea_structuring_task(product_idea, agents['product_idea_intake'])
        results['product_idea_structuring'] = run_task(task, agents['product_idea_intake'], "Product Idea Structuring")
        
        # 2. Market Research
        task = create_market_research_task(agents['market_research'])
        results['market_research'] = run_task(task, agents['market_research'], "Market Research")
        
        # 3. Competitive Analysis
        task = create_competitive_analysis_task(agents['competitive_analyst'])
        results['competitive_analysis'] = run_task(task, agents['competitive_analyst'], "Competitive Analysis")
        
        # 4. SWOT Analysis
        task = create_swot_analysis_task(agents['strategic_analyst'])
        results['swot_analysis'] = run_task(task, agents['strategic_analyst'], "SWOT Analysis")
        
        # 5. Financial Projections
        task = create_financial_projections_task(agents['financial_analyst'])
        results['financial_projections'] = run_task(task, agents['financial_analyst'], "Financial Projections")
        
        # 6. Technical Feasibility
        task = create_technical_feasibility_task(agents['technical_feasibility'])
        results['technical_feasibility'] = run_task(task, agents['technical_feasibility'], "Technical Feasibility")
        
        # 7. Customer Segmentation
        task = create_customer_segmentation_task(agents['customer_insights'])
        results['customer_segmentation'] = run_task(task, agents['customer_insights'], "Customer Segmentation")
        
        # 8. Marketing Strategy
        task = create_marketing_strategy_task(agents['marketing_strategist'])
        results['marketing_strategy'] = run_task(task, agents['marketing_strategist'], "Marketing Strategy")
        
        # 9. KPI Definition
        task = create_kpi_definition_task(agents['kpi_metrics'])
        results['kpi_definition'] = run_task(task, agents['kpi_metrics'], "KPI Definition")
        
        # 10. Report Synthesis
        task = create_report_synthesis_task(agents['report_synthesizer'], results)
        final_report = run_task(task, agents['report_synthesizer'], "Report Synthesis")
        
        # Generate visualizations
        try:
            from visualization_generator import ProductAnalysisVisualizer
            visualizer = ProductAnalysisVisualizer()
            images = visualizer.generate_all_visualizations(results)
            print(f"📊 Generated {len(images)} visualizations")
        except Exception as e:
            print(f"❌ Visualization generation failed: {e}")
            images = []
        
        # Generate HTML report
        try:
            from webpage import generate_report_webpage
            generate_report_webpage(final_report, images)
            print("📄 HTML report generated successfully")
        except Exception as e:
            print(f"❌ HTML report generation failed: {e}")
        
        print("\n" + "~" * 82)
        print("🎉 COMPREHENSIVE PRODUCT ANALYSIS COMPLETED")
        print("~" * 82)
        print(final_report)
        print("~" * 82)
        
        return final_report
        
    except Exception as e:
        print(f"❌ Full analysis failed: {e}")
        traceback.print_exc()
        return None

def main():
    """Main function with comprehensive error handling"""
    try:
        # Check prerequisites
        if not check_prerequisites():
            return
        
        # Get product idea
        idea = get_product_idea()
        
        # Store product idea (if function exists)
        try:
            from product_store import store_product_idea
            store_product_idea(idea)
            print("✅ Product idea stored successfully!")
        except ImportError:
            print("ℹ️ Product store module not found, skipping storage")
        except Exception as e:
            print(f"⚠️ Product storage failed: {e}")
        
        # Ask user for analysis type
        print("\n🎯 Analysis Options:")
        print("1. Simplified Analysis (Single Agent Test)")
        print("2. Full Comprehensive Analysis")
        
        while True:
            choice = input("\nSelect analysis type (1 or 2): ").strip()
            if choice in ['1', '2']:
                break
            print("❌ Please enter 1 or 2")
        
        if choice == '1':
            # Test single agent first
            if not test_single_agent():
                print("❌ Single agent test failed. Please fix the issues above.")
                return
            
            # Run simplified analysis
            result = run_simplified_analysis(idea)
            
        else:
            # Run full analysis
            result = run_full_analysis(idea)
        
        if result:
            print("\n✨ Analysis completed successfully!")
        else:
            print("\n❌ Analysis failed. Please check the errors above.")
        
    except KeyboardInterrupt:
        print("\n\n⏹️ Analysis interrupted by user")
        
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("\n🔧 Full error trace:")
        traceback.print_exc()
        
        print("\n💡 Common solutions:")
        print("   - Check your .env file and API key")
        print("   - Verify internet connection")
        print("   - Check API quota and billing")
        print("   - Ensure all dependencies are installed")

if __name__ == "__main__":
    main()