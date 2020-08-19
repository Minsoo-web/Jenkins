from src.side_confiure.configure import ReplaceConfigure
from src.side_filter.side_filter import SideFilter
from src.url_manager.master import Runner
from src.url_manager.io_manager import FileManager

from typing import List
from typing import Dict

import fire
import sys


class Pipeline:
    def __init__(self):
        self._writer = FileManager.Writer()
        self._reader = FileManager.Reader()

    def setting(self, build_target, user_name, user_pw, menu_target):
        config = {
            'build_target': build_target,
            'menu_target': menu_target,
            'user_name': user_name,
            'user_pw': user_pw
        }
        self._writer.write_JSON_file("config.json", "w", config)

    def get_side(self):
        config = self._reader.read_JSON_file('config.json', 'r')
        SideFilter(build_target=config["build_target"], menu_target=config["menu_target"])()

    def change_info(self):
        pass


if __name__ == "__main__":
    fire.Fire(Pipeline)
