import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Ensure figures directory exists
output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'figures')
os.makedirs(output_dir, exist_ok=True)

# Data
hist_years = [2020, 2021, 2022, 2023, 2024]
hist_mmlu = [35, 48, 62, 75, 82]

proj_years = [2024, 2025, 2026, 2027, 2028, 2029, 2030] # Start from 2024 to connect lines
# 2024 value is 82, matching historical
proj_aggressive = [82, 87, 91, 95, 97, 98, 98]
proj_moderate = [82, 85, 87, 89, 91, 93, 94]
proj_conservative = [82, 83, 75, 75, 76, 76, 77]

# Style
plt.style.use('seaborn-v0_8-paper')
sns.set_context("paper", font_scale=1.5)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']

fig, ax = plt.subplots(figsize=(10, 6))

# Historical data
ax.plot(hist_years, hist_mmlu, color='black', marker='o', linewidth=2.5, label='Historical')

# Projections with cones
ax.plot(proj_years, proj_aggressive, color='green', linestyle='--', linewidth=2, label='Aggressive Scenario')
ax.plot(proj_years, proj_moderate, color='blue', linestyle='--', linewidth=2, label='Moderate Scenario')
ax.plot(proj_years, proj_conservative, color='firebrick', linestyle='--', linewidth=2, label='Conservative Scenario')

# Shade the cone
ax.fill_between(proj_years, proj_conservative, proj_aggressive, color='gray', alpha=0.15, label='Forecast Uncertainty')

# Vertical line at 2024
ax.axvline(x=2024, color='black', linestyle=':', linewidth=1.5)
ax.text(2023.8, 40, 'Present (2024)', rotation=90, va='bottom')

# Formatting
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('MMLU Accuracy (%)', fontsize=14)
ax.set_title('MMLU Benchmark Performance Projections Through 2030', fontsize=16, fontweight='bold', pad=20)
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_ylim(0, 105)
ax.set_xlim(2019.5, 2030.5)

ax.legend(fontsize=12, loc='lower right')

# Caption
caption = "Three forecasting scenarios show benchmark saturation possible by 2027 (Aggressive)\nor plateau by 2026 (Conservative). Widening cone reflects compounding uncertainties."
plt.figtext(0.5, -0.05, caption, wrap=True, horizontalalignment='center', fontsize=12, style='italic')

plt.tight_layout()

output_path = os.path.join(output_dir, 'figure_4_forecasting_cone.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Figure saved to {output_path}")
