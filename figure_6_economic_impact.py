import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Ensure figures directory exists
output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'figures')
os.makedirs(output_dir, exist_ok=True)

# Data
domains = ['Writing', 'Programming', 'Analysis']
skill_levels = ['Low-skill', 'Mid-skill', 'High-skill']

# Productivity gains (%)
# Format: [Low, Mid, High]
writing_gains = [144, 41, 6]
programming_gains = [152, 43, 6]
analysis_gains = [148, 44, 7]

data = np.array([writing_gains, programming_gains, analysis_gains])

# Style
plt.style.use('seaborn-v0_8-paper')
sns.set_context("paper", font_scale=1.5)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']

fig, ax = plt.subplots(figsize=(12, 6))

# Bar configuration
x = np.arange(len(domains))
width = 0.25

# Colors (gradients: darker=low skill, lighter=high skill)
colors = ['#08306b', '#4292c6', '#c6dbef'] # Blues

# Plot bars
rects1 = ax.bar(x - width, data[:, 0], width, label='Low-skill', color=colors[0])
rects2 = ax.bar(x, data[:, 1], width, label='Mid-skill', color=colors[1])
rects3 = ax.bar(x + width, data[:, 2], width, label='High-skill', color=colors[2])

# Add labels
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}%',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=11, fontweight='bold')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

# Horizontal line at 0
ax.axhline(0, color='black', linewidth=1)

# Formatting
ax.set_ylabel('Productivity Gain (%)', fontsize=14)
ax.set_title('Asymmetric Productivity Gains Across Skill Levels', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(domains, fontsize=14)
ax.legend(fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Caption
caption = "Low-skill workers experience 150% average productivity gains compared to 6% for\nhigh-skill workers, demonstrating skill compression rather than amplification."
plt.figtext(0.5, -0.05, caption, wrap=True, horizontalalignment='center', fontsize=12, style='italic')

plt.tight_layout()

output_path = os.path.join(output_dir, 'figure_6_economic_impact.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Figure saved to {output_path}")
