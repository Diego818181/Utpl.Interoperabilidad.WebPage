from flask import Flask, jsonify, request, render_template
import requests
import logging

app = Flask(__name__)

@app.route("/")
def home():
    # La funcion render_template cargara el archivo "index.html" del directorio "templates"
    return render_template("index.html")

# URL base de los servicios web finales implementados con FastAPI
API_BASE_URL = "https://utplwso2.tk/utplinteroperabilidadapp/4.0"

# Token de autorizacion (este token debe ser obtenido de manera segura en una aplicacion real)
AUTH_TOKEN = "eyJ4NXQiOiJPREUzWTJaaE1UQmpNRE00WlRCbU1qQXlZemxpWVRJMllqUmhZVFpsT0dJeVptVXhOV0UzWVE9PSIsImtpZCI6ImdhdGV3YXlfY2VydGlmaWNhdGVfYWxpYXMiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbkBjYXJib24uc3VwZXIiLCJhcHBsaWNhdGlvbiI6eyJvd25lciI6ImFkbWluIiwidGllclF1b3RhVHlwZSI6bnVsbCwidGllciI6IjUwUGVyTWluIiwibmFtZSI6IlRlc3RFbXByZXNhcyIsImlkIjoxMCwidXVpZCI6ImJlYmI1OTI1LTM3NWYtNDIyYS04NmQ5LWFhY2Q2NTFhOGM1YiJ9LCJpc3MiOiJodHRwczpcL1wvdXRwbHdzbzIudGs6NDQzXC9hcGltXC9vYXV0aDJcL3Rva2VuIiwidGllckluZm8iOnsiVW5saW1pdGVkIjp7InRpZXJRdW90YVR5cGUiOiJyZXF1ZXN0Q291bnQiLCJncmFwaFFMTWF4Q29tcGxleGl0eSI6MCwiZ3JhcGhRTE1heERlcHRoIjowLCJzdG9wT25RdW90YVJlYWNoIjp0cnVlLCJzcGlrZUFycmVzdExpbWl0IjowLCJzcGlrZUFycmVzdFVuaXQiOm51bGx9fSwia2V5dHlwZSI6IlBST0RVQ1RJT04iLCJzdWJzY3JpYmVkQVBJcyI6W3sic3Vic2NyaWJlclRlbmFudERvbWFpbiI6ImNhcmJvbi5zdXBlciIsIm5hbWUiOiJVdHBsSW50ZXJvcGVyYWJpbGlkYWRBUFBFbXByZXNhcyIsImNvbnRleHQiOiJcL3V0cGxpbnRlcm9wZXJhYmlsaWRhZGFwcFwvNC4wIiwicHVibGlzaGVyIjoiYWRtaW4iLCJ2ZXJzaW9uIjoiNC4wIiwic3Vic2NyaXB0aW9uVGllciI6IlVubGltaXRlZCJ9XSwidG9rZW5fdHlwZSI6ImFwaUtleSIsImlhdCI6MTY5MDkwMjY2MCwianRpIjoiNjliNzczMGQtMTY5NC00ZmM0LWJmYjEtNjYwOGZjYWQ2ZDY5In0=.PlFtZH8fnu2Gm0TpgBRIhqdccdriTNqUWi3_nwbrWa3QA6rgXRVU20wnRhG-sUEXibTXiwLQOX3mEaFSb6ZNOB94AXleEx8A3ks_XKzdL5H2OVnaijSN4xKjvAUpmR_u0hJzaDmTJaJL-FUCZQlxZ5hn1iM5HfGRf2xHGJymUvLav-KglQvHWUFhsiF1TUOk-VrljN_ssnTpbM2id14W3AivbOtcIc16CAKAnCKfsaif2mrbZXnXTv_qmS_HngRQtICZmVy-3kNvBYnAtI9o9m6VJiTbkGvNoGSZL8yRRfQorSeDFdX5Nm1Cz6dsFImwz3tpUbcvWW_fD5ndOx8__Q=="

