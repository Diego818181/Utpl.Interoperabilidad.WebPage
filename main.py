from flask import Flask, jsonify, request, render_template
import requests
import logging

app = Flask(__name__)

@app.route("/")
def home():
    # La funcion render_template cargara el archivo "index.html" del directorio "templates"
    return render_template("index.html")

# URL base de los servicios web finales implementados con FastAPI
API_BASE_URL = "https://utplwso2.tk/utplinteroperabilidadapp/3.0"

# Token de autorizacion (este token debe ser obtenido de manera segura en una aplicacion real)
AUTH_TOKEN = "eyJ4NXQiOiJNV0l5TkRJNVlqRTJaV1kxT0RNd01XSTNOR1ptTVRZeU5UTTJOVFZoWlRnMU5UTTNaVE5oTldKbVpERTFPVEE0TldFMVlUaGxNak5sTldFellqSXlZUSIsImtpZCI6Ik1XSXlOREk1WWpFMlpXWTFPRE13TVdJM05HWm1NVFl5TlRNMk5UVmhaVGcxTlRNM1pUTmhOV0ptWkRFMU9UQTROV0UxWVRobE1qTmxOV0V6WWpJeVlRX1JTMjU2IiwidHlwIjoiYXQrand0IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJlMjkzYjRiNS0xNmFhLTQ5NTQtYTdiYi00NDU1NTIyMWU1MDciLCJhdXQiOiJBUFBMSUNBVElPTiIsImF1ZCI6IjNlRkU5QUMwdmJnc0w4NWFvWjhza2ZNOVhUUWEiLCJuYmYiOjE2OTA4NTg5MzYsImF6cCI6IjNlRkU5QUMwdmJnc0w4NWFvWjhza2ZNOVhUUWEiLCJzY29wZSI6ImRlZmF1bHQiLCJpc3MiOiJodHRwczpcL1wvbG9jYWxob3N0Ojk0NDNcL29hdXRoMlwvdG9rZW4iLCJleHAiOjE2OTA4NjI1MzYsImlhdCI6MTY5MDg1ODkzNiwianRpIjoiZWQzNzE3MzYtMmIzZS00NzQyLWFlMGQtYzE4NDhiMzU4MjIxIiwiY2xpZW50X2lkIjoiM2VGRTlBQzB2YmdzTDg1YW9aOHNrZk05WFRRYSJ9.lS0jhK4C4Ain7Jklo6WaQzWpemUFPafjRdidYg-6sDdPJQ_KjcS-PR27PS9XllI8-V6IYvz6wOdbGT_J8TmnO07kroYW-OwvBsPV-StEn0x5w49ZytHy99NusA9QVk0ArEru2k1el1vTW9QIZs358_WbEWgKOnQhpmTqLzJ9sCpm-MTWbXFnBUQwvioCg9cheNXqq5f2L_FPRJE5PG99fedMykY-x6ZAbSaz98YAVTVLp9dWyo7iL3BHcG7GqBzinB5OFbEZQplyAs5RpkjdXkGtrBxIXQV8eL_a595UtWTiRyJK69uyU4MyfLE8B0SQxkMLHxWxObrr79eR7xGRmQ"

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
    url = f"{API_BASE_URL}/v1_0/empresas?v=1.0"
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
    url = f"{API_BASE_URL}/v2_0/empresas?v=2.0"
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
    url = f"{API_BASE_URL}/v3_0/empresas?v=3.0"
    response = make_authorized_request("POST", url, data)
    if response.status_code == 200:
        empresa = response.json()
        return jsonify(empresa)
    else:
        return jsonify({"message": "Error creando empresa (v3.0)"}), 500

# Ruta para obtener una lista de empresas (version 1.0)
@app.route("/empresas/v1", methods=["GET"])
def get_empresas_v1():
    url = f"{API_BASE_URL}/v1_0/empresas?v=1.0"
    response = make_authorized_request("GET", url)
    if response.status_code == 200:
        empresas = response.json()
        return jsonify(empresas)
    else:
        return jsonify({"message": "Error obteniendo empresas (v1.0)"}), 500

