import http.server
import socketserver
import os
import json

# -- Puerto donde lanzar el servidor
PORT = 8002
IP = ""


# Clase con nuestro manejador. Es una clase derivada de BaseHTTPRequestHandler
# Esto significa que "hereda" todos los metodos de esta clase. Y los que
# nosotros consideremos los podemos reemplazar por los nuestros
class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    # GET. Este metodo se invoca automaticamente cada vez que hay una
    # peticion GET por HTTP. El recurso que nos solicitan se encuentra
    # en self.path
    def do_GET(self):

        # La primera linea del mensaje de respuesta es el
        # status. Indicamos que OK
        self.send_response(200)

        # En las siguientes lineas de la respuesta colocamos las
        # cabeceras necesarias para que el cliente entienda el
        # contenido que le enviamos (que sera HTML)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Este es el mensaje que enviamos al cliente: un texto y
        # el recurso solicitado
        message = "Hello world! " + self.path

        solicitud = self.path[1:]

        if solicitud in os.listdir():
            if ".json" in self.path:
                    self.send_header('Content-type', 'application/json')
                    with open(solicitud, "r") as f:
                        data = json.load(f)
                        message = data
                        #message = ""
                        #for p in data['people']:
                        #    people = ""
                        #    for i in p.keys():
                        #        people += " {}: {} ".format(i, p[i])
                        #    message += "{} ".format(people)

            else:
                message = FILE_HTML = solicitud
        elif self.path == "/":
            message = """<!doctype html>
            <html>
              <body style='background-color: yellow'>
                <h1>LISTA</h2>
                <p>Aqui tienes una lista con los archivos del directorio:</p>"""
            for i in os.listdir():
                message += "<p>   - " + i + "</p>"
                message += "<a href=\"http://{}:{}/{}\"> Enlace a la {}</a>".format(IP, PORT, i, i)
            message += """</body>
            </html>"""

        else:
            FILE_HTML = "pink.html"

        if solicitud != "" and ".json" not in solicitud:
            with open(FILE_HTML, "r") as f:
                message = f.read()


        # Enviar el mensaaje completo
        self.wfile.write(bytes(message, "utf8"))
        print("File served!")
        return


# ----------------------------------
# El servidor comienza a aqui
# ----------------------------------
# Establecemos como manejador nuestra propia clase
Handler = testHTTPRequestHandler

# -- Configurar el socket del servidor, para esperar conexiones de clientes
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)

# Entrar en el bucle principal
# Las peticiones se atienden desde nuestro manejador
# Cada vez que se ocurra un "GET" se invoca al metodo do_GET de
# nuestro manejador
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("")
    print("Interrumpido por el usuario")

print("")
print("Servidor parado")
httpd.close()

# https://github.com/joshmaker/simple-python-webserver/blob/master/server.py
