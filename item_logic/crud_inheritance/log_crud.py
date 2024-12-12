
from database import MONGOCRUD

class LogCrud(MONGOCRUD):

    def __init__(self):
        super().__init__('Log')