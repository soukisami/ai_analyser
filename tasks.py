from crewai import Task

def create_product_idea_structuring_task(product_idea, agent):
    """Create the product idea structuring task"""
    return Task(
        description=f"""
        Structure and validate the following product idea into a standardized format:
        
        Product Idea: "{product_idea}"
        
        Organize this idea into:
        1. Product name and description
        2. Core problem statement
        3. Proposed solution
        4. Initial target audience
        5. Unique value proposition
        6. Key assumptions to validate
        """,
        expected_output=(
            "A structured product idea document with clearly defined sections:\n"
            "- Product Overview\n"
            "- Problem Statement\n"
            "- Solution Description\n"
            "- Target Audience\n"
            "- Value Proposition\n"
            "- Key Assumptions"
        ),
        agent=agent
    )

def create_market_research_task(agent):
    """Create the market research task"""
    return Task(
        description="""
        Conduct comprehensive market research based on the structured product idea.
        
        Research areas:
        1. Market size and growth potential
        2. Industry trends and dynamics
        3. Regulatory considerations
        4. Market entry barriers
        5. Distribution channels
        6. Pricing benchmarks
        """,
        expected_output=(
            "A detailed market research report including:\n"
            "- Total Addressable Market (TAM) analysis\n"
            "- Market trends and growth projections\n"
            "- Industry landscape overview\n"
            "- Regulatory and compliance requirements\n"
            "- Go-to-market channel analysis\n"
            "- Pricing strategy recommendations"
        ),
        agent=agent
    )

def create_competitive_analysis_task(agent):
    """Create the competitive analysis task"""
    return Task(
        description="""
        Perform comprehensive competitive analysis to understand the competitive landscape.
        
        Analysis focus:
        1. Direct and indirect competitors identification
        2. Competitor strengths and weaknesses
        3. Market positioning analysis
        4. Feature comparison matrix
        5. Pricing strategy analysis
        6. Differentiation opportunities
        """,
        expected_output=(
            "A comprehensive competitive analysis report containing:\n"
            "- Competitor landscape map\n"
            "- Detailed competitor profiles\n"
            "- Feature comparison matrix\n"
            "- Competitive positioning analysis\n"
            "- Differentiation opportunities\n"
            "- Competitive threats assessment"
        ),
        agent=agent
    )

def create_swot_analysis_task(agent):
    """Create the SWOT analysis task"""
    return Task(
        description="""
        Conduct a comprehensive SWOT analysis based on all gathered information.
        
        Analyze:
        1. Internal Strengths - what advantages does this product have?
        2. Internal Weaknesses - what areas need improvement?
        3. External Opportunities - what market opportunities exist?
        4. External Threats - what challenges could impact success?
        5. Strategic implications and recommendations
        """,
        expected_output=(
            "A detailed SWOT analysis report with:\n"
            "- Strengths analysis with supporting evidence\n"
            "- Weaknesses identification and mitigation strategies\n"
            "- Market opportunities assessment\n"
            "- Threats analysis and risk mitigation\n"
            "- Strategic recommendations based on SWOT findings"
        ),
        agent=agent
    )

def create_financial_projections_task(agent):
    """Create the financial projections task"""
    return Task(
        description="""
        Develop comprehensive financial projections and business model analysis.
        
        Create projections for:
        1. Revenue model and streams
        2. Cost structure analysis
        3. 3-year financial projections
        4. Break-even analysis
        5. Funding requirements
        6. ROI and profitability analysis
        """,
        expected_output=(
            "A comprehensive financial analysis including:\n"
            "- Revenue model definition\n"
            "- Detailed cost structure breakdown\n"
            "- 3-year P&L projections\n"
            "- Cash flow analysis\n"
            "- Break-even analysis\n"
            "- Investment requirements and ROI projections"
        ),
        agent=agent
    )

def create_technical_feasibility_task(agent):
    """Create the technical feasibility task"""
    return Task(
        description="""
        Assess the technical feasibility and requirements for product development.
        
        Evaluate:
        1. Technology stack requirements
        2. Development complexity assessment
        3. Scalability considerations
        4. Security and compliance requirements
        5. Integration challenges
        6. Implementation timeline and milestones
        """,
        expected_output=(
            "A technical feasibility report containing:\n"
            "- Technology architecture recommendations\n"
            "- Development complexity analysis\n"
            "- Scalability and performance considerations\n"
            "- Security and compliance requirements\n"
            "- Technical risk assessment\n"
            "- Development roadmap and timeline"
        ),
        agent=agent
    )

