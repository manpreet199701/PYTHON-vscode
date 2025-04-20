# Write a Python program using pandas to read a CSV file named data.csv and print 
# its first 5 rows.
import pandas as pd
import numpy as np
# Write a Python program using pandas to read a CSV file named data.csv and print
# its first 5 rows.
csv_path = "data.csv"
try:
	df = pd.read_csv(csv_path)
	# Removed redundant print statement to avoid potential errors.
except FileNotFoundError:
	print(f"Error: The file '{csv_path}' was not found.")
except pd.errors.EmptyDataError:
	print(f"Error: The file '{csv_path}' is empty.")
except Exception as e:
	print(f"An unexpected error occurred: {e}")
print(df.head())
# Write a Python program using pandas to read an Excel file named data.xlsx and
