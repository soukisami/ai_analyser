from crewai import Agent, LLM
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_llm():
    """Initialize Google Gemini LLM with error handling"""
    try:
        # Get API key from environment variable
        api_key = os.getenv("LLM_API_KEY")
        if not api_key:
            raise ValueError("LLM_API_KEY environment variable not set. Please check your .env file.")
        
        # Validate API key format (basic check)
        if len(api_key) < 10:
            raise ValueError("LLM_API_KEY appears to be invalid (too short)")
        
        llm = LLM(
            model="gemini/gemini-1.5-flash",
            temperature=0.7,
            api_key=api_key,
            max_tokens=2000
        )
        
        print("✅ LLM initialized successfully")
        return llm
        
    except Exception as e:
        print(f"❌ Error initializing LLM: {e}")
        print("💡 Troubleshooting tips:")
        print("   - Verify your Google API key is valid and active")
        print("   - Ensure you have enabled the Generative AI API in Google Cloud")
        print("   - Check your internet connection")
        print("   - Verify you have sufficient API quota remaining")
        raise

# Initialize LLM globally
llm = get_llm()

def create_product_idea_intake_agent():
    """Create the product idea intake agent with error handling"""
    try:
        return Agent(
            role="Product Intake Architect",
            goal=(
                "Gather, structure, and validate new product ideas by identifying key components "
                "(customer need, features, target market, and constraints), and formatting them "
                "into a consistent, analysis-ready template."
            ),
            backstory=(
                "You are an expert Product Intake Architect with 5+ years working at high-growth startups. "
                "Your expertise is turning vague ideas into crystal-clear briefs that fuel market research, "
                "feasibility studies, and go-to-market strategies. You ask clarifying questions to uncover "
                "hidden assumptions and ensure completeness."
            ),
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
    except Exception as e:
        print(f"❌ Error creating product idea intake agent: {e}")
        raise

def create_market_research_analyst_agent():
    """Create the market research analyst agent"""
    try:
        return Agent(
            role="Strategic Market Insights Lead",
            goal=(
                "Perform comprehensive market research by analyzing market size, growth rates, "
                "competitor landscape, customer segments, and emerging trends to deliver "
                "actionable opportunity assessments."
            ),
            backstory=(
                "You are a Strategic Market Insights Lead with 7+ years advising Fortune 500s "
                "and high-growth startups. You excel at synthesizing large datasets, uncovering "
                "underserved segments, and translating raw data into strategic recommendations."
            ),
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
    except Exception as e:
        print(f"❌ Error creating market research analyst agent: {e}")
        raise

def create_competitive_analyst_agent():
    """Create the competitive intelligence analyst agent"""
    try:
        return Agent(
            role="Competitive Strategy Architect",
            goal=(
                "Map and analyze the competitive landscape by profiling key players, "
                "benchmarking their offerings, and uncovering strategic gaps to inform "
                "product differentiation and positioning."
            ),
            backstory=(
                "You are a Competitive Strategy Architect with a decade of experience in "
                "corporate strategy and intelligence. You excel at dissecting competitors' "
                "product suites, pricing models, and go-to-market tactics."
            ),
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
    except Exception as e:
        print(f"❌ Error creating competitive analyst agent: {e}")
        raise

def create_strategic_analyst_agent():
    """Create the strategic analyst agent"""
    try:
        return Agent(
            role="Strategic Business Analyst",
            goal="Perform SWOT analysis and strategic planning",
            backstory=(
                "You are a strategic business analyst with deep expertise in business strategy, "
                "SWOT analysis, and strategic planning. You identify strengths, weaknesses, "
                "opportunities, and threats to guide strategic decision-making."
            ),
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
    except Exception as e:
        print(f"❌ Error creating strategic analyst agent: {e}")
        raise

def create_financial_analyst_agent():
    """Create the financial projections analyst agent"""
    try:
        return Agent(
            role="Financial Modeling Architect",
            goal=(
                "Build robust financial models including revenue forecasts, expense budgets, "
                "margin analyses, cash flow projections, and break-even calculations to "
                "assess business viability."
            ),
            backstory=(
                "You are a Financial Modeling Architect with 10+ years of experience in "
                "startup finance and venture capital. You specialize in translating business "
                "assumptions into clear, scalable financial structures."
            ),
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
    except Exception as e:
        print(f"❌ Error creating financial analyst agent: {e}")
        raise

def create_technical_feasibility_assessor_agent():
    """Create the technical feasibility assessor agent"""
    try:
        return Agent(
            role="Technical Feasibility Architect",
            goal=(
                "Assess product ideas by mapping out architectural requirements, technology stacks, "
                "integration points, and development effort estimates to ensure technical viability."
            ),
            backstory=(
                "You are a Technical Feasibility Architect with 12+ years of experience "
                "designing and delivering complex systems. You excel at decomposing features "
                "into implementation tasks and identifying potential technical risks early."
            ),
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
    except Exception as e:
        print(f"❌ Error creating technical feasibility assessor agent: {e}")
        raise

def create_customer_insights_analyst_agent():
    """Create the customer insights analyst agent"""
    try:
        return Agent(
            role="Customer Empathy Architect",
            goal=(
                "Conduct in-depth customer analysis by segmenting users, mapping journeys, "
                "and crafting data-driven personas that capture needs, pain points, and "
                "motivations to inform product features and messaging."
            ),
            backstory=(
                "You are a Customer Empathy Architect with 6+ years guiding product strategy "
                "through user research and behavioral analysis. You leverage quantitative and "
                "qualitative methods to uncover latent customer needs."
            ),
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
    except Exception as e:
        print(f"❌ Error creating customer insights analyst agent: {e}")
        raise

def create_marketing_strategist_agent():
    """Create the go-to-market strategy architect agent"""
    try:
        return Agent(
            role="Go-to-Market Strategy Architect",
            goal=(
                "Design end-to-end go-to-market plans by defining product positioning, "
                "messaging frameworks, channel strategies, and launch timelines to "
                "maximize market adoption and ROI."
            ),
            backstory=(
                "You are a Go-to-Market Strategy Architect with 9+ years driving product "
                "launches at fast-growing tech companies. You specialize in translating "
                "product value into compelling narratives and selecting optimal channel mixes."
            ),
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
    except Exception as e:
        print(f"❌ Error creating marketing strategist agent: {e}")
        raise

def create_kpi_metrics_definer_agent():
    """Create the KPI and metrics definition specialist agent"""
    try:
        return Agent(
            role="Performance Metrics Architect",
            goal=(
                "Establish key performance indicators (KPIs) and success metrics by defining "
                "measurement frameworks, setting realistic targets, and linking metrics to "
                "strategic objectives across product, marketing, sales, and finance domains."
            ),
            backstory=(
                "You are a Performance Metrics Architect with 8+ years of experience in "
                "analytics and business intelligence. You have built end-to-end measurement "
                "systems ensuring metrics are actionable and aligned with business objectives."
            ),
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
    except Exception as e:
        print(f"❌ Error creating KPI metrics definer agent: {e}")
        raise

def create_report_synthesizer_agent():
    """Create the strategic report synthesizer agent"""
    try:
        return Agent(
            role="Executive Insights Architect",
            goal=(
                "Aggregate and synthesize outputs from all analysis agents into cohesive, "
                "data-driven strategic reports with executive summaries, key findings, "
                "and recommendations that inform high-level decision-making."
            ),
            backstory=(
                "You are an Executive Insights Architect with 15+ years as a senior business "
                "consultant and C-level advisor. You excel at weaving together market research, "
                "financial models, and customer insights into clear, compelling narratives."
            ),
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
    except Exception as e:
        print(f"❌ Error creating report synthesizer agent: {e}")
        raise