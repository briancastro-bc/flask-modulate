from src.controllers.index_controller import IndexController

routes: dict[str, str] = {
    "index": "/", "index_controller": IndexController.as_view('index'),
}