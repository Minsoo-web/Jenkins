from typing import List
from typing import Dict
from src.side_confiure.master import SideMaster

import glob


class ReplaceConfigure:

    def __init__(self, build_target: str, user: str):
        self._build_target = build_target
        self._user = user
