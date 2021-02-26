# "Henry Hub Natural Gas Spot Price"
## Description
Python script for obtain Gas Prices from US Energy Information Administration and convert it to a csv format.

## Running example  
First, create a python enviroment and install the basic libraries as described in requirements.txt

The following command will execute the python script and save the data from the source portal and save it as csv to a local path.
```
python download_data.py --period daily --path ./processed_files
```
The arguments are:  
1. period: STRING, defines granularity and options are "daily", "weekly", "monthly".  
2. path: STRING, valid path where the csv file will be saved.  

NOTE: The script save the the raw .xls file in a temporal folder called *raw_files* before processing.  
NOTE2: On monthly data option the default date format keeps day = 15 for each month as default.  

# Visualization
The linear visualization of the Daily dataset can be consulted in the index.html page.  

## Data package
The daily data package is available from this url:  
https://drive.google.com/drive/folders/11ozxVyRamfHO4_UfoVu6A5kT9US0wQf0?usp=sharing 