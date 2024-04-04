import json

from connexion.lifecycle import ConnexionRequest, ConnexionResponse


def handle_http_error(request: ConnexionRequest, exc: Exception) -> ConnexionResponse:
    return ConnexionResponse(
        status_code=exc.status_code,
        mimetype="application/json",
        body=json.dumps({"message": exc.message}),
    )
