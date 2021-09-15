from src.controllers import IndexController, LogInController

routes: dict[str, str] = {
    "index": "/", "index_controller": IndexController.as_view('index'),
    "login": "/login", "login_controller": LogInController.as_view('login')
}