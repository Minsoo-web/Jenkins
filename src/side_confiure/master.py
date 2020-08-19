from typing import List
from typing import Dict


class SideMaster(object):

    def get_tests(self, data: Dict[str, str]) -> list:
        return data['tests']

    def get_test_id_and_name(self, data: List[str]) -> dict:
        return {x['name']: x['id'] for x in data}

    def get_test_suites(self, data: dict) -> list:
        return data['suites'][0]['tests']
