from fastapi.openapi.utils import get_openapi
from book_api.models.book_response import bookResObj
from pprint import pprint


def custom_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Books Review by Camilla",
        version="1.0.0",
        openapi_version="3.0.0",
        description="Book review service",
        routes=app.routes
    )

    # Initialize paths and components
    openapi_schema.setdefault("paths", {})
    components = openapi_schema.setdefault("components", {"schemas": {}})
    components.setdefault("securitySchemes", {})

    pprint(openapi_schema["components"].get('securitySchemes'))
    # Add security schemes
    openapi_schema["components"]["securitySchemes"]["BasicAuth"] = {
        "type": "http",
        "scheme": "basic"
    }

    app.openapi_schema = openapi_schema
    return app.openapi_schema

