import pandas as pd

# load dataset
df = pd.read_csv("data/student-mat.csv", sep=';')


print(df.shape)      # rows & columns
print(df.columns)    # column names
print(df.head())     # first 5 rows


from sklearn.model_selection import train_test_split

# Select input features and target
X = df[['studytime', 'absences', 'G1', 'G2']]
y = df['G3']

print("Features:")
print(X.head())

print("\nTarget:")
print(y.head())


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining set size:", X_train.shape)
print("Testing set size:", X_test.shape)


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("Mean Squared Error:", mse)
print("R2 Score:", r2)


# Predict for a new student
# Example: studytime=2, absences=3, G1=12, G2=13
new_student = [[2, 3, 12, 13]]
predicted_score = model.predict(new_student)

print("\nPredicted Final Grade (G3):", predicted_score[0])
