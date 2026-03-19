import pandas as pd

df = pd.read_csv(
    r"C:\Users\cbran\Projects\TelecomChurnProject\data\telecom_customer_churn.csv"
)

print("Raw data loaded successfully!")
print("Shape:", df.shape)
print()

print("Missing values:")
print(df.isnull().sum()[df.isnull().sum() > 0])
print()

print("Negative monthly charges:", (df["Monthly Charge"] < 0).sum())
print()


# Customers with no churn reason simply never churned
df["Churn Reason"] = df["Churn Reason"].fillna("Not Churned")
df["Churn Category"] = df["Churn Category"].fillna("Not Churned")

# Customers with no internet type have no internet service
df["Internet Type"] = df["Internet Type"].fillna("No Internet")

# Customers with no offer were not on any promotion
df["Offer"] = df["Offer"].fillna("No Offer")

# Customers with no multiple lines have no phone service
df["Multiple Lines"] = df["Multiple Lines"].fillna("No Phone Service")

# Internet-related columns — fill with No for customers without internet
internet_columns = [
    "Online Security",
    "Online Backup",
    "Device Protection Plan",
    "Premium Tech Support",
    "Streaming TV",
    "Streaming Movies",
    "Streaming Music",
    "Unlimited Data",
    "Avg Monthly GB Download",
]

for col in internet_columns:
    df[col] = df[col].fillna("No Internet Service")

# Fill missing long distance charges with 0
df["Avg Monthly Long Distance Charges"] = df[
    "Avg Monthly Long Distance Charges"
].fillna(0)

print("Missing values fixed!")
print()

before = len(df)
df = df[df["Monthly Charge"] >= 0]
after = len(df)

print(f"Removed {before - after} rows with negative monthly charges")
print()

remaining_missing = df.isnull().sum()[df.isnull().sum() > 0]

if len(remaining_missing) == 0:
    print("All missing values fixed!")
else:
    print("Remaining missing values:")
    print(remaining_missing)

print("Remaining negative charges:", (df["Monthly Charge"] < 0).sum())
print()

df.to_csv(
    r"C:\Users\cbran\Projects\TelecomChurnProject\output\telecom_clean.csv", index=False
)

print("Clean file saved successfully!")
print("Final shape:", df.shape)
