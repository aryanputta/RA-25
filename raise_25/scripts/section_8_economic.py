
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Set style
sns.set_theme(style="whitegrid")

def plot_economic_impact():
    """
    Section 8: Societal Implications (Economic Impact)
    Skill Leveling Effect.
    """
    # structured data for seaborn
    data = [
        {'Group': 'Low-Skill Workers', 'Condition': 'No AI', 'Performance': 3.0},
        {'Group': 'Low-Skill Workers', 'Condition': 'With AI', 'Performance': 7.5},
        {'Group': 'High-Skill Workers', 'Condition': 'No AI', 'Performance': 8.0},
        {'Group': 'High-Skill Workers', 'Condition': 'With AI', 'Performance': 8.5}
    ]
    df = pd.DataFrame(data)
    
    plt.figure(figsize=(10, 6))
    
    # Bar Chart
    ax = sns.barplot(data=df, x='Group', y='Performance', hue='Condition', palette=['gray', 'green'])
    
    # Calculate improvements
    # Low Skill: (7.5 - 3.0) / 3.0 = 1.5 (150%)
    # High Skill: (8.5 - 8.0) / 8.0 = 0.0625 (6.25%)
    
    # Annotate bars
    for p in ax.patches:
        height = p.get_height()
        # Find which bar this is to annotate nicely
        # But specifically we want to show the % improvement gap
        pass

    # Manually adding text for improvement
    plt.text(-0.2, 7.8, "+150% Increase", fontsize=12, color='green', fontweight='bold', ha='center')
    plt.text(0.2, 8.8, "+6% Increase", fontsize=12, color='green', fontweight='bold', ha='center') # Tweaked position

    plt.ylim(0, 10)
    plt.ylabel('Performance Score (0-10)', fontsize=12)
    plt.xlabel('Worker Skill Baseline', fontsize=12)
    plt.title('The Redistributive Impact of LLMs on Worker Performance', fontsize=14, pad=20)
    
    # Save
    output_path = os.path.join(os.path.dirname(__file__), '../figures/section_8_economic.png')
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    print(f"Generated ../figures/{os.path.basename(output_path)}")

if __name__ == "__main__":
    plot_economic_impact()
