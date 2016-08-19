'''
# 2016. 08. 19
'''
import pandas as pd
from pandas.tools.plotting import scatter_matrix
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime

def main():
    DnloadStockData(
            "samsung.data", "005930", 2015, 1, 1, 2015, 12, 31)
    df = loadStockData("samsung.data")
    n, bins, patched = plt.hist(df["Open"])
    plt.axvline(df["Open"].mean(), color="green")
    # plt.show()

    print("       히스토그램          ")
    for index in range(len(n)):
        print("Bin : " + str(bins[index]) + " frequency : " + str(n[index]) )

    print("        산점도 행렬         ")
    scatter_matrix(
        df[["Open", "High", "Low", "Close"]], alpha=0.2, figsize=(6,6),
        diagonal='kde')
    # plt.show()
    
    print("        상자 그림         ")
    df[["Open", "High", "Low", "Close"]].plot(kind="box")
    plt.show()



def DnloadStockData(filename, companyCode, year1, month1, date1, 
                                           year2, month2, date2):
    start = datetime.datetime(year1, month1, date1)
    end = datetime.datetime(year2, month2, date2)
    df = web.DataReader(str(companyCode) + ".KS", "yahoo", start, end)

    df.to_pickle(filename)
    return df

def loadStockData(filename):
    df = pd.read_pickle(filename)
    print(df.describe())
    print(df.quantile([.25, .5, .75]))
    return df

if __name__ == '__main__':
    main()