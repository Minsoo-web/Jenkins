from colors import color
import time


def timer(original_func):
    """The execution time of the function is measured and the result is displayed on the screen Use it as a decorator"""

    def wrapper_func(*args, **kwargs):
        start_time: float = time.time()
        result = original_func(*args, **kwargs)
        end_time: float = time.time()
        duration = round((end_time - start_time), 2)
        print(color('Duration:', 'green'), color(f'{duration}', 'yellow'), color('seconds', 'green'), color('✔', 'cyan'), end='\n\n')
        return result
    return wrapper_func
