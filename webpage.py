import webbrowser
import os
import base64

def generate_report_webpage(analysis_text, image_paths, output_file="product_report.html"):
    """Generate an enhanced HTML report with embedded visualizations"""
    
    # Start HTML with enhanced styling
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>📊 Comprehensive Product Analysis Report</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                background: white;
                border-radius: 15px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                overflow: hidden;
            }
            .header {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 40px;
                text-align: center;
            }
            .header h1 {
                margin: 0;
                font-size: 2.5em;
                font-weight: 300;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
            .header p {
                margin: 10px 0 0 0;
                font-size: 1.2em;
                opacity: 0.9;
            }
            .content {
                padding: 40px;
            }
            .section {
                margin-bottom: 50px;
                padding: 30px;
                background: #f8f9fa;
                border-radius: 10px;
                border-left: 5px solid #667eea;
            }
            .section h2 {
                color: #333;
                margin-top: 0;
                font-size: 1.8em;
                display: flex;
                align-items: center;
                gap: 15px;
            }
            .analysis-text {
                background: white;
                padding: 30px;
                border-radius: 10px;
                font-size: 1.1em;
                line-height: 1.8;
                white-space: pre-wrap;
                border: 1px solid #e9ecef;
                box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            }
            .visualizations {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
                gap: 30px;
                margin-top: 40px;
            }
            .viz-card {
                background: white;
                border-radius: 15px;
                padding: 20px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .viz-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 20px 40px rgba(0,0,0,0.15);
            }
            .viz-card h3 {
                color: #333;
                margin-top: 0;
                font-size: 1.3em;
                text-align: center;
                padding-bottom: 15px;
                border-bottom: 2px solid #667eea;
            }
            .viz-card img {
                width: 100%;
                height: auto;
                border-radius: 10px;
                margin-top: 15px;
            }
            .toc {
                background: #f8f9fa;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 30px;
            }
            .toc h3 {
                margin-top: 0;
                color: #333;
            }
            .toc ul {
                list-style: none;
                padding: 0;
            }
            .toc li {
                padding: 8px 0;
                border-bottom: 1px solid #e9ecef;
            }
            .toc a {
                color: #667eea;
                text-decoration: none;
                font-weight: 500;
            }
            .toc a:hover {
                color: #764ba2;
            }
            .footer {
                text-align: center;
                padding: 30px;
                background: #f8f9fa;
                color: #666;
                margin-top: 50px;
            }
            .timestamp {
                font-size: 0.9em;
                opacity: 0.7;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>📊 Comprehensive Product Analysis Report</h1>
                <p>AI-Powered Market Intelligence & Strategic Insights</p>
                <p class="timestamp">Generated on: """ + str(datetime.now().strftime("%B %d, %Y at %I:%M %p")) + """</p>
            </div>
            
            <div class="content">
                <div class="toc">
                    <h3>📋 Table of Contents</h3>
                    <ul>
                        <li><a href="#analysis">🔍 Analysis Report</a></li>
                        <li><a href="#visualizations">📊 Visual Insights</a></li>
                    </ul>
                </div>
                
                <div class="section" id="analysis">
                    <h2>🔍 Comprehensive Analysis Report</h2>
                    <div class="analysis-text">""" + str(analysis_text) + """</div>
                </div>
                
                <div class="section" id="visualizations">
                    <h2>📊 Visual Insights & Data Visualizations</h2>
                    <div class="visualizations">
    """
    
    # Add visualization cards with proper titles and embedded images
    viz_titles = {
        'market_size_analysis.png': '📈 Market Size Analysis & Growth Projections',
        'competitive_positioning.png': '🎯 Competitive Positioning Map',
        'financial_projections.png': '💰 Financial Projections & Revenue Forecast',
        'customer_segmentation.png': '👥 Customer Segmentation & Demographics',
        'kpi_dashboard.png': '📊 Key Performance Indicators Dashboard',
        'swot_analysis.png': '⚖️ SWOT Analysis Matrix',
        'marketing_strategy.png': '📢 Marketing Strategy & Budget Allocation',
        'tech_feasibility.png': '🔧 Technical Feasibility Assessment'
    }
    
    # Process each image
    for img_path in image_paths:
        if os.path.exists(img_path):
            try:
                # Get filename for title lookup
                filename = os.path.basename(img_path)
                title = viz_titles.get(filename, f"📊 {filename.replace('_', ' ').title()}")
                
                # Convert image to base64 for embedding
                with open(img_path, 'rb') as img_file:
                    img_data = base64.b64encode(img_file.read()).decode('utf-8')
                    img_src = f"data:image/png;base64,{img_data}"
                
                html_content += f"""
                        <div class="viz-card">
                            <h3>{title}</h3>
                            <img src="{img_src}" alt="{title}">
                        </div>
                """
            except Exception as e:
                print(f"Warning: Could not embed image {img_path}: {e}")
                # Fallback to file path
                html_content += f"""
                        <div class="viz-card">
                            <h3>{viz_titles.get(os.path.basename(img_path), 'Visualization')}</h3>
                            <img src="{img_path}" alt="Visualization">
                        </div>
                """
    
    # Close HTML
    html_content += """
                    </div>
                </div>
            </div>
            
            <div class="footer">
                <p>🤖 Generated by AI-Powered Product Analysis System</p>
                <p>This report provides comprehensive insights for strategic decision making.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    # Write HTML file
    try:
        with open(output_file, "w", encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Enhanced report webpage generated: {output_file}")
        
        # Open in browser
        file_path = f"file://{os.path.abspath(output_file)}"
        webbrowser.open(file_path)
        print(f"🌐 Opening report in browser: {file_path}")
        
    except Exception as e:
        print(f"❌ Error generating webpage: {e}")

# Add datetime import at the top
from datetime import datetime