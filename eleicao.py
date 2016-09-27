import pandas as pd
import numpy as np

#http://agencia.tse.jus.br/estatistica/sead/odsele/prestacao_contas/prestacao_contas_2016.zip
#"despesas_candidatos_2016_brasil.txt".
file_name = '/Users/beatriz/Desktop/projetos/estudos/estudo_pandas/final.csv'

t=pd.read_excel('receitascandidatos1.xls',index_col=None, na_values=['NA'])
t.head()

df = t[['UF'] + ['Nome candidato'] + ['Cargo'] + ['Tipo receita']+['Valor receita']]
df1 = df[(df.Cargo.isin(['Prefeito']))]
uf = df1[(df1.UF.isin(['SP', 'RJ']))]
uf.groupby(['UF','Nome candidato', 'Cargo', 'Tipo receita', 'Valor receita']).sum()
tf = pd.pivot_table(uf,index=['UF','Nome candidato'], columns=['Tipo receita'], values='Valor receita', aggfunc=np.sum,fill_value=0)

tf.to_csv(file_name, encoding='utf-8')
