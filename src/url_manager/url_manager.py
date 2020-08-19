import re


URL_PATTERN = r'https?://[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:?[0-9]{0,5}'


class UrlFinder(object):
    """This class finds a URL in a string.
    """

    def find(self, data: str) -> str:
        """This function checks if the URL exists in the input string.\n
        :param str data: The string to find the URL for.\n
        :raises Exception: The URL does not exist or an unexpected error occurred.\n
        :returns: If the URL is not found, it returns an empty string, otherwise it returns the URL found.
        """

        try:
            res = re.search(URL_PATTERN, data).group()
        except Exception:
            res = ''
        finally:
            return res


class UrlChanger(object):
    """This class replaces the old URL with the new one.
    """

    def change(self, old_url: str, new_url: str, data: str) -> str:
        """This function finds the URL you want to replace in the input string and converts it to a new URL.\n
        :param str old_url: This is the current URL you want to change.\n
        :param str new_url: This is the new URL you want to change.\n
        :param str data: The entire string you want to change the URL for.\n
        :raises Exception: The URL does not exist or an unexpected error occurred.\n
        :returns: Returns the entire string with the URL changed.
        """

        data = re.sub(old_url, new_url, data)
        return data


if __name__ == "__main__":
    finder = UrlFinder()
    changer = UrlChanger()
