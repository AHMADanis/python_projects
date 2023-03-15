import pandas as pd
import re
import openpyxl

# Load the .spt file into a list of lines
with open('data.spt', 'r') as f:
    lines = f.readlines()

# Define a regular expression to match the polygon coordinates and name
coord_pattern = r'\[([\d.-]+),([\d.-]+)\]'
name_pattern = r'(\w+)\('

# Initialize an empty list to store the polygon data
polygon_data = []

# Loop over the lines in the file and extract the polygon data
for line in lines:
    if 'cs::polygon(' in line:
        match_coords = re.findall(coord_pattern, line)
        match_name = re.search(name_pattern, line)
        if match_coords and match_name:
            coords = [(float(x), float(y)) for x, y in match_coords]
            x_list = [x for x, y in coords]
            y_list = [y for x, y in coords]
            polygon_data.append({'x': x_list, 'y': y_list})

# Loop over the polygon data and write to separate files
for i, data in enumerate(polygon_data):
    df = pd.DataFrame(data)
    filename = f'elm{i}.xlsx'
    df.to_excel(filename, index=False)

# Combine all the data into one DataFrame and write to a separate file
combined_df = pd.concat([pd.DataFrame(data) for data in polygon_data])
combined_df.to_excel('combined_output.xlsx', index=False)