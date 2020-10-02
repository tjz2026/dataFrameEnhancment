from pandas import DataFrame
import pandas as pd
import numpy as np

class DataFrameEnhanced(DataFrame):
    def __init__(self,df):
        DataFrame.__init__(self, df)
        self.colIndxDict = dict(zip(self.columns.values,np.arange(len(self.columns))))
        print('col dict',self.colIndxDict)
        self.rawData = df.values
    def __getitem__(self, item):
        if len(item) ==2:
            slice_ = item[0]
            colName = item[1]
            print(type(slice_))
            print(type(colName))
            if type(slice_) == slice and type(colName) == str:
                print('hello, I am here')
                colIndx =  self.colIndxDict[colName]
                return self.iloc[slice_,colIndx]
        return super(DataFrameEnhanced,self).__getitem__(item)

    def __setitem__(self, item, value):
        if len(item) ==2:
            slice_ = item[0]
            colName = item[1]
            if type(slice_) == slice and type(colName) == str:
                colIndx =  self.colIndxDict[colName]
                self.iloc[slice_, colIndx] = value
                return
        super(DataFrameEnhanced,self).__setitem__(item,value)
        return

if __name__ == "__main__":
    rawData = np.zeros((4,3))
    df =   DataFrame(rawData, index= np.arange(rawData.shape[0]) , columns= ['A','B','C'])
    data = DataFrameEnhanced(df)
    # test enhanced features
    print(data[0:2,'A'])
    data[0:2,'A'] = 22
    print(data[0:2,'A'])
    # test dataframe features
    print(data.head(3))
    print(len(data))
    print(data.columns)
    print(data['A'])
