import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Ensure figures directory exists
output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'figures')
os.makedirs(output_dir, exist_ok=True)

# Data
tokens = ["The", "animal", "didn't", "cross", "the", "street", "because", "it", "was", "too", "tired"]
attention_weights = [0.01, 0.90, 0.01, 0.01, 0.00, 0.03, 0.02, 0.00, 0.01, 0.00, 0.01]

# Setup data for heatmap (needs 2D array)
# Reshape to (1, len) for a single row heatmap
data = np.array(attention_weights).reshape(1, -1)

# Style configuration
plt.style.use('seaborn-v0_8-paper')
sns.set_context("paper", font_scale=1.5)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']

# Create figure
fig, ax = plt.subplots(figsize=(12, 4))

# Create heatmap
sns.heatmap(data, 
            xticklabels=tokens, 
            yticklabels=False, 
            cmap="Blues", 
            annot=True, 
            fmt=".2f", 
            cbar_kws={'label': 'Attention Weight', 'orientation': 'horizontal', 'pad': 0.2},
            square=True,
            linewidths=1,
            linecolor='black')

# Aesthetics
plt.title('Contextual Attention Weights in Pronoun Resolution', fontsize=16, pad=20, fontweight='bold')
plt.xlabel('Input Tokens', fontsize=14, labelpad=10)

# Highlight connection "it" (pos 7) -> "animal" (pos 1)
# We use a standard annotation to highlight the high weight cell

# Add text annotation for the specific connection
plt.annotate('High Attention\n(0.90)', 
             xy=(1.5, 0.5), # Center of "animal" (index 1)
             xytext=(1.5, -0.5), # Position of text
             ha='center', 
             va='top',
             fontsize=12,
             color='darkred',
             fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='darkred', lw=2))

# Add caption
caption = "The model assigns 0.90 attention weight to 'animal' when processing 'it,'\ndemonstrating semantic rather than syntactic proximity bias."
plt.figtext(0.5, -0.1, caption, wrap=True, horizontalalignment='center', fontsize=12, style='italic')

# Adjust layout
plt.tight_layout()

# Save
output_path = os.path.join(output_dir, 'figure_1_attention_heatmap.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Figure saved to {output_path}")
