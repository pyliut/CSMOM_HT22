import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


class stockPortfolio:
    returns = pd.read_pickle('returnsDF4.pkl') #dataframe
    def __init__(self,startTime, portfolioName): 
        standardDF = pd.read_pickle('portfolio.pkl') #Note: Is a Dictionary
        self.portfolio = pd.DataFrame(standardDF,index = [stockPortfolio.currentTime(startTime)]) # dataframe
        self.name = portfolioName
        self.time = startTime
        self.currentDF = standardDF # Dictionary

    def report(self):
        s = 'Date: '+stockPortfolio.currentTime(self.time)+ '\n'+self.name + ' contains:\n'
        for i in self.currentDF:
            if self.currentDF[i] != 0 and i !='Sum':
                s+=(i +': '+str(self.currentDF[i])+'\n')
        s+='Total Value is ' + str(self.currentDF['Sum'])
        return s

    def reportData(self):
        arr = {}
        for i in self.currentDF:
            if self.currentDF[i] !=0:
                arr[i]=self.currentDF[i]
        return arr
    
    def sellAll(self):
        holder = stockPortfolio.reportData(self)
        for i in holder.keys():
            if i != 'Sum' and i != 'Nothing':
                self.currentDF['Nothing']+=holder[i]
                self.currentDF[i] = 0


    def historicalReport(self,date):
        dic = self.portfolio.loc[stockPortfolio.currentTime(date)].to_dict()
        s = 'Date: '+stockPortfolio.currentTime(date)+ '\n'+self.name + ' contains:\n'
        for i in dic:
            if dic[i] != 0 and i !='Sum':
                s+=(i +': '+str(dic[i])+'\n')
        s+='Total Value is ' + str(dic['Sum'])
        return s
    def plotReturns(self):
        plt.rc('font', size=6)
        plt.xticks(rotation=45)
        arr = self.portfolio.loc[:,'Sum'].to_numpy()
        dates = self.portfolio.index
        plt.plot(dates,arr,label = self.name)
        plt.xticks(np.arange(0, len(dates)+1, 10))
        plt.legend(loc = 'upper left')
        plt.show()
    def currentTime(arr):
        return str(arr[0]+'-'+arr[1])

    def moveTime(self):
        if(self.time[1]=='12'):
            self.time = [str(int(self.time[0])+1),'01']
        elif(self.time[1]=='11' or self.time[1]=='10' or self.time[1]=='09'):
            self.time = [self.time[0],str(int(self.time[1])+1)]
        else:
            self.time = [self.time[0],'0'+str(int(self.time[1])+1)]
        holderDF = self.currentDF
        arr = np.multiply(np.array(list(holderDF.values())),(np.append(np.array([1,1]),(stockPortfolio.returns.loc[stockPortfolio.currentTime(self.time)].to_numpy()))))
        self.portfolio = self.portfolio.append(pd.DataFrame(arr,index = self.portfolio.columns,columns = [stockPortfolio.currentTime(self.time)]).transpose())
        self.portfolio.at[stockPortfolio.currentTime(self.time),'Sum'] = sum(arr)-arr[1]
        self.currentDF = self.portfolio.loc[stockPortfolio.currentTime(self.time)].to_dict()
    def updatePortfolio(self, buyTicker, sellTicker, amount): #done
        self.currentDF[buyTicker] += amount
        self.currentDF[sellTicker] -= amount
    def compareReturns(self, p2):
        plt.rc('font', size=6)
        plt.xticks(rotation=45)
        arr = self.portfolio.loc[:,'Sum'].to_numpy()
        arr2 = p2.portfolio.loc[:,'Sum'].to_numpy()
        dates1 = self.portfolio.index
        dates2 = p2.portfolio.index
        plt.plot(dates1,arr, label = self.name)
        plt.plot(dates2,arr2, label = p2.name)
        plt.xticks(np.arange(0, len(dates1)+1, 10))
        plt.legend(loc = 'upper left')
        plt.show()





