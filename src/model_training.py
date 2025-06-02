from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def train_and_evaluate(df):
    X = df.drop(columns=['math_score', 'reading_score', 'writing_score'])
    y = df['math_score']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print("✅ Modèle entraîné")
    print(f"📉 MSE : {mse:.2f}")
    print(f"📊 R² : {r2:.2f}")
