from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates


rest_api = Starlette(debug=True)
templates = Jinja2Templates(directory='kame/templates')

registered_paths = []

@rest_api.route(path="/", name="home")
async def homepage(request):
    json_paths = []
    for path in registered_paths:
        json_paths.append({
            "list": str(request.url) + path.split("/")[1]
        })
    ctx = {
        'request': request,
        "paths": json_paths,
    }
    return templates.TemplateResponse("index.html", ctx)


class DefaultRouter:

    def __init__(self):
        pass

    def register_app(self, app):
        self.app = app
        app.mount("/api", rest_api)
        app.mount('/api-static', StaticFiles(directory='kame/statics'), name='static')

    def register(self, path, model_class, basename=""):
        print(path)
        rest_api.add_route(path, model_class)
        rest_api.add_route(path+"/{id:int}", model_class)
        registered_paths.append(path)
