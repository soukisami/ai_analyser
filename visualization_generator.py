import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
from matplotlib.patches import Circle
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.offline as pyo

class ProductAnalysisVisualizer:
    def __init__(self, output_dir="visualizations"):
        """Initialize the visualizer with output directory"""
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Set style for matplotlib
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
    
    def create_market_size_chart(self, market_data=None):
        """Create market size and growth projection chart"""
        if market_data is None:
            # Sample data - replace with actual market research data
            years = ['2024', '2025', '2026', '2027', '2028']
            tam = [100, 120, 145, 175, 210]  # Total Addressable Market in millions
            sam = [25, 35, 50, 70, 95]       # Serviceable Addressable Market
            som = [5, 8, 15, 25, 40]         # Serviceable Obtainable Market
        else:
            years = market_data['years']
            tam = market_data['tam']
            sam = market_data['sam']
            som = market_data['som']
        
        fig, ax = plt.subplots(figsize=(12, 8))
        
        x = np.arange(len(years))
        width = 0.25
        
        bars1 = ax.bar(x - width, tam, width, label='TAM (Total Addressable Market)', alpha=0.8)
        bars2 = ax.bar(x, sam, width, label='SAM (Serviceable Addressable Market)', alpha=0.8)
        bars3 = ax.bar(x + width, som, width, label='SOM (Serviceable Obtainable Market)', alpha=0.8)
        
        ax.set_xlabel('Year', fontsize=12)
        ax.set_ylabel('Market Size ($ Millions)', fontsize=12)
        ax.set_title('Market Size Analysis & Growth Projections', fontsize=16, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(years)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Add value labels on bars
        for bars in [bars1, bars2, bars3]:
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                       f'${height}M', ha='center', va='bottom', fontsize=10)
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/market_size_analysis.png', dpi=300, bbox_inches='tight')
        plt.close()
        return f'{self.output_dir}/market_size_analysis.png'
    
    def create_competitive_positioning_map(self, competitors_data=None):
        """Create competitive positioning map"""
        if competitors_data is None:
            # Sample data - replace with actual competitive analysis
            competitors = {
                'Our Product': {'price': 50, 'features': 85, 'market_share': 0},
                'Competitor A': {'price': 80, 'features': 70, 'market_share': 25},
                'Competitor B': {'price': 60, 'features': 60, 'market_share': 20},
                'Competitor C': {'price': 40, 'features': 45, 'market_share': 15},
                'Competitor D': {'price': 90, 'features': 90, 'market_share': 30}
            }
        else:
            competitors = competitors_data
        
        fig, ax = plt.subplots(figsize=(12, 10))
        
        for name, data in competitors.items():
            size = max(100, data['market_share'] * 20) if data['market_share'] > 0 else 200
            color = 'red' if name == 'Our Product' else 'blue'
            alpha = 1.0 if name == 'Our Product' else 0.6
            
            ax.scatter(data['price'], data['features'], s=size, alpha=alpha, 
                      c=color, edgecolors='black', linewidth=2)
            ax.annotate(name, (data['price'], data['features']), 
                       xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold')
        
        ax.set_xlabel('Price Point (Higher →)', fontsize=12)
        ax.set_ylabel('Feature Richness (Higher →)', fontsize=12)
        ax.set_title('Competitive Positioning Map', fontsize=16, fontweight='bold')
        ax.grid(True, alpha=0.3)
        
        # Add quadrant labels
        ax.text(0.02, 0.98, 'Low Price\nHigh Features', transform=ax.transAxes, 
                fontsize=10, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))
        ax.text(0.98, 0.98, 'High Price\nHigh Features', transform=ax.transAxes, 
                fontsize=10, verticalalignment='top', horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/competitive_positioning.png', dpi=300, bbox_inches='tight')
        plt.close()
        return f'{self.output_dir}/competitive_positioning.png'
    
    def create_financial_projections_chart(self, financial_data=None):
        """Create financial projections chart"""
        if financial_data is None:
            # Sample data - replace with actual financial projections
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            revenue = [10, 15, 25, 35, 50, 65, 80, 95, 110, 125, 140, 160]
            costs = [30, 28, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
            profit = [r - c for r, c in zip(revenue, costs)]
        else:
            months = financial_data['months']
            revenue = financial_data['revenue']
            costs = financial_data['costs']
            profit = financial_data['profit']
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
        
        # Revenue and Costs
        ax1.plot(months, revenue, marker='o', linewidth=3, label='Revenue', color='green')
        ax1.plot(months, costs, marker='s', linewidth=3, label='Costs', color='red')
        ax1.fill_between(months, revenue, alpha=0.3, color='green')
        ax1.fill_between(months, costs, alpha=0.3, color='red')
        ax1.set_ylabel('Amount ($000)', fontsize=12)
        ax1.set_title('Revenue vs Costs Projection (Year 1)', fontsize=14, fontweight='bold')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Profit/Loss
        colors = ['green' if p >= 0 else 'red' for p in profit]
        bars = ax2.bar(months, profit, color=colors, alpha=0.7)
        ax2.axhline(y=0, color='black', linestyle='-', linewidth=1)
        ax2.set_ylabel('Profit/Loss ($000)', fontsize=12)
        ax2.set_xlabel('Month', fontsize=12)
        ax2.set_title('Monthly Profit/Loss Projection', fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height + (1 if height >= 0 else -3),
                    f'${height}K', ha='center', va='bottom' if height >= 0 else 'top', fontsize=9)
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/financial_projections.png', dpi=300, bbox_inches='tight')
        plt.close()
        return f'{self.output_dir}/financial_projections.png'
    
    def create_customer_segmentation_chart(self, customer_data=None):
        """Create customer segmentation pie chart and demographics"""
        if customer_data is None:
            # Sample data - replace with actual customer insights
            segments = {
                'Tech Enthusiasts': 25,
                'Business Professionals': 35,
                'Cost-Conscious Users': 20,
                'Premium Seekers': 15,
                'Early Adopters': 5
            }
            demographics = {
                'Age Groups': {'18-25': 20, '26-35': 40, '36-45': 25, '46-55': 10, '55+': 5},
                'Income Levels': {'<$50K': 15, '$50K-$75K': 30, '$75K-$100K': 35, '$100K+': 20}
            }
        else:
            segments = customer_data['segments']
            demographics = customer_data['demographics']
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # Customer Segments Pie Chart
        colors = plt.cm.Set3(np.linspace(0, 1, len(segments)))
        wedges, texts, autotexts = ax1.pie(segments.values(), labels=segments.keys(), autopct='%1.1f%%',
                                          colors=colors, startangle=90, explode=[0.05] * len(segments))
        ax1.set_title('Customer Segmentation', fontsize=14, fontweight='bold')
        
        # Age Groups
        ax2.bar(demographics['Age Groups'].keys(), demographics['Age Groups'].values(), 
                color='skyblue', alpha=0.8)
        ax2.set_title('Target Demographics - Age Groups', fontsize=14, fontweight='bold')
        ax2.set_ylabel('Percentage (%)')
        ax2.tick_params(axis='x', rotation=45)
        
        # Income Levels
        ax3.bar(demographics['Income Levels'].keys(), demographics['Income Levels'].values(),
                color='lightcoral', alpha=0.8)
        ax3.set_title('Target Demographics - Income Levels', fontsize=14, fontweight='bold')
        ax3.set_ylabel('Percentage (%)')
        ax3.tick_params(axis='x', rotation=45)
        
        # Customer Journey Funnel
        funnel_stages = ['Awareness', 'Interest', 'Consideration', 'Purchase', 'Retention']
        funnel_values = [100, 70, 45, 25, 20]
        y_pos = np.arange(len(funnel_stages))
        
        bars = ax4.barh(y_pos, funnel_values, color='lightgreen', alpha=0.8)
        ax4.set_yticks(y_pos)
        ax4.set_yticklabels(funnel_stages)
        ax4.set_xlabel('Conversion Rate (%)')
        ax4.set_title('Customer Journey Funnel', fontsize=14, fontweight='bold')
        
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ax4.text(width + 1, bar.get_y() + bar.get_height()/2, 
                    f'{funnel_values[i]}%', ha='left', va='center')
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/customer_segmentation.png', dpi=300, bbox_inches='tight')
        plt.close()
        return f'{self.output_dir}/customer_segmentation.png'
    
    def create_implementation_timeline(self, timeline_data=None):
        """Create implementation timeline Gantt chart"""
        if timeline_data is None:
            # Sample data - replace with actual implementation plan
            tasks = [
                {'Task': 'Market Research', 'Start': '2024-01-01', 'Duration': 30, 'Progress': 100},
                {'Task': 'Product Design', 'Start': '2024-01-15', 'Duration': 45, 'Progress': 80},
                {'Task': 'Development Phase 1', 'Start': '2024-02-15', 'Duration': 60, 'Progress': 60},
                {'Task': 'Testing & QA', 'Start': '2024-04-01', 'Duration': 30, 'Progress': 40},
                {'Task': 'Marketing Campaign', 'Start': '2024-04-15', 'Duration': 45, 'Progress': 20},
                {'Task': 'Beta Launch', 'Start': '2024-05-01', 'Duration': 30, 'Progress': 0},
                {'Task': 'Full Launch', 'Start': '2024-06-01', 'Duration': 15, 'Progress': 0}
            ]
        else:
            tasks = timeline_data
        
        fig, ax = plt.subplots(figsize=(14, 8))
        
        # Convert dates and create timeline
        for i, task in enumerate(tasks):
            start_date = pd.to_datetime(task['Start'])
            end_date = start_date + timedelta(days=task['Duration'])
            progress_end = start_date + timedelta(days=task['Duration'] * task['Progress'] / 100)
            
            # Draw full timeline bar
            ax.barh(i, task['Duration'], left=start_date.toordinal(), 
                   color='lightgray', alpha=0.6, height=0.6)
            
            # Draw progress bar
            progress_duration = task['Duration'] * task['Progress'] / 100
            ax.barh(i, progress_duration, left=start_date.toordinal(), 
                   color='green', alpha=0.8, height=0.6)
            
            # Add task labels
            ax.text(start_date.toordinal() - 5, i, task['Task'], 
                   ha='right', va='center', fontweight='bold')
            
            # Add progress percentage
            ax.text(end_date.toordinal() + 2, i, f"{task['Progress']}%", 
                   ha='left', va='center', fontsize=10)
        
        # Format x-axis with dates
        ax.set_xlim(pd.to_datetime('2024-01-01').toordinal() - 10, 
                   pd.to_datetime('2024-07-01').toordinal() + 10)
        
        # Convert ordinal dates back to readable format
        ax.set_xlabel('Timeline (2024)', fontsize=12)
        ax.set_ylabel('Project Tasks', fontsize=12)
        ax.set_title('Implementation Timeline & Progress', fontsize=16, fontweight='bold')
        ax.set_yticks(range(len(tasks)))
        ax.set_yticklabels([])
        ax.grid(True, alpha=0.3, axis='x')
        
        # Add month labels
        months = pd.date_range('2024-01-01', '2024-07-01', freq='MS')
        month_ordinals = [date.toordinal() for date in months]
        month_labels = [date.strftime('%b') for date in months]
        ax.set_xticks(month_ordinals)
        ax.set_xticklabels(month_labels)
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/implementation_timeline.png', dpi=300, bbox_inches='tight')
        plt.close()
        return f'{self.output_dir}/implementation_timeline.png'
    
    def create_kpi_dashboard_mockup(self, kpi_data=None):
        """Create KPI dashboard visualization"""
        if kpi_data is None:
            # Sample KPI data
            kpi_data = {
                'revenue': {'current': 85000, 'target': 100000, 'unit': '$'},
                'users': {'current': 2450, 'target': 3000, 'unit': ''},
                'conversion': {'current': 3.2, 'target': 4.0, 'unit': '%'},
                'retention': {'current': 78, 'target': 85, 'unit': '%'},
                'satisfaction': {'current': 4.2, 'target': 4.5, 'unit': '/5'},
                'churn': {'current': 8.5, 'target': 6.0, 'unit': '%'}
            }
        
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        axes = axes.flatten()
        
        kpi_names = list(kpi_data.keys())
        colors = ['green', 'blue', 'orange', 'purple', 'red', 'brown']
        
        for i, (kpi, data) in enumerate(kpi_data.items()):
            ax = axes[i]
            
            current = data['current']
            target = data['target']
            unit = data['unit']
            
            # Create gauge-like visualization
            progress = min(current / target * 100, 100) if target > 0 else 0
            
            # Background circle
            circle = Circle((0.5, 0.5), 0.4, color='lightgray', alpha=0.3)
            ax.add_patch(circle)
            
            # Progress arc (simplified as a pie chart segment)
            theta = np.linspace(0, 2 * np.pi * (progress / 100), 100)
            x = 0.5 + 0.35 * np.cos(theta)
            y = 0.5 + 0.35 * np.sin(theta)
            ax.fill(x, y, color=colors[i], alpha=0.7)
            
            # Center text
            ax.text(0.5, 0.6, f"{current}{unit}", ha='center', va='center', 
                   fontsize=16, fontweight='bold')
            ax.text(0.5, 0.4, f"Target: {target}{unit}", ha='center', va='center', 
                   fontsize=10, alpha=0.7)
            ax.text(0.5, 0.3, f"{progress:.1f}%", ha='center', va='center', 
                   fontsize=12, color=colors[i], fontweight='bold')
            
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.set_aspect('equal')
            ax.axis('off')
            ax.set_title(kpi.replace('_', ' ').title(), fontsize=14, fontweight='bold', pad=20)
        
        plt.suptitle('KPI Dashboard Overview', fontsize=20, fontweight='bold', y=0.95)
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/kpi_dashboard.png', dpi=300, bbox_inches='tight')
        plt.close()
        return f'{self.output_dir}/kpi_dashboard.png'
    
    def generate_all_visualizations(self):
        """Generate all visualizations and return file paths"""
        print("📊 Generating visualizations...")
        
        generated_files = []
        
        try:
            generated_files.append(self.create_market_size_chart())
            print("✅ Market size chart created")
        except Exception as e:
            print(f"❌ Error creating market size chart: {e}")
        
        try:
            generated_files.append(self.create_competitive_positioning_map())
            print("✅ Competitive positioning map created")
        except Exception as e:
            print(f"❌ Error creating competitive positioning map: {e}")
        
        try:
            generated_files.append(self.create_financial_projections_chart())
            print("✅ Financial projections chart created")
        except Exception as e:
            print(f"❌ Error creating financial projections chart: {e}")
        
        try:
            generated_files.append(self.create_customer_segmentation_chart())
            print("✅ Customer segmentation chart created")
        except Exception as e:
            print(f"❌ Error creating customer segmentation chart: {e}")
        
        try:
            generated_files.append(self.create_implementation_timeline())
            print("✅ Implementation timeline created")
        except Exception as e:
            print(f"❌ Error creating implementation timeline: {e}")
        
        try:
            generated_files.append(self.create_kpi_dashboard_mockup())
            print("✅ KPI dashboard mockup created")
        except Exception as e:
            print(f"❌ Error creating KPI dashboard: {e}")
        
        print(f"📊 Generated {len(generated_files)} visualizations in '{self.output_dir}' folder")
        return generated_files