# -- Ejemplo de cliente web que usa la biblioteca http.client
import http.client
import json

PORT = 8000
archivo = "datos2.json"

# Conectarse con el servidor
conn = http.client.HTTPConnection('localhost', PORT)

# -- Enviar un mensaje de solicitud (Verbo: GET), Recurso: Raiz
conn.request("GET", "/{}".format(archivo))

# -- Leer el mensaje de respuesta recibido del servidor
r1 = conn.getresponse()

# -- Imprimir la linea de estado de la respuesta
print(r1.status, r1.reason)

# -- Leer el contenido de la respuesta y converirlo a una cadena
data1 = r1.read().decode("utf-8")

# -- Imprimir el fichero html recibido
print(data1)

with open(archivo, 'r') as f:
    data = json.load(f)
    temas = 0
    horas = 0
    for p in data['people'][0]["Temas de la asignatura"]:
        horas += p[temas]['Numero de horas']
        temas += 1


print("Número de temas: {}".format(temas))
print("Número de horas: {}".format(horas))
