from flask import Flask, jsonify, request, render_template
import requests
import logging

app = Flask(__name__)

@app.route("/")
def index():
    # La funcion render_template cargara el archivo "index.html" del directorio "templates"
    return render_template("index.html")

# URL base de los servicios web finales implementados con FastAPI
API_BASE_URL = "https://utplwso2.tk/utplinteroperabilidadapp/3.0"

# Token de autorizacion (este token debe ser obtenido de manera segura en una aplicacion real)
AUTH_TOKEN = "eyJ4NXQiOiJNV0l5TkRJNVlqRTJaV1kxT0RNd01XSTNOR1ptTVRZeU5UTTJOVFZoWlRnMU5UTTNaVE5oTldKbVpERTFPVEE0TldFMVlUaGxNak5sTldFellqSXlZUSIsImtpZCI6Ik1XSXlOREk1WWpFMlpXWTFPRE13TVdJM05HWm1NVFl5TlRNMk5UVmhaVGcxTlRNM1pUTmhOV0ptWkRFMU9UQTROV0UxWVRobE1qTmxOV0V6WWpJeVlRX1JTMjU2IiwidHlwIjoiYXQrand0IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJlMjkzYjRiNS0xNmFhLTQ5NTQtYTdiYi00NDU1NTIyMWU1MDciLCJhdXQiOiJBUFBMSUNBVElPTiIsImF1ZCI6IjNlRkU5QUMwdmJnc0w4NWFvWjhza2ZNOVhUUWEiLCJuYmYiOjE2OTA2MDQ4NDMsImF6cCI6IjNlRkU5QUMwdmJnc0w4NWFvWjhza2ZNOVhUUWEiLCJzY29wZSI6ImRlZmF1bHQiLCJpc3MiOiJodHRwczpcL1wvbG9jYWxob3N0Ojk0NDNcL29hdXRoMlwvdG9rZW4iLCJleHAiOjE2OTA2MDg0NDMsImlhdCI6MTY5MDYwNDg0MywianRpIjoiMzliNTAwOTYtNjE3Ny00NzRhLWFkZWUtOTRjNTk4OTUyZDljIiwiY2xpZW50X2lkIjoiM2VGRTlBQzB2YmdzTDg1YW9aOHNrZk05WFRRYSJ9.jNN6WMiIxoKquEJo3fB7H3-DNmVSlNgR-CmkiFAabTidap96PfDgjwkZAJ14_rufihEIIp5UwsI5-bT_PhbDw1d6JGmpfDaV4iIOAwl_J8IaL_JbW6eTRy_B6RlwCOVaTnkLTV8CWOJQeSqol1QXQt_2Csy0Ysx90pDMJ8OPLXh4pBIVQx0nNAuc67DdsDnUuO89SfZXq5ZSY73hfMJ449NQcP2oBVaAIYDgtm5jJKPxIGjoYupFaPWvwTPrt-BPyFtAynmzM8FNdMF8XoJUcbYH53KAmxQkGzHetwlwd7gw3sUqNhvZe9HPWZMKvjd11mdJyoYvfQSLvp6C6BT1WQ"

# Funcion auxiliar para hacer solicitudes HTTP con el header de autorizacion
def make_authorized_request(method, url, data=None):
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }
    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, json=data, headers=headers)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError("Metodo HTTP no valido")

        response.raise_for_status()  # Lanzar una excepcion si la solicitud no es exitosa

        return response.json()
    except Exception as e:
        # Si ocurre un error, devolver un JSON con el mensaje de error
        error_message = f"Error en la solicitud: {str(e)}"
        return {"error": error_message}

# Ruta para crear una empresa (version 1.0)
@app.route("/empresas/v1", methods=["POST"])
def crear_empresa_v1():
    data = request.json
    url = f"{API_BASE_URL}/empresas?v=1.0"
    response = make_authorized_request("POST", url, data)
    if response.status_code == 200:
        empresa = response.json()
        return jsonify(empresa)
    else:
        return jsonify({"message": "Error creando empresa (v1.0)"}), 500

