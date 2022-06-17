from starlite import Router

from ..controllers.home_controller import HomeController

base_router = Router(path="/base", route_handlers=[HomeController])
