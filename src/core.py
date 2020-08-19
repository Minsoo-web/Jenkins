from src.side_confiure.replace_configure import ReplaceConfigure
from src.side_filter.side_filter import SideFilter
from src.url_manager.master import Runner
from src.url_manager.io_manager import FileManager

from typing import List
from typing import Dict
from typing import NoReturn

import fire
import sys


class Pipeline:
    def __init__(self):
        self._writer = FileManager.Writer()
        self._reader = FileManager.Reader()

    def setting(self, build_target: str, menu_target: str, user: str, password='biris.manse') -> NoReturn:
        """
        받아온 파라미터를 세팅해서 config.json에 저장해준다.

        Args:
            build_target (str): 'IRIS-E2E' 또는 'IRIS-E2E-SASS'
            menu_target (str): '00.SETUP', 'IRIS-E2E-SAAS-ENG 등등의 대메뉴 타겟
            user (str): admin 또는 regular
            password (str, optional): IRIS-E2E의 비밀번호 변경을 위한 파라미터.
                                      /root/loginpass.auth 를 받는다.
                                      Defaults to 'biris.manse'.
        Returns:
            NoReturn: [description]
        """

        if password != 'biris.manse':
            password = self._reader.read_raw_file(password, 'r')
        config = {
            'build_target': build_target,
            'menu_target': menu_target,
            'user': user,
            'root_pw': password
        }
        self._writer.write_JSON_file("config.json", "w", config)

    def get_side(self) -> NoReturn:
        """
        Returns:
            NoReturn: 다음과 같은 구조로 만들어준다.
                      dist - [빌드타겟] - [메뉴타겟]
                                      |
                                      - [qa-script]
        """

        config = self._reader.read_JSON_file('config.json', 'r')
        SideFilter(build_target=config["build_target"], menu_target=config["menu_target"], user=config["user"])()

    def change_config(self):
        config = self._reader.read_JSON_file('config.json', 'r')
        ReplaceConfigure()


if __name__ == "__main__":
    fire.Fire(Pipeline)