# Ruta para crear una empresa (version 2.0)
@app.route("/empresas/v2", methods=["POST"])
def crear_empresa_v2():
    data = request.json
    url = f"{API_BASE_URL}/empresas?v=2.0"
    response = make_authorized_request("POST", url, data)
    if response.status_code == 200:
        empresa = response.json()
        return jsonify(empresa)
    else:
        return jsonify({"message": "Error creando empresa (v2.0)"}), 500

# Ruta para crear una empresa (version 3.0)
@app.route("/empresas/v3", methods=["POST"])
def crear_empresa_v3():
    data = request.json
    url = f"{API_BASE_URL}/empresas?v=3.0"
    response = make_authorized_request("POST", url, data)
    if response.status_code == 200:
        empresa = response.json()
        return jsonify(empresa)
    else:
        return jsonify({"message": "Error creando empresa (v3.0)"}), 500

# Ruta para obtener una lista de empresas (version 1.0)
@app.route("/empresas/v1", methods=["GET"])
def get_empresas_v1():
    url = f"{API_BASE_URL}/empresas?v=1.0"
    response = make_authorized_request("GET", url)
    if response.status_code == 200:
        empresas = response.json()
        return jsonify(empresas)
    else:
        return jsonify({"message": "Error obteniendo empresas (v1.0)"}), 500

# Ruta para obtener una lista de empresas (version 2.0)
@app.route("/empresas/v2", methods=["GET"])
def get_empresas_v2():
    url = f"{API_BASE_URL}/empresas?v=2.0"
    response = make_authorized_request("GET", url)
    if response.status_code == 200:
        empresas = response.json()
        return jsonify(empresas)
    else:
        return jsonify({"message": "Error obteniendo empresas (v2.0)"}), 500

# Ruta para obtener una lista de empresas (version 3.0)
@app.route("/empresas/v3", methods=["GET"])
def get_empresas_v3():
    url = f"{API_BASE_URL}/empresas?v=3.0"
    response = make_authorized_request("GET", url)
    if response.status_code == 200:
        empresas = response.json()
        return jsonify(empresas)
    else:
        return jsonify({"message": "Error obteniendo empresas (v3.0)"}), 500

# Ruta para eliminar una empresa (version 1.0)
@app.route("/empresas/v1/<id>", methods=["DELETE"])
def eliminar_empresa_v1(id):
    url = f"{API_BASE_URL}/empresas/{id}?v=1.0"
    response = make_authorized_request("DELETE", url)
    if response.status_code == 200:
        return jsonify({"message": "Empresa eliminada (v1.0)"})
    else:
        return jsonify({"message": "Error eliminando empresa (v1.0)"}), 500

# Ruta para eliminar una empresa (version 2.0)
@app.route("/empresas/v2/<id>", methods=["DELETE"])
def eliminar_empresa_v2(id):
    url = f"{API_BASE_URL}/empresas/{id}?v=2.0"
    response = make_authorized_request("DELETE", url)
    if response.status_code == 200:
        return jsonify({"message": "Empresa eliminada (v2.0)"})
    else:
        return jsonify({"message": "Error eliminando empresa (v2.0)"}), 500

# Ruta para eliminar una empresa (version 3.0)
@app.route("/empresas/v3/<id>", methods=["DELETE"])
def eliminar_empresa_v3(id):
    url = f"{API_BASE_URL}/empresas/{id}?v=3.0"
    response = make_authorized_request("DELETE", url)
    if response.status_code == 200:
        return jsonify({"message": "Empresa eliminada (v3.0)"})
    else:
        return jsonify({"message": "Error eliminando empresa (v3.0)"}), 500

