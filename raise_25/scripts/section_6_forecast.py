
import matplotlib.pyplot as plt
import numpy as np
import os

def plot_forecasting():
    """
    Section 6: Forecasting Capabilities (The Cone of Uncertainty)
    """
    years = [2022, 2023, 2024, 2025, 2026, 2027, 2028]
    
    # Historical (2022-2024)
    hist_years = [2022, 2023, 2024]
    hist_score = [70, 86, 90]
    
    # Projections (from 2024 onwards)
    fut_years = [2024, 2025, 2026, 2027, 2028]
    
    # Aggressive: Reaching 99% by 2026
    agg_score = [90, 96, 99, 99.9, 100]
    
    # Linear: Reaching 95% by 2028
    lin_score = [90, 92, 93, 94, 95]
    
    # Stagnation: Plateauing at 92%
    stag_score = [90, 91, 91.5, 92, 92]
    
    plt.figure(figsize=(10, 6))
    
    # Historical
    plt.plot(hist_years, hist_score, color='black', linewidth=3, label='Historical Data (GPT-4 Era)')
    
    # Projections
    plt.plot(fut_years, agg_score, color='green', linestyle='--', label='Aggressive (AGI Scenario)')
    plt.plot(fut_years, lin_score, color='blue', linestyle='--', label='Linear Growth')
    plt.plot(fut_years, stag_score, color='red', linestyle='--', label='Stagnation')
    
    # Cone of uncertainty
    plt.fill_between(fut_years, stag_score, agg_score, color='gray', alpha=0.2, label='Cone of Uncertainty')
    
    plt.ylim(60, 100)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Benchmark Accuracy (MMLU %)', fontsize=12)
    plt.title('Forecasted General Reasoning Capabilities (MMLU Benchmark)', fontsize=14, pad=20)
    plt.grid(True, alpha=0.3)
    plt.legend(loc='lower right')
    
    # Save
    output_path = os.path.join(os.path.dirname(__file__), '../figures/section_6_forecast.png')
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    print(f"Generated ../figures/{os.path.basename(output_path)}")

if __name__ == "__main__":
    plot_forecasting()
