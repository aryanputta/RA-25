import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Ensure figures directory exists
output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'figures')
os.makedirs(output_dir, exist_ok=True)

# Data
accuracy = [70, 75, 80, 85, 90, 92, 94, 96, 98, 99]
verification_rate = [85, 72, 62, 48, 35, 25, 16, 9, 4, 2]

# Style
plt.style.use('seaborn-v0_8-paper')
sns.set_context("paper", font_scale=1.5)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']

fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Verification Rate (Left Y-axis)
color = 'tab:blue'
ax1.set_xlabel('Model Accuracy (%)', fontsize=14)
ax1.set_ylabel('Human Verification Rate (%)', color=color, fontsize=14)
ax1.plot(accuracy, verification_rate, color=color, linewidth=3, marker='o', label='Verification Rate')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(0, 100)

# Create second y-axis
ax2 = ax1.twinx()  
color = 'tab:gray'
ax2.set_ylabel('Model Accuracy (Reference)', color=color, fontsize=14)
# Plot accuracy as diagonal reference line (dashed)? 
# Actually, x-axis is already accuracy. Ploting y=x reference line.
ax2.plot([70, 100], [70, 100], color=color, linestyle='--', alpha=0.5, label='Reference (x=y)')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(70, 100)

# Title
plt.title('The Trust Paradox: Model Accuracy vs. Human Verification Rates', fontsize=16, fontweight='bold', pad=20)

# Danger Zone Shading (Accuracy > 95%, Verification < 10%)
ax1.axvspan(95, 100, color='red', alpha=0.2, label='Danger Zone')
ax1.text(97.5, 50, 'Danger Zone\n(Complacency)', ha='center', color='darkred', fontweight='bold')

# Grid
ax1.grid(True, linestyle=':', alpha=0.6)

# Caption
caption = "As model accuracy reaches 99%, human verification drops to near 0%, creating maximum\nvulnerability through automation complacency at peak reliability."
plt.figtext(0.5, -0.05, caption, wrap=True, horizontalalignment='center', fontsize=12, style='italic')

plt.tight_layout()

output_path = os.path.join(output_dir, 'figure_5_trust_paradox.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Figure saved to {output_path}")
