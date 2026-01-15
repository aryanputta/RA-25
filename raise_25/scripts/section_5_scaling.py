
import matplotlib.pyplot as plt
import numpy as np
import os

def plot_scaling_laws():
    """
    Section 5: Empirical Scaling Laws
    Power Law relationship between Compute and Loss.
    """
    # Data from prompt
    compute_flops = [1e19, 1e20, 1e21, 1e22, 1e23, 1e24, 1e25]
    loss = [4.0, 3.4, 2.9, 2.5, 2.1, 1.8, 1.5]
    
    plt.figure(figsize=(10, 6))
    
    # Log-log scatter plot
    plt.scatter(compute_flops, loss, color='blue', s=100, zorder=5)
    
    # Fit power law line (Linear in Log-Log space)
    log_compute = np.log10(compute_flops)
    log_loss = np.log10(loss)
    
    # Polyfit degree 1
    slope, intercept = np.polyfit(log_compute, log_loss, 1)
    
    # Generate line points
    fit_x = np.array([min(compute_flops), max(compute_flops)])
    fit_y = 10**(slope * np.log10(fit_x) + intercept)
    
    plt.plot(fit_x, fit_y, color='black', linestyle='--', linewidth=2, label='Power Law Fit')
    
    # Annotate last point
    plt.annotate('Frontier Model (2024)', 
                 (compute_flops[-1], loss[-1]),
                 textcoords="offset points", 
                 xytext=(-100, -20), 
                 ha='center',
                 arrowprops=dict(arrowstyle="->", color='black'))

    plt.xscale('log')
    plt.yscale('log')
    
    plt.xlabel('Compute (FLOPs)', fontsize=12)
    plt.ylabel('Cross-Entropy Loss', fontsize=12)
    plt.title('Empirical Scaling Laws: The Power-Law Relationship Between Compute and Performance', fontsize=14, pad=20)
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.legend()
    
    # Save
    output_path = os.path.join(os.path.dirname(__file__), '../figures/section_5_scaling.png')
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    print(f"Generated ../figures/{os.path.basename(output_path)}")

if __name__ == "__main__":
    plot_scaling_laws()
