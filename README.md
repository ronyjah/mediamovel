Desenvolvimento de software para mm



1) Para usar o simulador.py baixe o histórico da ação atualizada no site do yahoo finanças. Há duas alternativas:
	1.1) manualmente: https://br.financas.yahoo.com/quote/BBDC3.SA/history?p=BBDC3.SA
	1.2) executar o programa: main.py que irá baixar automaticamente as ações listadas no arquivo "bancodadosz". Se o foço for apenas simular, defina apenas poucas ações no "bancodadosz" para baixar pois quanto mais ações mais demorado fica.

2) edite o arquivo simulador.py e altere os parâmetros:
	equity = 'AZUL4'
	diretorio = '/home/ronaldo/mercado/'


Resumo:

o software utiliza a técnica de Média Móvel no período de 20 dias com a margem de segurança de 0.15 centavos. A margem serve para evitar falsos rompimentos da MM.

Baixa todas as ações listadas no arquivo "bancodadosz"

pre-requisitos:
	selenium

executar:
	python main.py
