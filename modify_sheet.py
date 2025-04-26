import pandas as pd

# Load the Excel file
input_file = "C:\projects\Crystalgrowth\Hot graphite materials CO.xlsx"  # Replace with your file path
output_file = "C:\projects\Crystalgrowth\Hot graphite materials CO time corrected.xlsx"  # Output file path
import os


excel_data = pd.read_excel(input_file, sheet_name=None)  # Load all sheets into a dictionary

# Process each sheet
for sheet_name, df in excel_data.items():
    # Ensure the DataFrame has at least 2 columns
    if len(df.columns) > 1:
        # Modify the first row values starting from the second column
        df.iloc[0, 1:28] = list(range(0, 27))  # Overwrite the first row
        
        # Remove columns after the 27th
        df = df.iloc[:, :27]
        
        # Update the dictionary with the modified DataFrame
        excel_data[sheet_name] = df

# Save the formatted data back to a new Excel file
with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
    for sheet_name, df in excel_data.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Formatted Excel file saved as '{output_file}'.")


for