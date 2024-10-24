import pandas as pd


estudiantes = [
    {'nombre': 'Juan', 'edad': 20, 'carrera': 'Ingenieria de Sistemas'},
    {'nombre': 'Ana', 'edad': 22, 'carrera': 'Ingenieria Civil'},
    {'nombre': 'Carlos', 'edad': 21, 'carrera': 'Ingenieria de Sistemas'},
    {'nombre': 'Luis', 'edad': 23, 'carrera': 'Ingenieria Electrónica'},
    {'nombre': 'Maria', 'edad': 24, 'carrera': 'Ingenieria de Sistemas'} ,
    {'nombre': 'jorge', 'edad': 22, 'carrera': 'Ingenieria de Sistemas'} ,
    {'nombre': 'sebastian', 'edad': 23, 'carrera': 'Ingenieria de Sistemas'} 
]


df = pd.DataFrame(estudiantes)


df_sistemas = df[df['carrera'] == 'Ingenieria de Sistemas']

print("Estudiantes de Ingenieria de Sistemas:")
print(df_sistemas[['nombre', 'edad']].to_string(index=False))

df_mayores_21 = df_sistemas[df_sistemas['edad'] >= 21]


print("\nEstudiantes de Ingenieria de Sistemas mayores de 21 años:")
print(df_mayores_21[['nombre', 'edad']].to_string(index=False))


