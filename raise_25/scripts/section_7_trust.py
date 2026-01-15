
import matplotlib.pyplot as plt
import numpy as np
import os

def plot_trust_mismatch():
    """
    Section 7: Cognitive Science (Trust vs. Performance)
    Dual Axis plot.
    """
    model_gens = range(7) # 0 to 6
    ai_accuracy = [50, 60, 70, 80, 90, 95, 99]
    human_verification = [100, 95, 80, 60, 30, 10, 0]
    
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # Left Axis: Accuracy
    color = 'tab:blue'
    ax1.set_xlabel('Model Generation (Time)', fontsize=12)
    ax1.set_ylabel('Model Accuracy (%)', color=color, fontsize=12)
    ax1.plot(model_gens, ai_accuracy, color=color, linewidth=3, marker='o', label='Model Capability')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylim(0, 105)
    
    # Right Axis: Verification
    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Human Verification Rate (%)', color=color, fontsize=12)
    ax2.plot(model_gens, human_verification, color=color, linewidth=3, linestyle='--', marker='x', label='Human Oversight')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim(0, 105)
    
    # Highlight Danger Zone
    plt.axvspan(5, 6, color='yellow', alpha=0.3)
    plt.text(5.1, 50, "DANGER ZONE\nHigh Capability\nZero Oversight", fontsize=10, fontweight='bold', color='darkred')
    
    plt.title('The Paradox of Automation: Inverse Relationship Between Capability and Oversight', fontsize=14, pad=20)
    fig.tight_layout()
    
    # Save
    output_path = os.path.join(os.path.dirname(__file__), '../figures/section_7_trust.png')
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    print(f"Generated ../figures/{os.path.basename(output_path)}")

if __name__ == "__main__":
    plot_trust_mismatch()