# Ruta para crear una persona (version 1.0)
@app.route("/personas/v1", methods=["POST"])
def crear_persona_v1():
    data = request.json
    url = f"{API_BASE_URL}/personas?v=1.0"    
    try:
        response = make_authorized_request("POST", url, data)
        if response.status_code == 200:
            persona = response.json()
            return jsonify(persona)
        else:
            return jsonify({"message": "Error creando persona (v1.0)"}), 500
    except Exception as e:
        # Registrar el error
        logging.exception("Error en la solicitud para crear persona (v1.0)")
        return jsonify({"message": "Error interno del servidor"}), 500

# Ruta para crear una persona (version 2.0)
@app.route("/personas/v2", methods=["POST"])
def crear_persona_v2():
    data = request.json
    url = f"{API_BASE_URL}/personas?v=2.0"
    response = make_authorized_request("POST", url, data)
    if response.status_code == 200:
        persona = response.json()
        return jsonify(persona)
    else:
        return jsonify({"message": "Error creando persona (v2.0)"}), 500

# Ruta para crear una persona (version 3.0)
@app.route("/personas/v3", methods=["POST"])
def crear_persona_v3():
    data = request.json
    url = f"{API_BASE_URL}/personas?v=3.0"
    response = make_authorized_request("POST", url, data)
    if response.status_code == 200:
        persona = response.json()
        return jsonify(persona)
    else:
        return jsonify({"message": "Error creando persona (v3.0)"}), 500

# Ruta para obtener una lista de personas (version 1.0)
@app.route("/personas/v1", methods=["GET"])
def get_personas_v1():
    url = f"{API_BASE_URL}/personas?v=1.0"
    response = make_authorized_request("GET", url)
    if response.status_code == 200:
        personas = response.json()
        return jsonify(personas)
    else:
        return jsonify({"message": "Error obteniendo personas (v1.0)"}), 500

# Ruta para obtener una lista de personas (version 2.0)
@app.route("/personas/v2", methods=["GET"])
def get_personas_v2():
    url = f"{API_BASE_URL}/personas?v=2.0"
    response = make_authorized_request("GET", url)
    if response.status_code == 200:
        personas = response.json()
        return jsonify(personas)
    else:
        return jsonify({"message": "Error obteniendo personas (v2.0)"}), 500

# Ruta para obtener una lista de personas (version 3.0)
@app.route("/personas/v3", methods=["GET"])
def get_personas_v3():
    url = f"{API_BASE_URL}/personas?v=3.0"
    response = make_authorized_request("GET", url)
    if response.status_code == 200:
        personas = response.json()
        return jsonify(personas)
    else:
        return jsonify({"message": "Error obteniendo personas (v3.0)"}), 500

# Ruta para eliminar una persona (version 1.0)
@app.route("/personas/v1/<id>", methods=["DELETE"])
def eliminar_persona_v1(id):
    url = f"{API_BASE_URL}/personas/{id}?v=1.0"
    response = make_authorized_request("DELETE", url)
    if response.status_code == 200:
        return jsonify({"message": "Persona eliminada (v1.0)"})
    else:
        return jsonify({"message": "Error eliminando persona (v1.0)"}), 500

# Ruta para eliminar una persona (version 2.0)
@app.route("/personas/v2/<id>", methods=["DELETE"])
def eliminar_persona_v2(id):
    url = f"{API_BASE_URL}/personas/{id}?v=2.0"
    response = make_authorized_request("DELETE", url)
    if response.status_code == 200:
        return jsonify({"message": "Persona eliminada (v2.0)"})
    else:
        return jsonify({"message": "Error eliminando persona (v2.0)"}), 500

# Ruta para eliminar una persona (version 3.0)
@app.route("/personas/v3/<id>", methods=["DELETE"])
def eliminar_persona_v3(id):
    url = f"{API_BASE_URL}/personas/{id}?v=3.0"
    response = make_authorized_request("DELETE", url)
    if response.status_code == 200:
        return jsonify({"message": "Persona eliminada (v3.0)"})
    else:
        return jsonify({"message": "Error eliminando persona (v3.0)"}), 500

if __name__ == "__main__":
    app.run(debug=True)
