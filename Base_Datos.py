import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
pd.set_option('display.max_columns', None)

# Contar los sobrevivientes y los que no sobrevivieron por género
conteo_genero_sobrevivientes = df[df['Survived'] == 1]['Sex'].value_counts()
conteo_genero_no_sobrevivientes = df[df['Survived'] == 0]['Sex'].value_counts()

# Crear un DataFrame para el gráfico
conteo_genero = pd.DataFrame({
    'Sobrevivientes': conteo_genero_sobrevivientes,
    'No sobrevivieron': conteo_genero_no_sobrevivientes
})

# Crear el diagrama de barras
conteo_genero.plot(kind='bar', figsize=(10, 6), color=['blue', 'red'])
plt.title('Sobrevivientes y No Sobrevivientes del Titanic por Género')
plt.xlabel('Género')
plt.ylabel('Cantidad')
plt.xticks(rotation=0)
plt.show()