from webpage import generate_report_webpage
from crewai import Crew, Process 
from visualization_generator import ProductAnalysisVisualizer  # import your class
from product_store import store_product_idea
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
    create_report_synthesis_task,
    create_visualization_generation_task
)


def get_product_idea():
    print("Welcome to AI-Powered Comprehensive Product Analysis System")
    print("~" * 60)
    idea = input("Please enter your product idea: ")
    return idea

def run_analysis_and_generate_report(product_idea):
    # Initialize agents
    product_idea_intake_agent = create_product_idea_intake_agent()
    market_research_analyst_agent = create_market_research_analyst_agent()
    competitive_analyst_agent = create_competitive_analyst_agent()
    strategic_analyst_agent = create_strategic_analyst_agent()
    financial_analyst_agent = create_financial_analyst_agent()
    technical_feasibility_assessor_agent = create_technical_feasibility_assessor_agent()
    customer_insights_analyst_agent = create_customer_insights_analyst_agent()
    marketing_strategist_agent = create_marketing_strategist_agent()
    kpi_metrics_definer_agent = create_kpi_metrics_definer_agent()
    report_synthesizer_agent = create_report_synthesizer_agent()

    # Helper to run a single task with its agent
    def run_task(task, agent):
        crew = Crew(
            agents=[agent],
            tasks=[task],
            process=Process.sequential
        )
        return crew.kickoff()

    # Run each task sequentially and collect results
    product_idea_structuring_task = create_product_idea_structuring_task(product_idea, product_idea_intake_agent)
    product_idea_structuring_result = run_task(product_idea_structuring_task, product_idea_intake_agent)

    market_research_task = create_market_research_task(market_research_analyst_agent)
    market_research_result = run_task(market_research_task, market_research_analyst_agent)

    competitive_analysis_task = create_competitive_analysis_task(competitive_analyst_agent)
    competitive_analysis_result = run_task(competitive_analysis_task, competitive_analyst_agent)

    swot_analysis_task = create_swot_analysis_task(strategic_analyst_agent)
    swot_analysis_result = run_task(swot_analysis_task, strategic_analyst_agent)

    financial_projections_task = create_financial_projections_task(financial_analyst_agent)
    financial_projections_result = run_task(financial_projections_task, financial_analyst_agent)

    technical_feasibility_task = create_technical_feasibility_task(technical_feasibility_assessor_agent)
    technical_feasibility_result = run_task(technical_feasibility_task, technical_feasibility_assessor_agent)

    customer_segmentation_task = create_customer_segmentation_task(customer_insights_analyst_agent)
    customer_segmentation_result = run_task(customer_segmentation_task, customer_insights_analyst_agent)

    marketing_strategy_task = create_marketing_strategy_task(marketing_strategist_agent)
    marketing_strategy_result = run_task(marketing_strategy_task, marketing_strategist_agent)

    kpi_definition_task = create_kpi_definition_task(kpi_metrics_definer_agent)
    kpi_definition_result = run_task(kpi_definition_task, kpi_metrics_definer_agent)

    previous_results = {
        "product_idea_structuring": product_idea_structuring_result,
        "market_research": market_research_result,
        "competitive_analysis": competitive_analysis_result,
        "swot_analysis": swot_analysis_result,
        "financial_projections": financial_projections_result,
        "technical_feasibility": technical_feasibility_result,
        "customer_segmentation": customer_segmentation_result,
        "marketing_strategy": marketing_strategy_result,
        "kpi_definition": kpi_definition_result,
    }

    # Synthesize the final report
    report_synthesis_task = create_report_synthesis_task(report_synthesizer_agent, previous_results)
    report = run_task(report_synthesis_task, report_synthesizer_agent)

    return previous_results, report

def print_analysis_phases():
    """Print the analysis phases for user information"""
    phases = [
        "1. 📝 Product Idea Structuring",
        "2. 📊 Market Research Analysis", 
        "3. 🏢 Competitive Landscape Analysis",
        "4. 🎯 SWOT Strategic Analysis",
        "5. 💰 Financial Projections",
        "6. ⚙️  Technical Feasibility Assessment",
        "7. 👥 Customer Segmentation & Insights",
        "8. 📢 Marketing Strategy Development",
        "9. 📈 KPI Metrics Definition",
        "10. 📋 Comprehensive Report Synthesis",
        "11. 📊 Data Visualization Generation"
    ]
    
    print("\n🔄 Analysis will proceed through the following phases:")
    print("~" * 60)
    for phase in phases:
        print(phase)
    print("~" * 60)

if __name__ == "__main__":
    try:
        # Get product idea from user
        idea = get_product_idea()
        
        # Store the product idea
        store_product_idea(idea)
        print("✅ Product idea stored successfully!")
        
        # Show analysis phases
        print_analysis_phases()
        
        # Run the comprehensive analysis and generate report
        print("\n🚀 Starting comprehensive product analysis...")
        print("⏳ This may take several minutes to complete...")
        print("-" * 60)
        
        previous_results, result = run_analysis_and_generate_report(idea)

        # Run visualizer with real data
        visualizer = ProductAnalysisVisualizer()
        images = visualizer.generate_all_visualizations(previous_results)

        # Generate HTML report
        generate_report_webpage(result, images)

        
        # Display results
        print("\n" + "~" * 82)
        print("🎉 COMPREHENSIVE PRODUCT ANALYSIS COMPLETED")
        print("~" * 81)
        print(result)
        print("~" * 81)
        
        print("\n✨ Analysis complete! Check the results above for comprehensive insights.")
        
    except Exception as e:
        print(f"❌ An error occurred during analysis: {e}")
        print("\n💡 Troubleshooting tips:")
        print("   - Verify your Google API key is valid and active")
        print("   - Ensure you have enabled the Generative AI API in Google Cloud")
        print("   - Check your internet connection")
        print("   - Verify you have sufficient API quota remaining")
        print("   - Make sure all required dependencies are installed (crewai, etc.)")
        print("\n🔧 For detailed error information, check the full error trace above.")
        print(f"Error: {e}")
        print("   - Make sure all required dependencies are installed (crewai, etc.)")
        print("\n🔧 For detailed error information, check the full error trace above.")
        print(f"Error: {e}")
        generate_report_webpage(result, images)

        
        # Display results
        print("\n" + "~" * 82)
        print("🎉 COMPREHENSIVE PRODUCT ANALYSIS COMPLETED")
        print("~" * 81)
        print(result)
        print("~" * 81)
        
        print("\n✨ Analysis complete! Check the results above for comprehensive insights.")
        
    except Exception as e:
        print(f"❌ An error occurred during analysis: {e}")
        print("\n💡 Troubleshooting tips:")
        print("   - Verify your Google API key is valid and active")
        print("   - Ensure you have enabled the Generative AI API in Google Cloud")
        print("   - Check your internet connection")
        print("   - Verify you have sufficient API quota remaining")
        print("   - Make sure all required dependencies are installed (crewai, etc.)")
        print("\n🔧 For detailed error information, check the full error trace above.")
        print(f"Error: {e}")
        print("   - Make sure all required dependencies are installed (crewai, etc.)")
        print("\n🔧 For detailed error information, check the full error trace above.")
        print(f"Error: {e}")