# Ruta para obtener una lista de empresas (version 2.0)
@app.route("/empresas/v2", methods=["GET"])
def get_empresas_v2():
    url = f"{API_BASE_URL}/v2_0/empresas?v=2.0"
    response = make_authorized_request("GET", url)
    if response.status_code == 200:
        empresas = response.json()
        return jsonify(empresas)
    else:
        return jsonify({"message": "Error obteniendo empresas (v2.0)"}), 500

# Ruta para obtener una lista de empresas (version 3.0)
@app.route("/empresas/v3", methods=["GET"])
def get_empresas_v3():
    url = f"{API_BASE_URL}/v3_0/empresas?v=3.0"
    response = make_authorized_request("GET", url)
    if response.status_code == 200:
        empresas = response.json()
        return jsonify(empresas)
    else:
        return jsonify({"message": "Error obteniendo empresas (v3.0)"}), 500

# Ruta para obtener una empresa por ID (version 1.0)
@app.route("/empresas/v1/<id>", methods=["GET"])
def obtener_empresa_v1(id):
    url = f"{API_BASE_URL}/v1_0/empresas/{id}?v=1.0"
    response = make_authorized_request("GET", url)
    if response.get("error"):
        return jsonify({"message": "Empresa no encontrada (v1.0)"}), 404
    else:
        return jsonify(response)

# Ruta para obtener una empresa por ID (version 2.0)
@app.route("/empresas/v2/<id>", methods=["GET"])
def obtener_empresa_v2(id):
    url = f"{API_BASE_URL}/v2_0/empresas/{id}?v=2.0"
    response = make_authorized_request("GET", url)
    if response.get("error"):
        return jsonify({"message": "Empresa no encontrada (v2.0)"}), 404
    else:
        return jsonify(response)

# Ruta para obtener una empresa por ID (version 3.0)
@app.route("/empresas/v3/<id>", methods=["GET"])
def obtener_empresa_v3(id):
    url = f"{API_BASE_URL}/v3_0/empresas/{id}?v=3.0"
    response = make_authorized_request("GET", url)
    if response.get("error"):
        return jsonify({"message": "Empresa no encontrada (v3.0)"}), 404
    else:
        return jsonify(response)


# Ruta para eliminar una empresa (version 1.0)
@app.route("/empresas/v1/<id>", methods=["DELETE"])
def eliminar_empresa_v1(id):
    url = f"{API_BASE_URL}/v1_0/empresas/{id}?v=1.0"
    response = make_authorized_request("DELETE", url)
    if response.status_code == 200:
        return jsonify({"message": "Empresa eliminada (v1.0)"})
    else:
        return jsonify({"message": "Error eliminando empresa (v1.0)"}), 500

# Ruta para eliminar una empresa (version 2.0)
@app.route("/empresas/v2/<id>", methods=["DELETE"])
def eliminar_empresa_v2(id):
    url = f"{API_BASE_URL}/v2_0/empresas/{id}?v=2.0"
    response = make_authorized_request("DELETE", url)
    if response.status_code == 200:
        return jsonify({"message": "Empresa eliminada (v2.0)"})
    else:
        return jsonify({"message": "Error eliminando empresa (v2.0)"}), 500

# Ruta para eliminar una empresa (version 3.0)
@app.route("/empresas/v3/<id>", methods=["DELETE"])
def eliminar_empresa_v3(id):
    url = f"{API_BASE_URL}/v3_0/empresas/{id}?v=3.0"
    response = make_authorized_request("DELETE", url)
    if response.status_code == 200:
        return jsonify({"message": "Empresa eliminada (v3.0)"})
    else:
        return jsonify({"message": "Error eliminando empresa (v3.0)"}), 500

# Ruta para crear una persona (version 1.0)
@app.route("/personas/v1", methods=["POST"])
def crear_persona_v1():
    data = request.json
    url = f"{API_BASE_URL}/v1_0/personas?v=1.0"    
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
    url = f"{API_BASE_URL}/v2_0/personas?v=2.0"
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
    url = f"{API_BASE_URL}/v3_0/personas?v=3.0"
    response = make_authorized_request("POST", url, data)
    if response.status_code == 200:
        persona = response.json()
        return jsonify(persona)
    else:
        return jsonify({"message": "Error creando persona (v3.0)"}), 500

