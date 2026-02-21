import pandas as pd
import joblib
from scipy.io import arff
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load ARFF dataset
data, meta = arff.loadarff("training dataset.arff")

# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Convert byte columns to string (important fix)
for col in df.columns:
    if df[col].dtype == object:
        df[col] = df[col].apply(lambda x: x.decode("utf-8"))

# Convert class column to numeric
df['Result'] = df['Result'].astype(int)

# Features and label
X = df.drop("Result", axis=1)
y = df["Result"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# Save model
joblib.dump(model, "phishing_model.pkl")

print("Model saved as phishing_model.pkl")