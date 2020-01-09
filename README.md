# Scramble-csv-data

A small python program for scrambling confidential information in user-specified columns in a csv-file. 
The code will need to be adjusted for your own use, and the code-file contains some comments intended to make the adjustment easier.
In this version the csv-file must only contain the data and no headings. But this can easily be change by removing "header=None" from pandas read_csv.
You can either name your csv file "data.csv" and be locate it in the same folder as the python-file, or change the file-path in pandas read_csv. 
The program saves a file named "n_data.csv" in the folder containing the python file.

Prerequisites:
 - python 2.7* or 3.*
 - pandas
 - numpy
 


