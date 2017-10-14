# Box

The file contains the code to upload csv files (comma seperated values) directly into a personal Box account and also the ability to transform the file from csv to html, csv to json, or csv to xml. The directory includes:

* boxupload.py - the main file for uploading and transforming files 
* mycsv - get data and splits csv into data without calling a package
* csv2html - .csv into .html (if no header, replaces it with alphabetical characters a,b,c....)
* csv2xml - .csv into .xml (if no header, replaces it with alphabetical characters a,b,c....)
* csv2json - .csv into .json (if no header, replaces it with alphabetical characters a,b,c....)

Further additions include:
- combining redundant code into one function
- translating back from xml, html, or json to csv
