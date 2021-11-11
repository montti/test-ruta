from datetime import date
from dateutil.relativedelta import relativedelta

# Utilizo relativedelta pues datetime no tiene la capacidad de expresar diferencias
# de fecha en años, solo días. 

class Stock():
	def __init__(self, ticker):
		self.ticker = ticker # QQQ, FTEC, etc.
		self.listPrices = {}

	def updateStock(self, price, date):
		self.listPrices.update({date.today(): price})

	def price(self, date):
		return self.listPrices.get(date)

class Portfolio():
	def __init__(self):
		self.stocks = {}

	def addStocks(self, stock):
		self.stocks[stock.ticker] = stock

	def profit(self, dateA, dateB):
		precioInicial = 0
		precioFinal = 0

		for ticker, stock in self.stocks.items():
			precioInicial += stock.price(dateA)
			precioFinal += stock.price(dateB) 

		return (precioFinal - precioInicial) / precioInicial

	def annualizedReturn(self, dateA, dateB):
		if (abs(relativedelta(dateA, dateB).years) > 0):
			
			# Annual Return = (Simple Return + 1) ^ (1 / Years Held)-1
			return (self.profit(dateA, dateB) ** (1/abs(relativedelta(dateA, dateB).years))) - 1




			