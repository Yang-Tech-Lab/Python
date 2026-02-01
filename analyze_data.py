import pandas as pd

print("1. Reading Excel file...")
# Load the dataset
df = pd.read_excel('fiverr_sales.xlsx')

# 2. Calculate revenue per order
# Renaming columns to English for better compatibility
df['Total_Sales'] = df['Unit_Price'] * df['Quantity']

# 3. Calculate total revenue (for internal tracking)
total_revenue = df['Total_Sales'].sum()
print(f"💰 Total revenue today: ${total_revenue}")

print("4. Generating client report...")

# 5. Export the processed data to a new Excel file
# Setting index=False to exclude row numbers for a cleaner client-facing document
df.to_excel('fiverr_report_finished.xlsx', index=False)

print("✅ Success! [fiverr_report_finished.xlsx] has been saved to your directory.")
