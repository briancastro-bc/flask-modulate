from flask.views import MethodView
from src.services.index_service import IndexService

class IndexController(MethodView):
    
    def __init__(self) -> None:
        super().__init__()
        self.indexService = IndexService()
    
    def get(self) -> str:
        return self.indexService.index()