# Ruta para obtener una lista de personas (version 1.0)
@app.route("/personas/v1", methods=["GET"])
def get_personas_v1():
    print("personaV1")
    url = f"{API_BASE_URL}/v1_0/personas?v=1.0"
    response = make_authorized_request("GET", url)
    print(response)
    #if response.status_code == 200:
    personas = response
    return jsonify(personas)
    #else:
        #return jsonify({"message": "Error obteniendo personas (v1.0)"}), 500

# Ruta para obtener una lista de personas (version 2.0)
@app.route("/personas/v2", methods=["GET"])
def get_personas_v2():
    print("personaV2")
    url = f"{API_BASE_URL}/v2_0/personas?v=2.0"
    response = make_authorized_request("GET", url)
    print(response)
    #if response.status_code == 200:
    personas = response
    return jsonify(personas)

# Ruta para obtener una lista de personas (version 3.0)
@app.route("/personas/v3", methods=["GET"])
def get_personas_v3():
    url = f"{API_BASE_URL}/v3_0/personas?v=3.0"
    response = make_authorized_request("GET", url)
    if response.status_code == 200:
        personas = response.json()
        return jsonify(personas)
    else:
        return jsonify({"message": "Error obteniendo personas (v3.0)"}), 500

# Ruta para obtener una persona por ID (version 1.0)
@app.route("/personas/v1/<id>", methods=["GET"])
def obtener_persona_v1(id):
    url = f"{API_BASE_URL}/v1_0/personas/{id}?v=1.0"
    response = make_authorized_request("GET", url)
    if response.get("error"):
        return jsonify({"message": "Persona no encontrada (v1.0)"}), 404
    else:
        return jsonify(response)

# Ruta para obtener una persona por ID (version 2.0)
@app.route("/personas/v2/<id>", methods=["GET"])
def obtener_persona_v2(id):
    url = f"{API_BASE_URL}/v2_0/personas/{id}?v=2.0"
    response = make_authorized_request("GET", url)
    if response.get("error"):
        return jsonify({"message": "Persona no encontrada (v2.0)"}), 404
    else:
        return jsonify(response)

# Ruta para obtener una persona por ID (version 3.0)
@app.route("/personas/v3/<id>", methods=["GET"])
def obtener_persona_v3(id):
    url = f"{API_BASE_URL}/v3_0/personas/{id}?v=3.0"
    response = make_authorized_request("GET", url)
    if response.get("error"):
        return jsonify({"message": "Persona no encontrada (v3.0)"}), 404
    else:
        return jsonify(response)

# Ruta para eliminar una persona (version 1.0)
@app.route("/personas/v1/<id>", methods=["DELETE"])
def eliminar_persona_v1(id):
    url = f"{API_BASE_URL}/v1_0/personas/{id}?v=1.0"
    response = make_authorized_request("DELETE", url)
    if response.status_code == 200:
        return jsonify({"message": "Persona eliminada (v1.0)"})
    else:
        return jsonify({"message": "Error eliminando persona (v1.0)"}), 500

# Ruta para eliminar una persona (version 2.0)
@app.route("/personas/v2/<id>", methods=["DELETE"])
def eliminar_persona_v2(id):
    url = f"{API_BASE_URL}/v2_0/personas/{id}?v=2.0"
    response = make_authorized_request("DELETE", url)
    if response.status_code == 200:
        return jsonify({"message": "Persona eliminada (v2.0)"})
    else:
        return jsonify({"message": "Error eliminando persona (v2.0)"}), 500

# Ruta para eliminar una persona (version 3.0)
@app.route("/personas/v3/<id>", methods=["DELETE"])
def eliminar_persona_v3(id):
    url = f"{API_BASE_URL}/v3_0/personas/{id}?v=3.0"
    response = make_authorized_request("DELETE", url)
    if response.status_code == 200:
        return jsonify({"message": "Persona eliminada (v3.0)"})
    else:
        return jsonify({"message": "Error eliminando persona (v3.0)"}), 500

if __name__ == "__main__":
    app.run(debug=True)
