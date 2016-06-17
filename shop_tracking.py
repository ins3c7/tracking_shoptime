#!/usr/bin/env python
# -*- coding: utf-8 -*-

import BeautifulSoup, requests, os, time, sys

dic = []

while True:
	os.system('clear')
	data = requests.get('http://www.transfolha.com.br/outros/PesquisaHttpEntrega.asp?sCliente=&sChave=&sPesquisa=PEDIDO&sDado=&sProtocolo=')
	
	if data.text.find('consultas ao mesmo pedido') != -1:
		print 'Numero máximo de consultas.\n'
		for x in range(1800):
			print '\r' + str(1800 - x), 'segundos para próxima consulta.',
			sys.stdout.flush()
			time.sleep(1)

	try:
		soup = BeautifulSoup.BeautifulSoup(data.text)
		data = soup.findAll('td', attrs={'class':'texto_Padrao_Preto'})[0].text
		
		if data not in dic:
			print '\n[+] Nova movimentação:'
			print '[+] Data:', soup.findAll('td', attrs={'class':'texto_Padrao_Preto'})[0].text
			print '[+] Descrição:', soup.findAll('td', attrs={'class':'texto_Padrao_Preto'})[1].text
			print '[+] Para:', soup.findAll('td', attrs={'class':'texto_Padrao_Preto'})[2].text

			dic.append(data)

			raw_input('\nPressione ENTER para continuar monitorando.')

		for x in range(3600):
			print '\r' + str(3600 - x), 'segundos para próxima consulta.',
			sys.stdout.flush()
			time.sleep(1)
	except:
		pass
