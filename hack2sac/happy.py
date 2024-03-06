import pandas as pd
import mysql.connector

# Connect to your MySQL database
# Replace 'your_host', 'your_user', 'your_password', and 'your_database' with your actual database credentials
connection = mysql.connector.connect(
    host='your_host',
    user='your_user',
    password='your_password',
    database='your_database'
)

# Read data from MySQL into a DataFrame
query = "SELECT * FROM your_table"  # Replace 'your_table' with the actual table name
df = pd.read_sql(query, connection)

# Close the database connection
connection.close()

# Step 1: Add the first withdrawal and closing balance
initial_withdrawal = df.loc[0, 'Withdrawal Amt.']
initial_closing_balance = df.loc[0, 'Closing Balance']

# Step 2: Add the total withdrawal amount
total_withdrawal = df['Withdrawal Amt.'].sum()

# Step 3: Add the total deposit amount
total_deposit = df['Deposit Amt.'].sum()

# Step 4: Calculate the final amount
final_amount = (initial_closing_balance + total_deposit) - total_withdrawal

# Display the results
print(f"Step 1: Initial Withdrawal and Closing Balance - Withdrawal: {initial_withdrawal}, Closing Balance: {initial_closing_balance}")
print(f"Step 2: Total Withdrawal Amount: {total_withdrawal}")
print(f"Step 3: Total Deposit Amount: {total_deposit}")
print(f"Step 4: Final Amount: {final_amount}")
