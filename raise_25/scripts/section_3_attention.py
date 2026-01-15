
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Set clean style
sns.set_theme(style="white")

def plot_attention_heatmap():
    """
    Section 3: Technical Foundations (How LLMs Work)
    Visualizes Attention weights.
    """
    sentence = "The animal didn't cross the street because it was too tired"
    words = sentence.split()
    
    # 10x10 Matrix (padding the sentence to 10 words or using the first 10 tokens)
    # The sentence has 10 words exactly!
    
    # Create hypothetical attention scores
    # Default low attention
    attention_matrix = np.random.uniform(0.0, 0.2, size=(10, 10))
    
    # "it" (index 7) attends to "animal" (index 1)
    # 'it' is at index 6 in 0-indexed split ['The', 'animal', 'didn't', 'cross', 'the', 'street', 'because', 'it', 'was', 'too', 'tired'] -> wait, that's 11 words.
    # The prompt says: "The animal didn't cross the street because it was too tired."
    # Let's count: 1:The 2:animal 3:didn't 4:cross 5:the 6:street 7:because 8:it 9:was 10:too (11:tired)
    # Prompt asks for 10x10. I will truncate or adjust. Let's strictly follow "Create a 10x10 numpy array".
    # I will stick to the first 10 words or just label axes with the words.
    
    words = ['The', 'animal', 'didn\'t', 'cross', 'the', 'street', 'because', 'it', 'was', 'too'] # 10 words
    
    # Matrix Row 7 (index 7 corresponds to 'it')
    # Connect to 'animal' (index 1) with 0.9
    attention_matrix[7, 1] = 0.9 
    
    # Low score connecting to 'street' (index 5)
    attention_matrix[7, 5] = 0.05

    plt.figure(figsize=(10, 8))
    
    ax = sns.heatmap(attention_matrix, annot=True, fmt=".2f", cmap="Blues",
                     xticklabels=words, yticklabels=words)
    
    plt.title('Self-Attention Distribution: Resolution of Pronoun Ambiguity', fontsize=16, pad=20)
    plt.xlabel('Key (Source Token)', fontsize=12)
    plt.ylabel('Query (Target Token)', fontsize=12)
    
    # Save
    output_path = os.path.join(os.path.dirname(__file__), '../figures/section_3_attention.png')
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    print(f"Generated ../figures/{os.path.basename(output_path)}")

if __name__ == "__main__":
    plot_attention_heatmap()
