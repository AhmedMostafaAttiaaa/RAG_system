from helpers.config import get_settings, settings
import os
import random, string

class BaseController:

    def __init__(self):
        self.app_settings = get_settings()
        self.base_dir = os.path.dirname( os.path.dirname(__file__) ) # Give me the path of MINE => we need to reach the src 'main file'
        self.files_dir = os.path.join(
            self.base_dir,
            "assets/files"
        )

    def generate_random_string(self, lenght: int=12):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=lenght))    