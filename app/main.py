from starlite import CORSConfig, Starlite

from .routers.base import base_router

app = Starlite(
    route_handlers=[base_router],
    cors_config=CORSConfig(),
)