# Funcion auxiliar para hacer solicitudes HTTP con el header de autorizacion
def make_authorized_request(method, url, data=None):
    headers = {
        "apikey": f"{AUTH_TOKEN}"
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
    #if response.status_code == 200:
    empresa = response
    return jsonify(empresa)
    #else:
    #    return jsonify({"message": "Error creando empresa (v1.0)"}), 500

# Ruta para crear una empresa (version 2.0)
@app.route("/empresas/v2", methods=["POST"])
def crear_empresa_v2():
    data = request.json
    url = f"{API_BASE_URL}/v2_0/empresas?v=2.0"
    response = make_authorized_request("POST", url, data)
    #if response.status_code == 200:
    empresa = response
    return jsonify(empresa)
    #else:
    #    return jsonify({"message": "Error creando empresa (v2.0)"}), 500

# Ruta para crear una empresa (version 3.0)
@app.route("/empresas/v3", methods=["POST"])
def crear_empresa_v3():
    data = request.json
    url = f"{API_BASE_URL}/v3_0/empresas?v=3.0"
    response = make_authorized_request("POST", url, data)
    #if response.status_code == 200:
    empresa = response.json()
    return jsonify(empresa)
    #else:
    #    return jsonify({"message": "Error creando empresa (v3.0)"}), 500

# Ruta para obtener una lista de empresas (version 1.0)
@app.route("/empresas/v1", methods=["GET"])
def get_empresas_v1():
    url = f"{API_BASE_URL}/v1_0/empresas?v=1.0"
    response = make_authorized_request("GET", url)
    #if response.status_code == 200:
    empresas = response
    return jsonify(empresas)
    #else:
    #    return jsonify({"message": "Error obteniendo empresas (v1.0)"}), 500

# Ruta para obtener una lista de empresas (version 2.0)
@app.route("/empresas/v2", methods=["GET"])
def get_empresas_v2():
    url = f"{API_BASE_URL}/v2_0/empresas?v=2.0"
    response = make_authorized_request("GET", url)
    #if response.status_code == 200:
    empresas = response
    return jsonify(empresas)
    #else:
    #    return jsonify({"message": "Error obteniendo empresas (v2.0)"}), 500

# Ruta para obtener una lista de empresas (version 3.0)
@app.route("/empresas/v3", methods=["GET"])
def get_empresas_v3():
    url = f"{API_BASE_URL}/v3_0/empresas?v=3.0"
    response = make_authorized_request("GET", url)
    #if response.status_code == 200:
    empresas = response
    return jsonify(empresas)
    #else:
    #    return jsonify({"message": "Error obteniendo empresas (v3.0)"}), 500

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
    #if response.status_code == 200:
    return jsonify({"message": "Empresa eliminada (v1.0)"})
    #else:
    #    return jsonify({"message": "Error eliminando empresa (v1.0)"}), 500

# Ruta para eliminar una empresa (version 2.0)
@app.route("/empresas/v2/<id>", methods=["DELETE"])
def eliminar_empresa_v2(id):
    url = f"{API_BASE_URL}/v2_0/empresas/{id}?v=2.0"
    response = make_authorized_request("DELETE", url)
    #if response.status_code == 200:
    return jsonify({"message": "Empresa eliminada (v2.0)"})
    #else:
    #    return jsonify({"message": "Error eliminando empresa (v2.0)"}), 500

# Ruta para eliminar una empresa (version 3.0)
@app.route("/empresas/v3/<id>", methods=["DELETE"])
def eliminar_empresa_v3(id):
    url = f"{API_BASE_URL}/v3_0/empresas/{id}?v=3.0"
    response = make_authorized_request("DELETE", url)
    #if response.status_code == 200:
    return jsonify({"message": "Empresa eliminada (v3.0)"})
    #else:
    #    return jsonify({"message": "Error eliminando empresa (v3.0)"}), 500

# Ruta para crear una persona (version 1.0)
@app.route("/personas/v1", methods=["POST"])
def crear_persona_v1():
    data = request.json
    url = f"{API_BASE_URL}/v1_0/personas?v=1.0"    
    try:
        response = make_authorized_request("POST", url, data)
        #if response.status_code == 200:
        persona = response
        return jsonify(persona)
        #else:
        #    return jsonify({"message": "Error creando persona (v1.0)"}), 500
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
    #if response.status_code == 200:
    persona = response
    return jsonify(persona)
    #else:
    #    return jsonify({"message": "Error creando persona (v2.0)"}), 500

# Ruta para crear una persona (version 3.0)
@app.route("/personas/v3", methods=["POST"])
def crear_persona_v3():
    data = request.json
    url = f"{API_BASE_URL}/v3_0/personas?v=3.0"
    response = make_authorized_request("POST", url, data)
    #if response.status_code == 200:
    persona = response
    return jsonify(persona)
    #else:
    #    return jsonify({"message": "Error creando persona (v3.0)"}), 500

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
    #if response.status_code == 200:
    personas = response
    return jsonify(personas)
    #else:
    #    return jsonify({"message": "Error obteniendo personas (v3.0)"}), 500

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
    #if response.status_code == 200:
    return jsonify({"message": "Persona eliminada (v1.0)"})
    #else:
    #    return jsonify({"message": "Error eliminando persona (v1.0)"}), 500

# Ruta para eliminar una persona (version 2.0)
@app.route("/personas/v2/<id>", methods=["DELETE"])
def eliminar_persona_v2(id):
    url = f"{API_BASE_URL}/v2_0/personas/{id}?v=2.0"
    response = make_authorized_request("DELETE", url)
    #if response.status_code == 200:
    return jsonify({"message": "Persona eliminada (v2.0)"})
    #else:
    #    return jsonify({"message": "Error eliminando persona (v2.0)"}), 500

# Ruta para eliminar una persona (version 3.0)
@app.route("/personas/v3/<id>", methods=["DELETE"])
def eliminar_persona_v3(id):
    url = f"{API_BASE_URL}/v3_0/personas/{id}?v=3.0"
    response = make_authorized_request("DELETE", url)
    #if response.status_code == 200:
    return jsonify({"message": "Persona eliminada (v3.0)"})
    #else:
    #    return jsonify({"message": "Error eliminando persona (v3.0)"}), 500

if __name__ == "__main__":
    app.run(debug=True)
