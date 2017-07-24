from os import walk, environ
import os.path
import argparse
from datetime import datetime

import pandas as pd

def get_files(directory=None):
    docslist=[]
    if not directory:
        directory = "data/current"
    else:
        pass
    listings = walk(directory)
    for item in listings:
        if item[1]:
            continue
        else:
            pre_path = item[0]
            for file in item[2]:
                xlsx = os.path.join(pre_path, file)
                docslist.append(xlsx)
    return docslist

def make_frame(docslist):
    print("Creating a dataframe of DoD records")
    dodframe = pd.DataFrame()
    sheet_counter=0
    file_counter = 0

    for file in docslist:
        if file.endswith('xls') or file.endswith('xlsx'):
            print("Scraping data from {0}".format(file))
            xlsn = pd.ExcelFile(file)
            nsheets = xlsn.sheet_names

            for item in nsheets:
                dodframe = pd.concat([dodframe, xlsn.parse(item, index_col=None)])
                sheet_counter += 1
            file_counter += 1
        else:
            print("Skipping {0}".format(file))

    records = len(dodframe)
    states = sheet_counter
    files = file_counter

    print("Added {0} sheets for states and territories from {1} files to the dataframe".format(states, files))
    print("Total of {0} records in dataframe".format(records))
    return dodframe

def output_csv(dodframe, csv_name=None):
    if csv_name:
        pass
    else:
        today = str(datetime.now().date())
        csv_name = today + "-dod-snapshot.csv"
    dodframe.to_csv(csv_name, encoding="utf-8", index=False)
    print("Created {0} file in this directory.".format(csv_name))
    return


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Make a CSV out of the DoD's 1033 Excel spreadsheets")
    parser.add_argument('-d', dest='dir', help='directory with 1033 data files to combine')
    parser.add_argument('-o', dest='out', help='Name your output csv.')
    args = parser.parse_args()
    docslist = get_files(directory=args.dir)
    dodframe =  make_frame(docslist)
    output_csv(dodframe, csv_name=args.out)
