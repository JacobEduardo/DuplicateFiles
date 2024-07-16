import os
import shutil

def LoadVariablesFromTxt(file_name):
    variables = [] 
    try:
        with open(file_name, 'r') as archivo:
            for linea in archivo:
                variable = linea.strip()
                variables.append(variable)     
    except FileNotFoundError:
        print(f"Error al cargar archivos de: '{file_name}'")
    print(f"{len(variables)} ruts cargados" )
    return variables 
def CreateIndexs(index_1, index_2):
    try:
        generated_names = []
        for k in index_1:
            for j in index_2:
                generated_names.append( k + '_'+ j )
    except Exception as e:
        print(f"Ha acurrido un error al concatener los indices: {str(e)}")
    print(f"Se han generado {len(generated_names)} nombres de archivos")
    return generated_names
def concatenateRutAndData(ruts,fecha, generated_indexs,extension):
    try:
        n = 0
        a = []
        for elemento in generated_indexs:
            a.append(f'{ruts[n]}_{fecha}_{elemento}.{extension}')
            n = n + 1
            if(n == len(ruts)):
                n = 0
        print(f"Rut y fecha concatenado. {len(a)}")
        return a
    except Exception as e:
        print(f"Ha ocurrido un error al generar los nombres: {str(e)}")
        return []

fecha = '2021-10-10'
ruts = LoadVariablesFromTxt('ruts.txt')
index_1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
index_2 = ['6', '3', '4', '5', '8', '7']
extension = 'pdf'

generated_indexs = CreateIndexs(index_1, index_2)
generated_names = concatenateRutAndData(ruts,fecha, generated_indexs,extension)


fordedr_origin = 'files/origin'
folder_destiny = 'files/destiny'

os.makedirs(folder_destiny, exist_ok=True)

for nombre_archivo in os.listdir(fordedr_origin):
    ruta_origen = os.path.join(fordedr_origin, nombre_archivo)
    
    if os.path.isfile(ruta_origen):
        nombre_archivo_duplicado = f"copia_{nombre_archivo}"
        ruta_destino = os.path.join(folder_destiny, nombre_archivo_duplicado)
        
        shutil.copy2(ruta_origen, ruta_destino)
        print(f'Archivo {nombre_archivo} duplicado como {nombre_archivo_duplicado}')