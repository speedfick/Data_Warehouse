# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

import pandas as pd

excel1 = pd.read_excel(r'Dados/first_table.xlsx')


#Remove Nulls
excel2 = excel1.dropna()
#Remove Coluna Id
excel3 = excel2.drop('Id',axis=1)
#Range Idades 
excel4 = excel3.loc[(excel3.Idade > 0) & (excel3.Idade < 100)]
#Range Filhos 
excel5 = excel4.loc[(excel4.Filhos > 0) & (excel4.Filhos < 50)]

#verify Sexo (Masculino (M) ou Feminino(F))
excel6 = excel5[(excel5.Sexo == 'F') | (excel5.Sexo == 'M')]

#verify Casado (Sim ou Não)
excel7 = excel6[(excel6.Casado == 'Sim') | (excel6.Casado == 'Não')]

#verify Região (Aldeia ou Cidade ou Vila)
excel8 = excel7[(excel7.Região == 'Aldeia') | (excel7.Região == 'Cidade') | (excel6.Região == 'Vila')]

#verify Carro (Sim ou Não)
excel9 = excel8[(excel8.Carro == 'Sim') | (excel8.Carro == 'Não')]

#verify Conta Prazo (Sim ou Não)
excel10 = excel9[(excel9.Prazo == 'Sim') | (excel9.Prazo == 'Não')]

#verify Conta Ordem (Sim ou Não)
excel10 = excel9[(excel9.Ordem == 'Sim') | (excel9.Ordem == 'Não')]

#verify Credito Habitaçao (Sim ou Não)
excel11 = excel10[(excel10.Crédito == 'Sim') | (excel10.Crédito == 'Não')]

#verify Camapanha Anterior (Sim ou Não)
excel12 = excel11[(excel11.CampanhaAnterior == 'Sim') | (excel11.CampanhaAnterior == 'Não')]

Filhos = excel12['Filhos']
Filhos.to_excel('AfterETl/TemFilhos.xlsx')

Idade = excel12['Idade']
Idade.to_excel('AfterETL/Idade.xlsx')

Sexo = excel12['Sexo']
Sexo.to_excel('AfterETL/Sexo.xlsx')

Região = excel12['Região']
Região.to_excel('AfterETL/Região.xlsx')

Casado = excel12['Casado']
Casado.to_excel('AfterETL/Casado.xlsx')

Carro = excel12['Carro']
Carro.to_excel('AfterETL/TemCarro.xlsx')

Ordem = excel12['Ordem']
Ordem.to_excel('AfterETL/TemContaOrdem.xlsx')

Prazo = excel12['Prazo']
Prazo.to_excel('AfterETL/TemContaPrazo.xlsx')

Credito = excel12['Crédito']
Credito.to_excel('AfterETL/TemCreditoHabitacao.xlsx')

CampanhaAnterior = excel12['CampanhaAnterior']
CampanhaAnterior.to_excel('AfterETL/CampanhaAnterior.xlsx')

excel12.to_excel('AfterETL/AllTable.xlsx')
















      
    
    
    