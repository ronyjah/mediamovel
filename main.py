from mm import *

empresas = list()
with open("/home/ronaldo/mercado/bancodadosz") as f:
	line = f.readline()
	while line:
		empresas.append(line.strip())
		line = f.readline()
for i in empresas:
	mediamovel(i)