def create_customer_segmentation_task(agent):
    """Create the customer segmentation task"""
    return Task(
        description="""
        Develop detailed customer segmentation and user personas.
        
        Create:
        1. Customer segment identification
        2. Detailed user personas
        3. Customer journey mapping
        4. Needs and pain points analysis
        5. Behavioral patterns analysis
        6. Customer acquisition strategies
        """,
        expected_output=(
            "A comprehensive customer insights report with:\n"
            "- Customer segmentation matrix\n"
            "- Detailed user personas with demographics and psychographics\n"
            "- Customer journey maps\n"
            "- Pain points and needs analysis\n"
            "- Behavioral insights and preferences\n"
            "- Customer acquisition recommendations"
        ),
        agent=agent
    )

def create_marketing_strategy_task(agent):
    """Create the marketing strategy task"""
    return Task(
        description="""
        Develop a comprehensive go-to-market and marketing strategy.
        
        Develop:
        1. Brand positioning and messaging
        2. Marketing channel strategy
        3. Content marketing approach
        4. Launch strategy and timeline
        5. Customer acquisition tactics
        6. Marketing budget recommendations
        """,
        expected_output=(
            "A comprehensive marketing strategy document including:\n"
            "- Brand positioning and value proposition\n"
            "- Messaging framework and key messages\n"
            "- Marketing channel mix and strategy\n"
            "- Go-to-market launch plan\n"
            "- Customer acquisition funnel and tactics\n"
            "- Marketing budget allocation and ROI expectations"
        ),
        agent=agent
    )

def create_kpi_definition_task(agent):
    """Create the KPI definition task"""
    return Task(
        description="""
        Define key performance indicators and success metrics framework.
        
        Establish:
        1. Business performance KPIs
        2. Product usage metrics
        3. Customer satisfaction indicators
        4. Financial performance metrics
        5. Operational efficiency measures
        6. Growth and retention metrics
        """,
        expected_output=(
            "A comprehensive KPI framework document with:\n"
            "- Business KPIs with targets and benchmarks\n"
            "- Product metrics and analytics requirements\n"
            "- Customer success and satisfaction metrics\n"
            "- Financial performance indicators\n"
            "- Operational metrics and efficiency measures\n"
            "- Measurement methodology and reporting cadence"
        ),
        agent=agent
    )

def create_report_synthesis_task(agent, previous_results):
    """Create the comprehensive report synthesis task"""
    return Task(
        description=f"""
        Synthesize all previous analyses into a comprehensive strategic report.

        Product Idea Structuring:
        {previous_results.get('product_idea_structuring', '')}

        Market Research:
        {previous_results.get('market_research', '')}

        Competitive Analysis:
        {previous_results.get('competitive_analysis', '')}

        SWOT Analysis:
        {previous_results.get('swot_analysis', '')}

        Financial Projections:
        {previous_results.get('financial_projections', '')}

        Technical Feasibility:
        {previous_results.get('technical_feasibility', '')}

        Customer Segmentation:
        {previous_results.get('customer_segmentation', '')}

        Marketing Strategy:
        {previous_results.get('marketing_strategy', '')}

        KPI Definition:
        {previous_results.get('kpi_definition', '')}

        Compile and synthesize:
        1. Executive summary with key findings
        2. Strategic recommendations
        3. Implementation roadmap
        4. Risk analysis and mitigation
        5. Success factors and critical dependencies
        6. Next steps and action items
        """,
        expected_output=(
            "A comprehensive strategic report including:\n"
            "- Executive Summary with key insights\n"
            "- Strategic recommendations and rationale\n"
            "- Detailed implementation roadmap\n"
            "- Risk assessment and mitigation strategies\n"
            "- Critical success factors\n"
            "- Prioritized action plan and next steps"
        ),
        agent=agent
    )

def create_visualization_generation_task(agent):
    """Create the visualization generation task"""
    return Task(
        description="""
        Generate visual representations and charts for key insights and data.
        
        Create visualizations for:
        1. Market analysis charts and graphs
        2. Competitive positioning maps
        3. Financial projection charts
        4. Customer segmentation diagrams
        5. Implementation timeline visualizations
        6. KPI dashboard mockups
        """,
        expected_output=(
            "A collection of data visualizations including:\n"
            "- Market analysis charts and infographics\n"
            "- Competitive landscape positioning maps\n"
            "- Financial projection graphs and charts\n"
            "- Customer segment visualization\n"
            "- Implementation Gantt charts\n"
            "- KPI dashboard design recommendations"
        ),
        agent=agent
    )