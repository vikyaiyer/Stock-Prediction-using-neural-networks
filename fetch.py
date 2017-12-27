from alpha_vantage.timeseries import TimeSeries
#import matplotlib.pyplot as plt
import sys
import csv
outfile=None
api_key = '7DHY25ARREXBTLCG'

ts=TimeSeries(key = api_key,output_format='pandas')

with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    for row in readCSV:
        data, meta_data = ts.get_intraday(symbol=row[1],interval='1min', outputsize='compact')
        print(data)
        outfilename = 'data/file-{}.csv'.format(row[0])
        outfilenameRO = 'dataRO/fileRO-{}.csv'.format(row[0])
        data.to_csv(outfilename, sep=',')

        with open(outfilename, 'r') as infile, open(outfilenameRO, 'a', newline = '') as outfile:
            fieldnames = ['Date','open','close','high','low','volume']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in csv.DictReader(infile):
                writer.writerow(row)


            

