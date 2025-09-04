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

print("\nStudent Count by Course:\n", df["Course"].value_counts())

print("\nCourse with Highest Avg Marks:\n", df.groupby("Course")["Marks"].mean().idxmax())
