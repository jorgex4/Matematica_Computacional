import pandas as pd 
#Crear un dataframe (arreglo de datos)

data = {'Nombre': ['John', 'Anna', 'Peter', 'Linda'],
        'Edad': [23, 32, 27, 29],
        'Notas': [5, 3, 4, 3.5],}
df = pd.DataFrame(data)
print(df)

#Calcular promedio de edades
prom_edad = df['Edad'].mean()
print('Promedio de edad:', prom_edad)

#Calcular promedio de notas
prom_nota = df['Notas'].mean()
print('Promedio nota:', prom_nota )

#Clasificacion Notas
def clasificar_notas(nota):
    if 4.5 <= nota <= 5:
        return 'Excelente'
    elif 4 <= nota < 4.5:
        return 'Bueno'
    elif 3 <= nota < 4:
        return 'Regular'
    elif 3 < nota:
        return 'Perdio'
df['Clasificacion'] = df['Notas'].apply(clasificar_notas)
    
       
