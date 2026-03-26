import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Načtení dat
df = pd.read_csv("dataset.csv")

# Převod na čísla
cols = ["study_hours", "sleep_hours", "attendance", "previous_score", "coffee_cups", "final_score"]
for col in cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Odstranění chyb
df = df.dropna()
df = df.drop_duplicates()

# Výběr vstupů a výstupu
X = df[["study_hours", "sleep_hours", "attendance", "coffee_cups", "previous_score"]]
y = df["final_score"]

# Rozdělení dat
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predikce
predictions = model.predict(X_test)

# Vyhodnocení
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

# Koeficienty
print("Koeficienty modelu:")
for col, coef in zip(X.columns, model.coef_):
    print(f"{col}: {coef}")

# Intercept
print("Intercept:", model.intercept_)
