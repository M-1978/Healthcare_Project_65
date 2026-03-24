import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("healthcare_dataset.csv")

print("===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATA INFO =====")
print(df.info())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# ---------------------------
# DATA CLEANING
# ---------------------------

df.drop_duplicates(inplace=True)

# Optional (dataset already clean)
# df = df.ffill()

# Convert date column
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])

# ---------------------------
# EXPLORATORY DATA ANALYSIS
# ---------------------------

print("\n===== SUMMARY =====")
print(df.describe())

print("\n===== MOST COMMON MEDICAL CONDITION =====")
print(df['Medical Condition'].value_counts())

print("\n===== AVERAGE BILLING AMOUNT =====")
print(df['Billing Amount'].mean())

print("\n===== GENDER COUNT =====")
print(df['Gender'].value_counts())

# ---------------------------
# VISUALIZATIONS (SAVE AS IMAGES)
# ---------------------------

# 1. Gender Distribution
plt.figure()
sns.countplot(x='Gender', data=df)
plt.title("Gender Distribution")
plt.savefig("gender_distribution.png")

# 2. Age Distribution
plt.figure()
sns.histplot(df['Age'], bins=20)
plt.title("Age Distribution")
plt.savefig("age_distribution.png")

# 3. Medical Condition Distribution
plt.figure(figsize=(10,5))
sns.countplot(x='Medical Condition', data=df)
plt.xticks(rotation=45)
plt.title("Medical Condition Distribution")
plt.savefig("medical_condition.png")

# 4. Billing Amount Distribution
plt.figure()
sns.histplot(df['Billing Amount'], bins=20)
plt.title("Billing Amount Distribution")
plt.savefig("billing_distribution.png")

# 5. Insurance Provider Distribution
plt.figure(figsize=(10,5))
sns.countplot(x='Insurance Provider', data=df)
plt.xticks(rotation=45)
plt.title("Insurance Provider Distribution")
plt.savefig("insurance_provider.png")

print("\n===== ANALYSIS COMPLETE =====")
print("Graphs saved as image files ✅")