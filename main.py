from src.preprocessing import load_and_clean_data
from src.feature_engineering import encode_features
from src.visualization import plot_distributions
from src.model_training import train_and_evaluate

def main():
    df = load_and_clean_data("StudentsPerformance.csv")
    df = encode_features(df)
    plot_distributions(df)
    train_and_evaluate(df)

if __name__ == "__main__":
    main()
