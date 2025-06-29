from crewai import Agent, LLM
import os

def get_llm():
    """Initialize Google Gemini LLM"""
    # Get API key from environment variable for security
    api_key = "AIzaSyDqK1g4s5W0cSRiiyrAhJafGACaKiwCBs4"
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set")

    return LLM(
        model="gemini/gemini-1.5-flash",
        temperature=0.7,
        api_key=api_key,
        max_tokens=2000
    )

def create_product_idea_intake_agent():
    """Create the product idea intake agent"""
    llm = get_llm()
    return Agent(
        role="Product Idea Intake Specialist",
        goal="Structure and validate incoming product ideas into a standardized format",
        backstory=(
            "You are a product intake specialist who excels at organizing raw product ideas "
            "into structured, actionable formats. You ensure all necessary information is captured "
            "and properly categorized for downstream analysis."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_market_research_analyst_agent():
    """Create the market research analyst agent"""
    llm = get_llm()
    return Agent(
        role="Market Research Analyst",
        goal="Conduct comprehensive market research and identify market opportunities",
        backstory=(
            "You are an experienced market research analyst with expertise in identifying "
            "market trends, sizing opportunities, and understanding industry dynamics. "
            "You provide data-driven insights about market potential and positioning."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_competitive_analyst_agent():
    """Create the competitive analyst agent"""
    llm = get_llm()
    return Agent(
        role="Competitive Intelligence Analyst",
        goal="Analyze competitive landscape and identify differentiation opportunities",
        backstory=(
            "You are a competitive intelligence expert who specializes in analyzing competitors, "
            "identifying market gaps, and finding strategic positioning opportunities. "
            "You provide insights on competitive advantages and threats."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_strategic_analyst_agent():
    """Create the strategic analyst agent"""
    llm = get_llm()
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

def create_financial_analyst_agent():
    """Create the financial analyst agent"""
    llm = get_llm()
    return Agent(
        role="Financial Projections Analyst",
        goal="Create detailed financial projections and business models",
        backstory=(
            "You are a financial analyst specializing in startup and product financial modeling. "
            "You create comprehensive financial projections, revenue models, and cost structures "
            "to evaluate business viability and investment requirements."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_technical_feasibility_assessor_agent():
    """Create the technical feasibility assessor agent"""
    llm = get_llm()
    return Agent(
        role="Technical Feasibility Assessor",
        goal="Evaluate technical requirements and implementation feasibility",
        backstory=(
            "You are a senior technical architect with expertise in evaluating the technical "
            "feasibility of product ideas. You assess technology requirements, development "
            "complexity, scalability concerns, and implementation roadmaps."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_customer_insights_analyst_agent():
    """Create the customer insights analyst agent"""
    llm = get_llm()
    return Agent(
        role="Customer Insights Analyst",
        goal="Analyze customer segments and develop user personas",
        backstory=(
            "You are a customer insights specialist who excels at understanding user behavior, "
            "creating detailed customer segments, and developing comprehensive user personas. "
            "You provide deep insights into customer needs and motivations."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_marketing_strategist_agent():
    """Create the marketing strategist agent"""
    llm = get_llm()
    return Agent(
        role="Marketing Strategy Specialist",
        goal="Develop comprehensive go-to-market strategies",
        backstory=(
            "You are a marketing strategist with expertise in developing go-to-market strategies, "
            "positioning, messaging, and marketing channel optimization. You create actionable "
            "marketing plans that drive product success."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_kpi_metrics_definer_agent():
    """Create the KPI metrics definer agent"""
    llm = get_llm()
    return Agent(
        role="KPI Metrics Definition Specialist",
        goal="Define key performance indicators and success metrics",
        backstory=(
            "You are a metrics and analytics expert who specializes in defining meaningful KPIs "
            "and success metrics for products. You establish measurement frameworks that track "
            "product performance and business outcomes."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_report_synthesizer_agent():
    """Create the report synthesizer agent"""
    llm = get_llm()
    return Agent(
        role="Strategic Report Synthesizer",
        goal="Synthesize all analyses into comprehensive strategic reports",
        backstory=(
            "You are a senior business consultant who excels at synthesizing complex analyses "
            "from multiple sources into clear, actionable strategic reports. You create "
            "executive-level summaries that drive decision-making."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm
    )