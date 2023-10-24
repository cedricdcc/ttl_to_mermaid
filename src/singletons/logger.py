import inspect
import logging


class SingletonLogger(logging.Logger):
    _instance = None
    __initialized = False

    def __init__(self, name=None, level=logging.DEBUG):
        if not self.__initialized:
            self.__initialized = True
            super().__init__(name=name, level=level)
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)
            
            file_handler = logging.FileHandler('logs.txt', mode='w')
            file_handler.setLevel(level)
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            console_handler.setFormatter(formatter)
            file_handler.setFormatter(formatter)
            self.addHandler(console_handler)
            self.addHandler(file_handler)


def get_logger():
    # Get the name of the calling module
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    module_name = module.__name__

    # Create a logger instance with the module name as its name
    logger = SingletonLogger(module_name)
    return logger
