
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados do arquivo gasolina.csv
df = pd.read_csv('gasolina.csv')

# Garantir que o campo 'dia' seja interpretado como uma data
df['dia'] = pd.to_datetime(df['dia'])

# Criar o gráfico de linha
plt.figure(figsize=(12, 6))
sns.lineplot(x='dia', y='preço', data=df, marker='o', color='blue')

# Personalizar o gráfico
plt.title('Preço da Gasolina ao Longo do Tempo')
plt.xlabel('Dia')
plt.ylabel('Preço da Gasolina')
plt.xticks(rotation=45)
plt.grid(True)

# Salvar o gráfico como um arquivo PNG
plt.savefig('gasolina.png', bbox_inches='tight')
plt.close()
