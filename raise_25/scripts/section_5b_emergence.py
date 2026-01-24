
import matplotlib.pyplot as plt
import numpy as np
import os

def plot_emergent_capabilities():
    """
    Section 5 (Part B): Emergent Capabilities
    Visualizes phase transition/spike in capability.
    """

    model_scale_billions = [0.1, 1, 10, 50, 100, 175, 500]
    accuracy_3_digit_add = [1, 2, 3, 5, 10, 85, 95]
    
    plt.figure(figsize=(10, 6))
    
    # Line plot with markers
    plt.plot(model_scale_billions, accuracy_3_digit_add, marker='o', color='purple', linewidth=3, markersize=10)
    
    # Log scale X only
    plt.xscale('log')
    plt.ylim(0, 100)
    
    # Phase transition line
    plt.axvline(x=100, color='red', linestyle=':', linewidth=2, label='Phase Transition Threshold')
    
    # Labels
    plt.xlabel('Model Size (Billions of Parameters)', fontsize=12)
    plt.ylabel('Accuracy on 3-Digit Addition (%)', fontsize=12)
    plt.title('Emergence of Arithmetic Proficiency at Scale', fontsize=14, pad=20)
    plt.grid(True, which="both", ls="-", alpha=0.1)
    plt.legend()
    
    # Save
    output_path = os.path.join(os.path.dirname(__file__), '../figures/section_5b_emergence.png')
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    print(f"Generated ../figures/{os.path.basename(output_path)}")

if __name__ == "__main__":
    plot_emergent_capabilities()
