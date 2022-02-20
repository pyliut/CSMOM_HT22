from tracemalloc import start
import numpy as np 
import stockPortfolio as portfolio 
import pandas 

port = portfolio.stockPortfolio(['2003', '01'], 'base_strategy_1month')
#port.updatePortfolio('MSFT','Nothing',1)
all_returns = pandas.read_pickle('returnsDF4.pkl')
SNP500 = all_returns.columns


def find_current_winners(month):
    data = all_returns.loc[month]
    ranked = data.sort_values()
    winners = ranked[-11:-1]
    return dict(winners)

def do_strategy(no_months):
    date = str(port.time[0]+'-'+port.time[1])
    for i in range(0,no_months):
        buy_options = find_current_winners(date)

        current_balance = port.reportData()['Sum']

        #buy into the 10 top stocks equally 
        buy_balance = current_balance/10

        # sell all old stocks
        #print(port.report())
        port.sellAll()
        
        # buy new stocks (top 10 equally)
        for stock in buy_options:
            port.updatePortfolio(str(stock), 'Nothing', buy_balance)
        #print(port.report())
        port.moveTime()
        
        date = str(port.time[0]+'-'+port.time[1])



#print(port.portfolio)
do_strategy(180)
port.plotReturns()
#print(port.portfolio)
#print(find_current_winners('2000-01'))




