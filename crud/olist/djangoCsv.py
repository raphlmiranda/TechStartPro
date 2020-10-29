import os
import requests
import pandas as pd
import json
from olist.models import Category
import csv



class djangoCsv():

    def __init__(self):
        self.csvName = os.listdir('.\\files\\')

    def getCsvName(self):
        '''
        Get from 'files' path name CSV
        '''
        files = self.csvName[0].split('.csv')
        return files[0]
    
    def deleteFile(self):
        '''
        Delete CSV file after read
        '''
        if os.path.exists(f'.\\files\\{self.getCsvName()}.csv'):
            os.remove(f'.\\files\\{self.getCsvName()}.csv')


    def readCsv(self):
        '''
        Read CSV File in 'files' path
        '''
        df = pd.read_csv(f'.\\files\\{self.getCsvName()}.csv')
        # print(df.columns)
        for i in range(len(df)):
            c = Category(name=df['nome'][i])
            c.save() # Insert in DB

        self.deleteFile()
        