import os
import requests
import argparse
import pandas as pd

base_url = 'https://www.eia.gov/dnav/ng/hist_xls/RNGWHHD'
period_dict = {'daily':'d.xls', 'weekly':'w.xls', 'monthly':'m.xls'}


def get_raw_file(response, name):
    file_name = '{}_data.xls'.format(name)
    with open('./raw_files/'+file_name,'wb') as f:
        f.write(response.content)


def get_data(period):
    response = requests.get(base_url + period_dict[period])
    get_raw_file(response, period)


def process_data(period, path):
    #Obtaining .xls data files
    get_data(period)

    #CSV Table preparation
    file_name = './raw_files/{}_data.xls'.format(period)
    df = pd.read_excel(file_name, "Data 1")[2:] #droping non-data rows
    df.columns = ["Date", "Price"]
    df.Price = df.Price.astype('float16')
    df.Date = pd.to_datetime(df.Date)
    df.dropna(axis = 0, inplace= True)
    df.reset_index(inplace=True, drop=True)

    #Saving the csv file
    saving_name = "{}_data.csv".format(period)
    saving_path = os.path.join(path, saving_name)
    df.to_csv(saving_path, index = False)
    print("Data saved as csv in: ", saving_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Download and convert Henry Hub Natural Gas Spot Price')
    parser.add_argument('--period', type=str, required = True, 
            help="Define if data is reported daily, weekly or monthly")
    parser.add_argument('--path', type=str, required = True,
            help="Path where the csv file will be saved")
    args = parser.parse_args()
    
    #Validating arguments
    if args.period not in list(period_dict.keys()):
        raise argparse.ArgumentError(
            'Not valid period option selected')

    if not os.path.isdir(args.path):
        raise argparse.ArgumentTypeError(
            'Saving path is invalid')

    #Running the process
    process_data(args.period, args.path)