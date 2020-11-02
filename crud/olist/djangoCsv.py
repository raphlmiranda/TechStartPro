import os
import requests
import pandas as pd
import json
from olist.models import Category
import csv



class djangoCsv():

    def __init__(self):
        self.dir = '.\\files\\'
        self.csvName = os.listdir(self.dir)

    def getCsvName(self) -> str:
        '''
        Get from 'files' path name CSV
        '''
        files = self.csvName[0].split('.csv')
        return files[0]
    
    def deleteFile(self) -> None:
        '''
        Delete CSV file after read
        '''
        if os.path.exists(f'{self.dir}{self.getCsvName()}.csv'):
            os.remove(f'{self.dir}{self.getCsvName()}.csv')


    def readCsv(self) -> None:
        '''
        Read CSV File in 'files' path
        '''
        df = pd.read_csv(f'{self.dir}{self.getCsvName()}.csv')
        # print(df.columns)
        for i in range(len(df)):
            c = Category(name=df['nome'][i])
            c.save() # Insert in DB

        self.deleteFile()
        