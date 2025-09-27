import pandas as pd
from io import StringIO

"""
Activity: Load data, clean it, and do quick analysis
"""

# -----------------------------
# Load data
# -----------------------------
csv_data = """Name,Course,Grade,Marks
Sam,Math,B,13
James,Science,A,16
Shaz,Statistics,B,17
Mary,SocialStudies,A,35
,English,A,25
"""
onEvent("id", "click", function( ) {
  setScreen(aiistorice);
});
df = pd.read_csv(StringIO(csv_data))
print("Raw data:\n", df, "\n")

# -----------------------------
# Clean data
# -----------------------------
# Fill missing values
df["Name"] = df["Name"].fillna("Unknown")       # Replace missing names
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())  # Replace missing marks with average
df["Grade"] = df["Grade"].fillna("Pending")     # Replace missing grades

print("Cleaned data:\n", df, "\n")

# Remove duplicates
df = df.drop_duplicates()

# -----------------------------
# Sample Analysis
# -----------------------------
print("Mean of Marks:", df["Marks"].mean())

print("\nStudents in Math:\n", df[df["Course"] == "Math"])

# regression analysis diabetic patients
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

#1 load data set
diabetes = load_diabetes()
#2 linear two varaibles X,Y
X=diabetes.data[:,[2]] # BMI calculation
y=diabetes.target # disease progression

#3 Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#4 Train linear regression
model=LinearRegression()
model.fit(X_train, y_train)
#5 predictions
y_pred=model.predict(X_test)

#6 evaluation
print("This is mean  sqaured error :",mean_squared_error(y_test,y_pred))
print(f"Regression Equation: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}")
#7 Showing it  Visualizing it
plt.scatter(X_test,y_test,color='blue', label="actual")
plt.scatter(X_test,y_pred,color='blue', label="prediction")
plt.xlabel("BMI")
plt.ylabel("Disease progression")
plt.title("Linear regression on diabetes")
plt.legend()
plt.show()

print("\nStudent Count by Course:\n", df["Course"].value_counts())

print("\nCourse with Highest Avg Marks:\n", df.groupby("Course")["Marks"].mean().idxmax())
