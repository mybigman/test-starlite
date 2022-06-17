from starlite import CORSConfig, Starlite

from routers.base import base_router

app = Starlite(
    route_handlers=[base_router],
    cors_config=CORSConfig(),
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, debug=True)
