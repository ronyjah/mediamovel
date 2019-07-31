from selenium import webdriver
import csv
import time
equity = 'AZUL4'
valorCompra = 0.0
diretorio = '/home/ronaldo/mercado/'
margem = 0.15 # Margem de seguranca apos cruzar a media para evitar falsos rompimentos.
renda = 0.0
l = [0] *20
ldata = [0] *20 
#try:
f =open(diretorio+equity+".SA.csv", "rb")
#except:
#	time.sleep (1)
#	driver.find_element_by_xpath("//span[@class='Fl(end) Pos(r) T(-6px)']/a").click()
#	time.sleep (1)
#	f =open("/home/ronaldo/mercado/"+equity+".SA.csv", "rb")
cr = csv.reader(f, delimiter=',')
a=0
my_list = list(cr)
#driver.close()
for row in my_list:
	#if i == 0:
	if a != 0:

		l.append(float(row[4]))
		l.pop(0)
		ldata.append(row[0])
		ldata.pop(0)
	else:
		a=a+1
	mm = sum(l) / len(l)
	if l[0] != 0:
		#print('teste')
		if (l[18] < mm) and ((l[19])> (mm + margem)):
			print("Cruzou pra cima...")
			print('Cotacao Atual: {0}'.format(l[19]))
			print("Data: "+ldata[19])
			print("Media movel "+equity+": {0} Ultimo valor: {1}".format(mm,l[19]))
			if valorCompra == 0.0:
				print('Acao Comprada')
				valorCompra = l[19]
		if (l[18] > mm) and ((l[19]) < (mm - margem)):
			print("Cruzou pra baixo...")
			print("Media movel "+equity+": {0}. Ultimo valor: {1}".format(mm,l[19]))
			if valorCompra == 0:
				print('Sem acao para vender...')
			else:
				print('Data: '+ldata[19])
				print('cotacaoAtual: {}'.format(l[19]))
				renda = (l[19] - valorCompra) + renda
				valorCompra = 0.0
				print('renda: {0}'.format(renda))

print('renda final por acao: {0}'.format(renda))
print('Valor da acao na carteira: {0}'.format(valorCompra))
print('Este simulador, verifica a renda na compra e venda de uma acao')