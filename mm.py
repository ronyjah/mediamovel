from selenium import webdriver
import csv
import time


def mediamovel(equity):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--no-sandbox')
	prefs = {"download.default_directory" : "/home/ronaldo/mercado"}
	chrome_options.add_experimental_option("prefs",prefs)
	driver = webdriver.Chrome('/home/ronaldo/mercado/chromedriver',chrome_options=chrome_options)
	driver.get("https://br.financas.yahoo.com/quote/"+equity+".SA/history?p="+equity+".SA")
	try:
		driver.find_element_by_xpath("//span[@class='Fl(end) Pos(r) T(-6px)']/a").click()
	except:
		time.sleep(1)
		#driver = webdriver.Chrome('/home/ronaldo/mercado/chromedriver',chrome_options=chrome_options)
		driver.find_element_by_xpath("//span[@class='Fl(end) Pos(r) T(-6px)']/a").click()

	time.sleep (1)
	l = [0] *20
	try:
		f =open("/home/ronaldo/mercado/"+equity+".SA.csv", "rb")
	except:
		time.sleep (1)
		driver.find_element_by_xpath("//span[@class='Fl(end) Pos(r) T(-6px)']/a").click()
		time.sleep (1)
		f =open("/home/ronaldo/mercado/"+equity+".SA.csv", "rb")
	cr = csv.reader(f, delimiter=',')
	a=0
	my_list = list(cr)
	driver.close()
	for row in my_list:
		#if i == 0:
		if a != 0:
			l.append(float(row[4]))
			l.pop(0)
		else:
			a=a+1
	mm = sum(l) / len(l)
	if (l[18] < mm) and (l[19]> mm):
		print("Cruzou...")
	print("Media movel "+equity+": {0} ultimo valor: {1}".format(mm,l[19]))
