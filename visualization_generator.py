import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
from matplotlib.patches import Circle
import re
import json
from typing import Dict, List, Any

class ProductAnalysisVisualizer:
    def __init__(self, output_dir="visualizations"):
        """Initialize the visualizer with output directory"""
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Set style for matplotlib
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
    
    def extract_market_data(self, market_research_text: str) -> Dict[str, Any]:
        """Extract market data from market research text"""
        try:
            # Look for market size mentions
            market_data = {
                'years': ['2024', '2025', '2026', '2027', '2028'],
                'tam': [100, 120, 145, 175, 210],  # Default values
                'sam': [25, 35, 50, 70, 95],
                'som': [5, 8, 15, 25, 40]
            }
            
            # Try to extract actual numbers from text
            tam_match = re.search(r'TAM[:\s]*\$?(\d+(?:\.\d+)?)\s*([MmBb]illion|[Mm]illion)', market_research_text)
            sam_match = re.search(r'SAM[:\s]*\$?(\d+(?:\.\d+)?)\s*([MmBb]illion|[Mm]illion)', market_research_text)
            
            if tam_match:
                tam_value = float(tam_match.group(1))
                unit = tam_match.group(2).lower()
                multiplier = 1000 if 'billion' in unit else 1
                base_tam = tam_value * multiplier
                
                # Generate growth projections
                growth_rate = 0.25  # 25% annual growth
                market_data['tam'] = [base_tam * (1 + growth_rate)**i for i in range(5)]
                market_data['sam'] = [tam * 0.25 for tam in market_data['tam']]
                market_data['som'] = [sam * 0.20 for sam in market_data['sam']]
            
            return market_data
            
        except Exception as e:
            print(f"Warning: Could not extract market data from text: {e}")
            return {
                'years': ['2024', '2025', '2026', '2027', '2028'],
                'tam': [100, 120, 145, 175, 210],
                'sam': [25, 35, 50, 70, 95],
                'som': [5, 8, 15, 25, 40]
            }
    
    def extract_competitor_data(self, competitive_analysis_text: str) -> Dict[str, Any]:
        """Extract competitor data from competitive analysis text"""
        try:
            competitors = {
                'Our Product': {'price': 50, 'features': 85, 'market_share': 0}
            }
            
            # Look for competitor mentions
            competitor_patterns = [
                r'(\w+(?:\s+\w+)*?):\s*.*?price[:\s]*\$?(\d+)',
                r'(\w+(?:\s+\w+)*?):\s*.*?features[:\s]*(\d+)',
                r'(\w+(?:\s+\w+)*?):\s*.*?market share[:\s]*(\d+)%'
            ]
            
            # Extract competitor names and basic info
            competitor_names = re.findall(r'competitor[:\s]*([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', competitive_analysis_text, re.IGNORECASE)
            
            # Add default competitor data
            default_competitors = [
                {'name': 'Competitor A', 'price': 80, 'features': 70, 'market_share': 25},
                {'name': 'Competitor B', 'price': 60, 'features': 60, 'market_share': 20},
                {'name': 'Competitor C', 'price': 40, 'features': 45, 'market_share': 15}
            ]
            
            for i, comp in enumerate(default_competitors):
                if i < len(competitor_names):
                    comp['name'] = competitor_names[i]
                competitors[comp['name']] = {
                    'price': comp['price'],
                    'features': comp['features'],
                    'market_share': comp['market_share']
                }
            
            return competitors
            
        except Exception as e:
            print(f"Warning: Could not extract competitor data: {e}")
            return {
                'Our Product': {'price': 50, 'features': 85, 'market_share': 0},
                'Competitor A': {'price': 80, 'features': 70, 'market_share': 25},
                'Competitor B': {'price': 60, 'features': 60, 'market_share': 20}
            }
    
    def extract_financial_data(self, financial_text: str) -> Dict[str, Any]:
        """Extract financial data from financial analysis text"""
        try:
            # Look for revenue and cost projections
            revenue_pattern = r'revenue[:\s]*\$?(\d+(?:,\d+)*)'
            cost_pattern = r'cost[:\s]*\$?(\d+(?:,\d+)*)'
            
            revenues = re.findall(revenue_pattern, financial_text, re.IGNORECASE)
            costs = re.findall(cost_pattern, financial_text, re.IGNORECASE)
            
            # Default monthly progression
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            
            if revenues:
                # Use first revenue number as base
                base_revenue = int(revenues[0].replace(',', ''))
                revenue = [base_revenue * (1 + 0.15)**i for i in range(12)]  # 15% monthly growth
            else:
                revenue = [10, 15, 25, 35, 50, 65, 80, 95, 110, 125, 140, 160]
            
            if costs:
                base_cost = int(costs[0].replace(',', ''))
                cost = [base_cost * (1 + 0.05)**i for i in range(12)]  # 5% monthly growth
            else:
                cost = [30, 28, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
            
            profit = [r - c for r, c in zip(revenue, cost)]
            
            return {
                'months': months,
                'revenue': revenue,
                'costs': cost,
                'profit': profit
            }
            
        except Exception as e:
            print(f"Warning: Could not extract financial data: {e}")
            return {
                'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                'revenue': [10, 15, 25, 35, 50, 65, 80, 95, 110, 125, 140, 160],
                'costs': [30, 28, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],
                'profit': [-20, -13, -10, -5, 5, 15, 25, 35, 45, 55, 65, 80]
            }
    
    def extract_customer_data(self, customer_text: str) -> Dict[str, Any]:
        """Extract customer segmentation data"""
        try:
            # Look for customer segments
            segments = {}
            segment_patterns = [
                r'(\w+(?:\s+\w+)*?):\s*(\d+)%',
                r'(\w+(?:\s+\w+)*?)\s*-\s*(\d+)%',
                r'(\d+)%\s*(\w+(?:\s+\w+)*?)'
            ]
            
            for pattern in segment_patterns:
                matches = re.findall(pattern, customer_text, re.IGNORECASE)
                for match in matches:
                    if len(match) == 2:
                        try:
                            if match[0].isdigit():
                                segments[match[1]] = int(match[0])
                            else:
                                segments[match[0]] = int(match[1])
                        except ValueError:
                            continue
            
            # Default segments if none found
            if not segments:
                segments = {
                    'Tech Enthusiasts': 25,
                    'Business Professionals': 35,
                    'Cost-Conscious Users': 20,
                    'Premium Seekers': 15,
                    'Early Adopters': 5
                }
            
            # Default demographics
            demographics = {
                'Age Groups': {'18-25': 20, '26-35': 40, '36-45': 25, '46-55': 10, '55+': 5},
                'Income Levels': {'<$50K': 15, '$50K-$75K': 30, '$75K-$100K': 35, '$100K+': 20}
            }
            
            return {
                'segments': segments,
                'demographics': demographics
            }
            
        except Exception as e:
            print(f"Warning: Could not extract customer data: {e}")
            return {
                'segments': {
                    'Tech Enthusiasts': 25,
                    'Business Professionals': 35,
                    'Cost-Conscious Users': 20,
                    'Premium Seekers': 15,
                    'Early Adopters': 5
                },
                'demographics': {
                    'Age Groups': {'18-25': 20, '26-35': 40, '36-45': 25, '46-55': 10, '55+': 5},
                    'Income Levels': {'<$50K': 15, '$50K-$75K': 30, '$75K-$100K': 35, '$100K+': 20}
                }
            }
    
    def extract_kpi_data(self, kpi_text: str) -> Dict[str, Any]:
        """Extract KPI data from KPI analysis text"""
        try:
            kpis = {}
            
            # Look for KPI mentions with values
            kpi_patterns = [
                r'revenue[:\s]*\$?(\d+(?:,\d+)*)',
                r'users?[:\s]*(\d+(?:,\d+)*)',
                r'conversion[:\s]*(\d+(?:\.\d+)?)%',
                r'retention[:\s]*(\d+(?:\.\d+)?)%',
                r'satisfaction[:\s]*(\d+(?:\.\d+)?)(?:/5)?',
                r'churn[:\s]*(\d+(?:\.\d+)?)%'
            ]
            
            # Extract values
            revenue_match = re.search(kpi_patterns[0], kpi_text, re.IGNORECASE)
            users_match = re.search(kpi_patterns[1], kpi_text, re.IGNORECASE)
            conversion_match = re.search(kpi_patterns[2], kpi_text, re.IGNORECASE)
            retention_match = re.search(kpi_patterns[3], kpi_text, re.IGNORECASE)
            satisfaction_match = re.search(kpi_patterns[4], kpi_text, re.IGNORECASE)
            churn_match = re.search(kpi_patterns[5], kpi_text, re.IGNORECASE)
            
            # Build KPI data with extracted or default values
            return {
                'revenue': {
                    'current': int(revenue_match.group(1).replace(',', '')) if revenue_match else 85000,
                    'target': int(revenue_match.group(1).replace(',', '')) * 1.2 if revenue_match else 100000,
                    'unit': '$'
                },
                'users': {
                    'current': int(users_match.group(1).replace(',', '')) if users_match else 2450,
                    'target': int(users_match.group(1).replace(',', '')) * 1.2 if users_match else 3000,
                    'unit': ''
                },
                'conversion': {
                    'current': float(conversion_match.group(1)) if conversion_match else 3.2,
                    'target': float(conversion_match.group(1)) * 1.25 if conversion_match else 4.0,
                    'unit': '%'
                },
                'retention': {
                    'current': float(retention_match.group(1)) if retention_match else 78,
                    'target': float(retention_match.group(1)) * 1.1 if retention_match else 85,
                    'unit': '%'
                },
                'satisfaction': {
                    'current': float(satisfaction_match.group(1)) if satisfaction_match else 4.2,
                    'target': min(float(satisfaction_match.group(1)) * 1.1, 5.0) if satisfaction_match else 4.5,
                    'unit': '/5'
                },
                'churn': {
                    'current': float(churn_match.group(1)) if churn_match else 8.5,
                    'target': float(churn_match.group(1)) * 0.7 if churn_match else 6.0,
                    'unit': '%'
                }
            }
            
        except Exception as e:
            print(f"Warning: Could not extract KPI data: {e}")
            return {
                'revenue': {'current': 85000, 'target': 100000, 'unit': '$'},
                'users': {'current': 2450, 'target': 3000, 'unit': ''},
                'conversion': {'current': 3.2, 'target': 4.0, 'unit': '%'},
                'retention': {'current': 78, 'target': 85, 'unit': '%'},
                'satisfaction': {'current': 4.2, 'target': 4.5, 'unit': '/5'},
                'churn': {'current': 8.5, 'target': 6.0, 'unit': '%'}
            }
    
    def create_market_size_chart(self, market_data=None):
        """Create market size and growth projection chart"""
        if market_data is None:
            market_data = {
                'years': ['2024', '2025', '2026', '2027', '2028'],
                'tam': [100, 120, 145, 175, 210],
                'sam': [25, 35, 50, 70, 95],
                'som': [5, 8, 15, 25, 40]
            }
        
        fig, ax = plt.subplots(figsize=(12, 8))
        
        x = np.arange(len(market_data['years']))
        width = 0.25
        
        bars1 = ax.bar(x - width, market_data['tam'], width, label='TAM (Total Addressable Market)', alpha=0.8)
        bars2 = ax.bar(x, market_data['sam'], width, label='SAM (Serviceable Addressable Market)', alpha=0.8)
        bars3 = ax.bar(x + width, market_data['som'], width, label='SOM (Serviceable Obtainable Market)', alpha=0.8)
        
        ax.set_xlabel('Year', fontsize=12)
        ax.set_ylabel('Market Size ($ Millions)', fontsize=12)
        ax.set_title('Market Size Analysis & Growth Projections', fontsize=16, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(market_data['years'])
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Add value labels on bars
        for bars in [bars1, bars2, bars3]:
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                       f'${height:.0f}M', ha='center', va='bottom', fontsize=10)
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/market_size_analysis.png', dpi=300, bbox_inches='tight')
        plt.close()
        return f'{self.output_dir}/market_size_analysis.png'
    
    def create_competitive_positioning_map(self, competitors_data=None):
        """Create competitive positioning map"""
        if competitors_data is None:
            competitors_data = {
                'Our Product': {'price': 50, 'features': 85, 'market_share': 0},
                'Competitor A': {'price': 80, 'features': 70, 'market_share': 25},
                'Competitor B': {'price': 60, 'features': 60, 'market_share': 20}
            }
        
        fig, ax = plt.subplots(figsize=(12, 10))
        
        for name, data in competitors_data.items():
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
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/competitive_positioning.png', dpi=300, bbox_inches='tight')
        plt.close()
        return f'{self.output_dir}/competitive_positioning.png'
    
    def create_financial_projections_chart(self, financial_data=None):
        """Create financial projections chart"""
        if financial_data is None:
            financial_data = {
                'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                'revenue': [10, 15, 25, 35, 50, 65, 80, 95, 110, 125, 140, 160],
                'costs': [30, 28, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],
                'profit': [-20, -13, -10, -5, 5, 15, 25, 35, 45, 55, 65, 80]
            }
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
        
        # Revenue and Costs
        ax1.plot(financial_data['months'], financial_data['revenue'], marker='o', linewidth=3, label='Revenue', color='green')
        ax1.plot(financial_data['months'], financial_data['costs'], marker='s', linewidth=3, label='Costs', color='red')
        ax1.fill_between(financial_data['months'], financial_data['revenue'], alpha=0.3, color='green')
        ax1.fill_between(financial_data['months'], financial_data['costs'], alpha=0.3, color='red')
        ax1.set_ylabel('Amount ($000)', fontsize=12)
        ax1.set_title('Revenue vs Costs Projection (Year 1)', fontsize=14, fontweight='bold')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Profit/Loss
        colors = ['green' if p >= 0 else 'red' for p in financial_data['profit']]
        bars = ax2.bar(financial_data['months'], financial_data['profit'], color=colors, alpha=0.7)
        ax2.axhline(y=0, color='black', linestyle='-', linewidth=1)
        ax2.set_ylabel('Profit/Loss ($000)', fontsize=12)
        ax2.set_xlabel('Month', fontsize=12)
        ax2.set_title('Monthly Profit/Loss Projection', fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height + (1 if height >= 0 else -3),
                    f'${height:.0f}K', ha='center', va='bottom' if height >= 0 else 'top', fontsize=9)
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/financial_projections.png', dpi=300, bbox_inches='tight')
        plt.close()
        return f'{self.output_dir}/financial_projections.png'
    
    def create_customer_segmentation_chart(self, customer_data=None):
        """Create customer segmentation pie chart and demographics"""
        if customer_data is None:
            customer_data = {
                'segments': {
                    'Tech Enthusiasts': 25,
                    'Business Professionals': 35,
                    'Cost-Conscious Users': 20,
                    'Premium Seekers': 15,
                    'Early Adopters': 5
                },
                'demographics': {
                    'Age Groups': {'18-25': 20, '26-35': 40, '36-45': 25, '46-55': 10, '55+': 5},
                    'Income Levels': {'<$50K': 15, '$50K-$75K': 30, '$75K-$100K': 35, '$100K+': 20}
                }
            }
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # Customer Segments Pie Chart
        colors = plt.cm.Set3(np.linspace(0, 1, len(customer_data['segments'])))
        wedges, texts, autotexts = ax1.pie(customer_data['segments'].values(), 
                                          labels=customer_data['segments'].keys(), 
                                          autopct='%1.1f%%',
                                          colors=colors, startangle=90, 
                                          explode=[0.05] * len(customer_data['segments']))
        ax1.set_title('Customer Segmentation', fontsize=14, fontweight='bold')
        
        # Age Groups
        ax2.bar(customer_data['demographics']['Age Groups'].keys(), 
               customer_data['demographics']['Age Groups'].values(), 
               color='skyblue', alpha=0.8)
        ax2.set_title('Target Demographics - Age Groups', fontsize=14, fontweight='bold')
        ax2.set_ylabel('Percentage (%)')
        ax2.tick_params(axis='x', rotation=45)
        
        # Income Levels
        ax3.bar(customer_data['demographics']['Income Levels'].keys(), 
               customer_data['demographics']['Income Levels'].values(),
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
    
    def create_kpi_dashboard_mockup(self, kpi_data=None):
        """Create KPI dashboard visualization"""
        if kpi_data is None:
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
            if kpi == 'churn':  # Lower is better for churn
                progress = max(0, min(100, (target / current) * 100)) if current > 0 else 0
            else:
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
            ax.text(0.5, 0.6, f"{current:,.0f}{unit}", ha='center', va='center', 
                   fontsize=16, fontweight='bold')
            ax.text(0.5, 0.4, f"Target: {target:,.0f}{unit}", ha='center', va='center', 
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
    
    def generate_all_visualizations(self, analysis_results: Dict[str, str]):
        """Generate all visualizations using actual analysis results"""
        print("📊 Generating visualizations with analysis data...")
        
        generated_files = []
        
        try:
            # Extract market data from market research
            market_data = self.extract_market_data(analysis_results.get('market_research', ''))
            generated_files.append(self.create_market_size_chart(market_data))
            print("✅ Market size chart created with analysis data")
        except Exception as e:
            print(f"❌ Error creating market size chart: {e}")
        
        try:
            # Extract competitor data from competitive analysis
            competitor_data = self.extract_competitor_data(analysis_results.get('competitive_analysis', ''))
            generated_files.append(self.create_competitive_positioning_map(competitor_data))
            print("✅ Competitive positioning map created with analysis data")
        except Exception as e:
            print(f"❌ Error creating competitive positioning map: {e}")
        
        try:
            # Extract financial data from financial projections
            financial_data = self.extract_financial_data(analysis_results.get('financial_projections', ''))
            generated_files.append(self.create_financial_projections_chart(financial_data))
            print("✅ Financial projections chart created with analysis data")
        except Exception as e:
            print(f"❌ Error creating financial projections chart: {e}")
        
        try:
            # Extract customer data from customer segmentation
            customer_data = self.extract_customer_data(analysis_results.get('customer_segmentation', ''))
            generated_files.append(self.create_customer_segmentation_chart(customer_data))
            print("✅ Customer segmentation chart created with analysis data")
        except Exception as e:
            print(f"❌ Error creating customer segmentation chart: {e}")
        
        try:
            # Extract KPI data from KPI analysis
            kpi_data = self.extract_kpi_data(analysis_results.get('kpi_definition', ''))
            generated_files.append(self.create_kpi_dashboard_mockup(kpi_data))
            print("✅ KPI dashboard created with analysis data")
        except Exception as e:
            print(f"❌ Error creating KPI dashboard: {e}")
        
        try:
            # Create SWOT analysis visualization
            swot_data = self.extract_swot_data(analysis_results.get('swot_analysis', ''))
            generated_files.append(self.create_swot_analysis_chart(swot_data))
            print("✅ SWOT analysis chart created with analysis data")
        except Exception as e:
            print(f"❌ Error creating SWOT analysis chart: {e}")
        
        try:
            # Create marketing strategy visualization
            marketing_data = self.extract_marketing_data(analysis_results.get('marketing_strategy', ''))
            generated_files.append(self.create_marketing_strategy_chart(marketing_data))
            print("✅ Marketing strategy chart created with analysis data")
        except Exception as e:
            print(f"❌ Error creating marketing strategy chart: {e}")
        
        try:
            # Create technical feasibility visualization
            tech_data = self.extract_tech_data(analysis_results.get('technical_feasibility', ''))
            generated_files.append(self.create_tech_feasibility_chart(tech_data))
            print("✅ Technical feasibility chart created with analysis data")
        except Exception as e:
            print(f"❌ Error creating technical feasibility chart: {e}")
        
        print(f"📊 Generated {len(generated_files)} visualizations total")
        return generated_files
    
    def extract_swot_data(self, swot_text: str) -> Dict[str, List[str]]:
        """Extract SWOT analysis data from text"""
        try:
            swot_data = {
                'strengths': [],
                'weaknesses': [],
                'opportunities': [],
                'threats': []
            }
            
            # Look for SWOT sections
            sections = ['strengths', 'weaknesses', 'opportunities', 'threats']
            
            for section in sections:
                # Find section in text
                pattern = rf'{section}[:\s]*\n?(.*?)(?=\n\n|\n[A-Z]|$)'
                match = re.search(pattern, swot_text, re.IGNORECASE | re.DOTALL)
                
                if match:
                    content = match.group(1).strip()
                    # Extract bullet points or numbered items
                    items = re.findall(r'[-•*\d+\.]\s*([^\n]+)', content)
                    if items:
                        swot_data[section] = items[:5]  # Limit to 5 items
                    else:
                        # Split by sentences if no bullet points
                        sentences = [s.strip() for s in content.split('.') if s.strip()]
                        swot_data[section] = sentences[:3]
            
            # Default values if nothing found
            if not any(swot_data.values()):
                swot_data = {
                    'strengths': ['Innovative product features', 'Strong technical team', 'Competitive pricing'],
                    'weaknesses': ['Limited market presence', 'New brand recognition', 'Resource constraints'],
                    'opportunities': ['Growing market demand', 'Digital transformation trend', 'Strategic partnerships'],
                    'threats': ['Established competitors', 'Economic uncertainty', 'Regulatory changes']
                }
            
            return swot_data
            
        except Exception as e:
            print(f"Warning: Could not extract SWOT data: {e}")
            return {
                'strengths': ['Innovative product features', 'Strong technical team', 'Competitive pricing'],
                'weaknesses': ['Limited market presence', 'New brand recognition', 'Resource constraints'],
                'opportunities': ['Growing market demand', 'Digital transformation trend', 'Strategic partnerships'],
                'threats': ['Established competitors', 'Economic uncertainty', 'Regulatory changes']
            }
    
    def extract_marketing_data(self, marketing_text: str) -> Dict[str, Any]:
        """Extract marketing strategy data from text"""
        try:
            # Extract budget allocation
            budget_pattern = r'(\w+(?:\s+\w+)*?):\s*\$?(\d+(?:,\d+)*)'
            budget_matches = re.findall(budget_pattern, marketing_text, re.IGNORECASE)
            
            channels = {}
            for match in budget_matches:
                channel = match[0].strip()
                amount = int(match[1].replace(',', ''))
                if 'digital' in channel.lower() or 'social' in channel.lower():
                    channels['Digital Marketing'] = amount
                elif 'content' in channel.lower() or 'blog' in channel.lower():
                    channels['Content Marketing'] = amount
                elif 'email' in channel.lower():
                    channels['Email Marketing'] = amount
                elif 'paid' in channel.lower() or 'ads' in channel.lower():
                    channels['Paid Advertising'] = amount
                elif 'seo' in channel.lower() or 'search' in channel.lower():
                    channels['SEO/SEM'] = amount
            
            # Default channels if none found
            if not channels:
                channels = {
                    'Digital Marketing': 40000,
                    'Content Marketing': 25000,
                    'Email Marketing': 15000,
                    'Paid Advertising': 35000,
                    'SEO/SEM': 20000,
                    'Events & PR': 15000
                }
            
            # Extract campaign timeline
            timeline = {
                'Pre-Launch': ['Market research', 'Content creation', 'Website development'],
                'Launch': ['PR campaign', 'Social media blitz', 'Email announcement'],
                'Post-Launch': ['User feedback', 'Content optimization', 'Retention campaigns']
            }
            
            return {
                'budget_allocation': channels,
                'campaign_timeline': timeline
            }
            
        except Exception as e:
            print(f"Warning: Could not extract marketing data: {e}")
            return {
                'budget_allocation': {
                    'Digital Marketing': 40000,
                    'Content Marketing': 25000,
                    'Email Marketing': 15000,
                    'Paid Advertising': 35000,
                    'SEO/SEM': 20000,
                    'Events & PR': 15000
                },
                'campaign_timeline': {
                    'Pre-Launch': ['Market research', 'Content creation', 'Website development'],
                    'Launch': ['PR campaign', 'Social media blitz', 'Email announcement'],
                    'Post-Launch': ['User feedback', 'Content optimization', 'Retention campaigns']
                }
            }
    
    def extract_tech_data(self, tech_text: str) -> Dict[str, Any]:
        """Extract technical feasibility data from text"""
        try:
            # Extract complexity ratings
            complexity_pattern = r'(\w+(?:\s+\w+)*?):\s*(\d+(?:\.\d+)?)'
            complexity_matches = re.findall(complexity_pattern, tech_text, re.IGNORECASE)
            
            tech_components = {}
            for match in complexity_matches:
                component = match[0].strip()
                score = float(match[1])
                if 'frontend' in component.lower() or 'ui' in component.lower():
                    tech_components['Frontend/UI'] = score
                elif 'backend' in component.lower() or 'server' in component.lower():
                    tech_components['Backend/Server'] = score
                elif 'database' in component.lower() or 'db' in component.lower():
                    tech_components['Database'] = score
                elif 'api' in component.lower():
                    tech_components['API Integration'] = score
                elif 'security' in component.lower():
                    tech_components['Security'] = score
                elif 'scalability' in component.lower():
                    tech_components['Scalability'] = score
            
            # Default components if none found
            if not tech_components:
                tech_components = {
                    'Frontend/UI': 7.5,
                    'Backend/Server': 8.0,
                    'Database': 6.5,
                    'API Integration': 7.0,
                    'Security': 8.5,
                    'Scalability': 7.8,
                    'DevOps/Deployment': 7.2
                }
            
            # Extract development timeline
            timeline = {
                'Phase 1': ['Requirements gathering', 'System design', 'Architecture planning'],
                'Phase 2': ['Frontend development', 'Backend development', 'Database setup'],
                'Phase 3': ['Integration testing', 'Security implementation', 'Performance optimization'],
                'Phase 4': ['User testing', 'Bug fixes', 'Deployment']
            }
            
            return {
                'complexity_scores': tech_components,
                'development_timeline': timeline
            }
            
        except Exception as e:
            print(f"Warning: Could not extract technical data: {e}")
            return {
                'complexity_scores': {
                    'Frontend/UI': 7.5,
                    'Backend/Server': 8.0,
                    'Database': 6.5,
                    'API Integration': 7.0,
                    'Security': 8.5,
                    'Scalability': 7.8,
                    'DevOps/Deployment': 7.2
                },
                'development_timeline': {
                    'Phase 1': ['Requirements gathering', 'System design', 'Architecture planning'],
                    'Phase 2': ['Frontend development', 'Backend development', 'Database setup'],
                    'Phase 3': ['Integration testing', 'Security implementation', 'Performance optimization'],
                    'Phase 4': ['User testing', 'Bug fixes', 'Deployment']
                }
            }
    
    def create_swot_analysis_chart(self, swot_data=None):
        """Create SWOT analysis visualization"""
        if swot_data is None:
            swot_data = {
                'strengths': ['Innovative features', 'Strong team', 'Competitive pricing'],
                'weaknesses': ['Limited presence', 'New brand', 'Resource constraints'],
                'opportunities': ['Growing market', 'Digital trend', 'Partnerships'],
                'threats': ['Competitors', 'Economic uncertainty', 'Regulations']
            }
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # Define colors for each quadrant
        colors = {
            'strengths': '#2E8B57',  # Sea Green
            'weaknesses': '#DC143C',  # Crimson
            'opportunities': '#4682B4',  # Steel Blue
            'threats': '#FF8C00'  # Dark Orange
        }
        
        axes = [ax1, ax2, ax3, ax4]
        quadrants = ['strengths', 'opportunities', 'weaknesses', 'threats']
        titles = ['Strengths', 'Opportunities', 'Weaknesses', 'Threats']
        
        for i, (ax, quadrant, title) in enumerate(zip(axes, quadrants, titles)):
            # Create a simple bar chart for each quadrant
            items = swot_data[quadrant][:5]  # Limit to 5 items
            y_pos = np.arange(len(items))
            
            # Create horizontal bars
            bars = ax.barh(y_pos, [1] * len(items), color=colors[quadrant], alpha=0.7)
            
            # Add text labels
            for j, (bar, item) in enumerate(zip(bars, items)):
                ax.text(0.5, bar.get_y() + bar.get_height()/2, 
                       item[:50] + '...' if len(item) > 50 else item, 
                       ha='center', va='center', fontsize=10, fontweight='bold', color='white')
            
            ax.set_xlim(0, 1)
            ax.set_yticks([])
            ax.set_xticks([])
            ax.set_title(title, fontsize=14, fontweight='bold', color=colors[quadrant])
            
            # Add borders
            for spine in ax.spines.values():
                spine.set_edgecolor(colors[quadrant])
                spine.set_linewidth(3)
        
        plt.suptitle('SWOT Analysis Matrix', fontsize=20, fontweight='bold')
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/swot_analysis.png', dpi=300, bbox_inches='tight')
        plt.close()
        return f'{self.output_dir}/swot_analysis.png'
    
    def create_marketing_strategy_chart(self, marketing_data=None):
        """Create marketing strategy visualization"""
        if marketing_data is None:
            marketing_data = {
                'budget_allocation': {
                    'Digital Marketing': 40000,
                    'Content Marketing': 25000,
                    'Email Marketing': 15000,
                    'Paid Advertising': 35000,
                    'SEO/SEM': 20000,
                    'Events & PR': 15000
                },
                'campaign_timeline': {
                    'Pre-Launch': ['Market research', 'Content creation', 'Website development'],
                    'Launch': ['PR campaign', 'Social media blitz', 'Email announcement'],
                    'Post-Launch': ['User feedback', 'Content optimization', 'Retention campaigns']
                }
            }
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
        
        # Budget allocation pie chart
        channels = list(marketing_data['budget_allocation'].keys())
        budgets = list(marketing_data['budget_allocation'].values())
        colors = plt.cm.Set3(np.linspace(0, 1, len(channels)))
        
        wedges, texts, autotexts = ax1.pie(budgets, labels=channels, autopct='%1.1f%%',
                                          colors=colors, startangle=90, 
                                          explode=[0.02] * len(channels))
        ax1.set_title('Marketing Budget Allocation', fontsize=14, fontweight='bold')
        
        # Campaign timeline
        timeline = marketing_data['campaign_timeline']
        phases = list(timeline.keys())
        y_positions = np.arange(len(phases))
        
        # Create timeline bars
        bars = ax2.barh(y_positions, [3, 2, 4], color=['#FF6B6B', '#4ECDC4', '#45B7D1'], alpha=0.7)
        
        # Add phase labels and activities
        for i, (phase, activities) in enumerate(timeline.items()):
            ax2.text(0.1, i, phase, fontweight='bold', fontsize=12, va='center')
            activity_text = ' • '.join(activities[:3])  # Show first 3 activities
            ax2.text(0.1, i - 0.2, activity_text, fontsize=9, va='center', alpha=0.8)
        
        ax2.set_yticks(y_positions)
        ax2.set_yticklabels(phases)
        ax2.set_xlabel('Timeline (Months)', fontsize=12)
        ax2.set_title('Marketing Campaign Timeline', fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/marketing_strategy.png', dpi=300, bbox_inches='tight')
        plt.close()
        return f'{self.output_dir}/marketing_strategy.png'
    
    def create_tech_feasibility_chart(self, tech_data=None):
        """Create technical feasibility visualization"""
        if tech_data is None:
            tech_data = {
                'complexity_scores': {
                    'Frontend/UI': 7.5,
                    'Backend/Server': 8.0,
                    'Database': 6.5,
                    'API Integration': 7.0,
                    'Security': 8.5,
                    'Scalability': 7.8,
                    'DevOps/Deployment': 7.2
                },
                'development_timeline': {
                    'Phase 1': ['Requirements gathering', 'System design', 'Architecture planning'],
                    'Phase 2': ['Frontend development', 'Backend development', 'Database setup'],
                    'Phase 3': ['Integration testing', 'Security implementation', 'Performance optimization'],
                    'Phase 4': ['User testing', 'Bug fixes', 'Deployment']
                }
            }
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
        
        # Complexity scores radar chart
        components = list(tech_data['complexity_scores'].keys())
        scores = list(tech_data['complexity_scores'].values())
        
        # Create radar chart
        angles = np.linspace(0, 2 * np.pi, len(components), endpoint=False).tolist()
        scores += scores[:1]  # Complete the circle
        angles += angles[:1]
        
        ax1.plot(angles, scores, 'o-', linewidth=2, color='#FF6B6B')
        ax1.fill(angles, scores, alpha=0.25, color='#FF6B6B')
        ax1.set_xticks(angles[:-1])
        ax1.set_xticklabels(components, fontsize=10)
        ax1.set_ylim(0, 10)
        ax1.set_yticks([2, 4, 6, 8, 10])
        ax1.set_title('Technical Complexity Assessment', fontsize=14, fontweight='bold')
        ax1.grid(True)
        
        # Development timeline Gantt chart
        timeline = tech_data['development_timeline']
        phases = list(timeline.keys())
        y_pos = np.arange(len(phases))
        
        # Create timeline bars with different colors
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
        start_times = [0, 2, 4, 6]
        durations = [2, 2, 2, 2]
        
        for i, (phase, start, duration) in enumerate(zip(phases, start_times, durations)):
            ax2.barh(i, duration, left=start, color=colors[i], alpha=0.7, height=0.6)
            ax2.text(start + duration/2, i, phase, ha='center', va='center', 
                    fontweight='bold', fontsize=10)
        
        ax2.set_yticks(y_pos)
        ax2.set_yticklabels(phases)
        ax2.set_xlabel('Development Time (Months)', fontsize=12)
        ax2.set_title('Development Timeline', fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/tech_feasibility.png', dpi=300, bbox_inches='tight')
        plt.close()
        return f'{self.output_dir}/tech_feasibility.png'