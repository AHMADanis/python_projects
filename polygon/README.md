## Python Code Converting Polygon Data from .spt to .xlsx

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This Python code takes a .spt file as input, extracts the polygon data from it, and converts it into separate .xlsx files, with each file containing the x and y coordinates of a polygon. The code also combines all the data into one DataFrame and writes it to a separate file.

## Libraries Used
The following libraries are used in this code:

- pandas: used to create DataFrames from the extracted polygon data and write it to .xlsx files.
- re: used to extract the polygon data from the .spt file using regular expressions.
- os: used to check if the output directory exists, and if not, create it.

## How to Execute the Code
- Make sure you have Python 3.x installed on your computer.
- Install the necessary libraries by running the following command in your command prompt or terminal:

```
pip install pandas openpyxl
```

- Download the polygon_converter.py file and place it in a directory of your choice.
- Place your input .spt file in the same directory as polygon_converter.py.
- Open a command prompt or terminal in the directory where polygon_converter.py and your input .spt file are located.
- Run the following command:


```
python polygon_converter.py
```

- The converted .xlsx files will be created in a new directory called output in the same directory as polygon_converter.py.

## Process
- The code first reads the contents of the input .spt file into a list of strings.
- It then uses regular expressions to extract the polygon data from each line in the list.
- The polygon data is stored in a list of dictionaries, where each dictionary contains the name, x-coordinates, and y-coordinates of a polygon.
- The code then loops over the list of dictionaries and writes each polygon's data to a separate .xlsx file in the output directory.
- Finally, the code creates a DataFrame containing all the polygon data and writes it to a separate .xlsx file in the output directory.

Note: If the output directory already exists, the code will overwrite any files with the same names as the output files. If the directory does not exist, the code will create it.


