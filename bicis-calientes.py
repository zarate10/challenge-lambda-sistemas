from pathlib import Path
import csv

def valid_time(fecha_origen_recorrido, time_range):
    hora = fecha_origen_recorrido.split(' ')[1]
    return hora > time_range['inicio'] and hora < time_range['fin']

def read_file(path, time_range):
    data = []
    try:
        with open(path, 'rt', encoding='UTF-8-SIG') as file:
            csv_reader = csv.reader(file)
            estaciones = {}

            next(csv_reader)

            for arr in csv_reader:
                if valid_time(arr[3], time_range):
                    if arr[5] in estaciones: 
                        estaciones[arr[5]] += 1 
                    else: 
                        estaciones[arr[5]] = 1 

            data = list(dict(sorted(estaciones.items(), key=lambda item: item[1], reverse=True)).items())[:3]
    except Exception as e:
        print('Ocurrió un error:', e)
    else:
        print('Archivo importado correctamente.')
    finally:
        return data

CURRENT_PATH = Path(__file__).parent

time_range = {
    "inicio": '06:00:00', 
    "fin": '11:59:59'
}

data = read_file(CURRENT_PATH / 'trips_2023.csv', time_range)

print(data) # -> [('147 - Constitución', 15884), ('130 - RETIRO II', 9082), ('014 - Pacifico', 6495)]