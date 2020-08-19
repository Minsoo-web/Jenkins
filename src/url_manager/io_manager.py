from typing import Any
import json

from src.utils import isfile


class FileManager(object):
    """Has a class for file I/O."""

    class Reader(object):
        """Can read various types of files."""

        def read_raw_file(self, file: str, mode: str, encoding='utf-8', *, option=None) -> str:
            """Returns any kind of file as a raw string

            Args:
                file (str): The file name to be read.
                mode (str): This is the mode to use when reading files. You can use'r' or'rb'.
                encoding (str, optional): The encoding of the file to be read. Defaults to 'utf-8'.

            Raises:
                FileNotFoundError: If the file does not exist, an error occurs.

            Returns:
                str: The contents of the file.

            >>> FileManager.Reader().read_raw_file(file='./qa-script/side_manager/test_data/password.txt', mode='r')
            'oXIlpT@0:mS^CDvj$Qs2B9XDHSPtAn'

            >>> FileManager.Reader().read_raw_file(file='MyFile', mode='r')
            Traceback (most recent call last):
            FileNotFoundError: MyFile

            >>> FileManager.Reader().read_raw_file(file='./qa-script/side_manager/test_data/password.txt', mode='a')
            Traceback (most recent call last):
            io.UnsupportedOperation: not readable
            """

            if not isfile(path=file):
                raise FileNotFoundError(file)

            with open(file=file, mode=mode, encoding=encoding) as f:
                if option == 'line':
                    data = f.read().splitlines()
                else:
                    data = f.read()

            return data

        def read_JSON_file(self, file: str, mode: str, encoding='utf-8') -> dict:
            """Read a JSON format file.

            Args:
                file (str): The file name to be read.
                mode (str): This is the mode to use when reading files. You can use'r' or'rb'.
                encoding (str, optional): The encoding of the file to be read. Defaults to 'utf-8'.

            Raises:
                FileNotFoundError: If the file does not exist, an error occurs.

            Returns:
                dict: It is a value obtained by converting JSON format data into dictionary format.

            >>> FileManager.Reader().read_JSON_file(file='./qa-script/side_manager/test_data/sample.json', mode='r')
            {'data': ':}}Z[8ASE<s.tWKBoIAdJpX0+>o*B6'}

            >>> FileManager.Reader().read_JSON_file(file='MyJSON', mode='r')
            Traceback (most recent call last):
            FileNotFoundError: MyJSON

            >>> FileManager.Reader().read_JSON_file(file='./qa-script/side_manager/test_data/sample.json', mode='a')
            Traceback (most recent call last):
            io.UnsupportedOperation: not readable
            """

            raw_json = self.read_raw_file(file=file, mode=mode, encoding=encoding)
            data = json.loads(raw_json)

            return data

    class Writer(object):

        def write_raw_file(self, file: str, mode: str, data: Any, encoding='utf-8') -> bool:
            """Any kind of file is saved as raw data.

            Args:
                file (str): The name of the file to be saved.
                mode (str): How to save the file. You can use'w' and'wb' or'a'.
                data (Any): This is the data you want to save as a file.
                encoding (str, optional): The encoding of the file to be write. Defaults to 'utf-8'.

            Returns:
                bool: Returns whether the data was successfully saved.

            >>> writer = FileManager.Writer()
            >>> _ = writer.write_raw_file(file='doctest.out', mode='w', data='Hello world!!')
            >>> reader = FileManager.Reader() 
            >>> reader.read_raw_file(file='doctest.out', mode='r')
            'Hello world!!'
            >>> import os
            >>> os.remove('doctest.out')

            >>> writer.write_raw_file(file='')
            Traceback (most recent call last):
            TypeError: write_raw_file() missing 2 required positional arguments: 'mode' and 'data'
            """

            flag = True
            try:
                with open(file=file, mode=mode, encoding=encoding) as f:
                    f.write(data)
            except Exception:
                flag = False
            finally:
                return flag

        def write_JSON_file(self, file: str, mode: str, data: Any, encoding='utf-8') -> bool:
            """Any kind of file is saved as raw data.

            Args:
                file (str): The name of the file to be saved.
                mode (str): How to save the file. You can use'w' and'wb' or'a'.
                data (Any): This is the data you want to save as a file.
                encoding (str, optional): The encoding of the file to be write. Defaults to 'utf-8'.

            Returns:

                bool: Returns whether the data was successfully saved.
            """

            data = json.dumps(data, indent='\t', ensure_ascii=False)
            flag = self.write_raw_file(file=file, mode=mode, data=data, encoding=encoding)

            return flag


if __name__ == "__main__":
    import doctest
    doctest.testmod()
