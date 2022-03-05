# -*- coding: utf-8 -*-
"""CSMOM_MLModels.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18sdN1UQraA_rgjXJrEY4Xkh6w2lgs4hz
"""

import pandas as pd
import sys
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor

yrStep = 5
minReq = 20
def predictTo(model, ticker, ind1, ind2):
  X = featureDic[ticker]
  y = returnDic[ticker]
  X_train = X[X.index <= ind1].set_index("month")
  y_train = y[y.index <= ind1].set_index("month")
  X_test = X[(X.index <= ind2) & (X.index > ind1)].set_index("month")
  y_test = y[(y.index <= ind2) & (y.index > ind1)].set_index("month")
  model.fit(X_train, y_train)
  return model.predict(X_test)
def getPreds(model, ticker, pred):
  X = featureDic[ticker]
  y = returnDic[ticker]
  if len(X) < minReq:
    return
  firstDate = X["month"][minReq-2]
  lastDate = X["month"][len(X["month"])-1]
  year = int(firstDate[0:4])
  month = firstDate[5:7]
  monthCol = list(X["month"])
  index
  while index:
    date1 = str(year)+"-"+month
    date2 = str(year+yrStep)+"-"+month
    if compare(date2, lastDate) >= 0:
      date2 = lastDate
      endOfData = True
    pred["pred"] += [float(x[0]) for x in list(predictTo(model, ticker, date1, date2))]
    year += yrStep
  mnthList = list(X["month"][X["month"].index > minReq-2])
  pred["TICKER"] += [ticker]*len(mnthList)
  pred["month"] += mnthList
def compare(date1, date2): #returns 1 if date 1 is after date 2, -1 if date 2 after date 1, 0 otherwise
  #dates are of the form YYYY-MM
  year1 = int(date1[0:4])
  year2 = int(date2[0:4])
  month1 = int(date1[5:7])
  month2 = int(date2[5:7])
  if year1 > year2:
    return 1
  elif year1 < year2:
    return -1
  elif month1 > month2:
    return 1
  elif month1 < month2:
    return -1
  else:
    return 0
df_NN = pd.read_csv("df_NeuralNetworkFeatures.csv")
df_NN = df_NN[["TICKER","month","pred_target","debt_assets","de_ratio","evm","pe_exi","roe","npm","ps","ptb","pcf","aftret_invcapx","CPI","FedFundsTargetRate","GDP","MedianHomeSalesPrice","NonFarmPayrolls","PMI","PPI","PrivateHousingStarts","Unemployment","MEDPTG","PCTUP4W","PCTDOWN4W","volume"]]#,"price_adjusted"]]
tickers = df_NN["TICKER"].squeeze().unique()
featureDic = {tk:df_NN[df_NN.TICKER == tk].reset_index().drop(["TICKER", "pred_target", "index"],1) for tk in tickers}
returnDic = {tk:df_NN[df_NN.TICKER == tk][["pred_target", "month"]].reset_index().drop(["index"],1) for tk in tickers}
pred = {"TICKER":[], "month":[],"pred":[]} 
for tk in tickers:
  getPreds(LinearRegression(), tk, pred)
df_Ret = pd.DataFrame(data = pred).set_index("month")
predictionDic = {tk:df_Ret[df_Ret.TICKER == tk].drop(["TICKER"],1) for tk in tickers}
for tk in tickers:
  returnDic[tk].set_index("month")
predictionDic[tickers[0]].plot()
returnDic[tickers[0]].plot()




