import logging
import os
import shlex
import subprocess
import shutil
import sys
from colors import color
from typing import List
from typing import NoReturn
from tqdm import tqdm


logging.basicConfig(
    filename='./log',
    level=logging.INFO, filemode='w',
    format='%(asctime)s:\n\t%(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)


class SideFilter:
    def __init__(self, build_target: str, menu_target: str) -> None:
        self.side_command = f"find {build_target} -type f -name '*.side'"
        self.menu_target = menu_target
        self.dist_path = 'dist'

    def call(self, command: str) -> str:
        """find 명령어를 통해 side 파일을 가지고 있는 폴더들을 가져와 str로 만들어준다.

        Args:
            command (str): find 명령어를 받아온다.

        Returns:
            str: 폴더 경로를 가지고 있는 str로 \n으로 구분되어 있다.
        """

        try:
            print(color('Run:', 'yellow'), color(command, 'blue'), end=' ')
            response = subprocess.Popen(
                args=shlex.split(command),
                shell=False,
                stderr=subprocess.STDOUT,
                stdout=subprocess.PIPE
            )
        except FileNotFoundError as e:
            print(e)
            print('command: {command}'.format(command=command))
            logging.error(
                str(e) + '\n\tcommand: {command}'.format(command=command))
            sys.exit(1)
        else:
            print(color('✔', 'green'))
            logging.info('The command was executed normally')

            stdout, _ = response.communicate()
            return stdout.decode('utf-8')

    def split_file_list(self, data: str) -> List[str]:
        """\n이 포함되어 있는 str을 한 줄로 바꿔준 뒤 Set 자료형을 사용해 중복을 제거해주고 다시 배열에 담는다.

        Args:
            data (str): side 파일의 경로를 담고 있는 여러줄의 문자열

        Returns:
            List[str]: 중복이 제거된 폴더 경로
        """
        print(color('Extract only directory name from full path', 'yellow'), end=' ')
        response = sorted(list({os.path.dirname(x)
                                for x in data.splitlines()}))
        logging.info('A total of {response} directories were searched.'.format(
            response=len(response)))
        print(color('✔', 'green'))
        return response

    def copy_files(self, path: List[str]) -> NoReturn:
        """폴더 경로를 배열로 받아 루트 경로의 /dist 로 복사해온다.

        Args:
            path (List[str]): 리스트 형태의 폴더 경로

        Returns:
            NoReturn: dist 폴더가 있으면 삭제하고 없으면 생성해서 복사한다.
        """

        print(color('Check:', 'yellow'), color(
            'dist directory exist', 'blue'), end=' ')
        print(color('✔', 'green'))
        print(color('Copy:', 'yellow'), color('Directory copy', 'blue'))
        if self.menu_target == 'All':
            for dir_path in tqdm(path):
                shutil.copytree(src=dir_path, dst='{dist_path}/{dir_path}'.format(
                    dist_path=self.dist_path, dir_path=dir_path))
        else:
            print("준비 안 됨")
        print(color('✔', 'green'))

    def __call__(self) -> NoReturn:
        """[summary]

        Returns:
            NoReturn: [description]
        """

        if os.path.isdir(self.dist_path):
            shutil.rmtree(self.dist_path)
        os.mkdir(self.dist_path)

        data = self.call(self.side_command)
        list_path = self.split_file_list(data)
        self.copy_files(list_path)
        self.copy_files(['IRIS-E2E-SAAS/qa-script'])
