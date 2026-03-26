import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Načtení dat
df = pd.read_csv("dataset.csv")

# Převod na čísla
cols = ["study_hours", "sleep_hours", "attendance", "previous_score", "coffee_cups", "final_score"]
for col in cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Odstranění chyb
df = df.dropna()
df = df.drop_duplicates()

# Vytvoření klasifikace
df["passed"] = (df["final_score"] >= 75).astype(int)

# Výběr vstupů a výstupu
X = df[["study_hours", "sleep_hours", "attendance", "coffee_cups"]]
y = df["passed"]

# Rozdělení dat
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predikce
predictions = model.predict(X_test)

# Přesnost
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# Pravděpodobnosti
proba = model.predict_proba(X_test)
print("Pravděpodobnosti:")
print(proba)

# Koeficienty
print("Koeficienty modelu:")
for col, coef in zip(X.columns, model.coef_[0]):
    print(f"{col}: {coef}")
