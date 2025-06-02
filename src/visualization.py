import seaborn as sns
import matplotlib.pyplot as plt

def plot_distributions(df):
    plt.figure(figsize=(8,5))
    sns.histplot(df['math_score'], kde=True)
    plt.title("Distribution du score en mathématiques")
    plt.xlabel("Score")
    plt.ylabel("Fréquence")
    plt.tight_layout()
    plt.show()
