from typing import List
from typing import Dict
from src.side_confiure.master import SideMaster


class ReplaceConfigure:
    def __init__(self, filtered_side: List[Dict[str, str]], side_config: Dict[str, str]):
        self.master = SideMaster()
        self.filtered_side = filtered_side
        self.side_config = side_config

    def change_user_info(self, side_list: List[Dict[str, str]], configure_info: Dict[str, str]) -> List[Dict[str, str]]:
        """[summary]
        변경되지 않은 side 파일들이 들어와서 변경할 설정들을 변경해서 List로 반환

        Args:
            side_list (List[Dict[str, str]]): [description]
            configure_info (Dict[str, str]): [description]

        Returns:
            List[Dict[str, str]]: 넘겨받은 설정들이 적용된 side 파일 데이터 List
        """
        pass

    def __call__(self):
        pass
