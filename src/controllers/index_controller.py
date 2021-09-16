from flask.views import MethodView
from src.services import IndexService
from src.hooks import verify_token

class IndexController(MethodView):
    
    decorators = [verify_token]
    
    def __init__(self) -> None:
        super().__init__()
        self.indexService = IndexService()
    
    def get(self) -> str:
        return self.indexService.index()