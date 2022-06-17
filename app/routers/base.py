from controllers.home_controller import HomeController
from starlite import Router

base_router = Router(path="/base", route_handlers=[HomeController])
