import webbrowser
import os

def generate_report_webpage(analysis_text, image_paths, output_file="product_report.html"):
    html_content = "<html><head><title>Product Analysis Report</title></head><body>"
    html_content += "<h1>📊 Comprehensive Product Analysis</h1>"
    html_content += f"<pre style='white-space: pre-wrap; font-family: sans-serif;'>{analysis_text}</pre>"
    html_content += "<h2>🔍 Visual Insights</h2>"

    for img_path in image_paths:
        html_content += f"<div><img src='{img_path}' style='max-width: 800px; margin: 20px 0;'><hr></div>"

    html_content += "</body></html>"

    with open(output_file, "w") as f:
        f.write(html_content)

    print(f"✅ Report page generated: {output_file}")
    webbrowser.open(f"file://{os.path.abspath(output_file)}")