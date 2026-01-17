import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Ensure figures directory exists
output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'figures')
os.makedirs(output_dir, exist_ok=True)

# Data
params = [1, 3, 10, 30, 50, 70, 90, 95, 100, 105, 110, 130, 150, 175]
accuracy = [2, 3, 4, 3, 5, 4, 8, 28, 67, 82, 84, 85, 85, 85]

# Style
plt.style.use('seaborn-v0_8-paper')
sns.set_context("paper", font_scale=1.5)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']

fig, ax = plt.subplots(figsize=(10, 6))

# Plot line
ax.plot(params, accuracy, marker='o', color='navy', linewidth=2.5, label='Arithmetic Accuracy')

# Vertical line at 100B
ax.axvline(x=100, color='red', linestyle='--', linewidth=2, label='Emergence Threshold (100B)')

# Shaded region 90-110B
ax.axvspan(90, 110, alpha=0.2, color='gray', label='Transition Window')

# Formatting
ax.set_xlabel('Model Size (Billions of Parameters)', fontsize=14)
ax.set_ylabel('Arithmetic Accuracy (%)', fontsize=14)
ax.set_title('Phase Transition in Arithmetic Reasoning Capability', fontsize=16, fontweight='bold', pad=20)
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_ylim(0, 100)

# Annotate jump
plt.annotate('Sudden Emergence', 
             xy=(100, 67), 
             xytext=(60, 80),
             ha='center', 
             fontsize=12,
             fontweight='bold',
             arrowprops=dict(facecolor='black', shrink=0.05))

ax.legend(fontsize=12, loc='upper left')

# Caption
caption = "Arithmetic reasoning accuracy exhibits a sharp phase transition at 100B parameters,\njumping from near-zero to 85% over a narrow 20B parameter window."
plt.figtext(0.5, -0.05, caption, wrap=True, horizontalalignment='center', fontsize=12, style='italic')

plt.tight_layout()

output_path = os.path.join(output_dir, 'figure_3_phase_transition.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Figure saved to {output_path}")
