from starlite.controller import Controller
from starlite.handlers import get


class HomeController(Controller):
    path = "/"

    @get()
    async def home(self) -> None:
        return {"message": "hello"}
