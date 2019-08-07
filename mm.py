import csv
import datetime
import pandas_datareader.data as pdr

def mediamovel(equity):
	if '.SA' not in equity:
		equity = equity + '.SA'
	end = datetime.datetime.today()
	start = datetime.datetime(end.year - 1, end.month, end.day)

	stock_history = pdr.get_data_yahoo(equity, start=start, end=end)
	stock_history.to_csv("{}.csv".format(equity))

	with open("{}.csv".format(equity)) as f:
		cr = csv.reader(f, delimiter=',')

		l = [0] *20
		a = 0
		my_list = list(cr)

		for row in my_list:
			#if i == 0:
			if a != 0:
				if (row[4]=='null'):
					print('Erro na leitura da cotacao')
					break
				l.append(float(row[4]))
				l.pop(0)
			else:
				a=a+1
		mm = sum(l) / len(l)
		if (l[18] < mm) and (l[19]> mm):
			print("Cruzou pra cima...")
		print("Media movel "+equity+": {0} ultimo valor: {1}".format(mm,l[19]))
