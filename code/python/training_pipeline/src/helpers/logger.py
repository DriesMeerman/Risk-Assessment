import os
from enum import Enum
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


class Verbosity(Enum):
    error = 1
    warning = 2
    info = 3
    debug = 4


BASE_FOLDER = "output/"


class Logger:
    current_run = None

    def __init__(self, verbosity=Verbosity.info, markdown=False, output_file=None, img_format='png') -> None:
        self.verbosity = Verbosity(verbosity) if isinstance(verbosity, int) else verbosity
        self.markdown_mode = markdown
        self.output_file = output_file
        self.img_format = img_format

    def df(self, frame):
        if not isinstance(frame, pd.DataFrame):
            frame = pd.DataFrame(frame)

        self.info("\n")
        self.info(frame.to_markdown(), "\n\n")

    def csv(self, frame: pd.DataFrame, name: str, extra="csv/"):
        file_path = self.get_file_path(name, extra)
        frame.to_csv(file_path)

    def list(self, data):
        self.__print("[")
        for item in data:
            self.__print(item, ",")
        self.__print("]")

    def log_img(self, name: str, file_format=None):
        if file_format is None:
            file_format = self.img_format
        print(f"saving: {name} as {file_format}")
        file_path = self.get_file_path(f"{name}.{file_format}")
        plt.savefig(file_path, bbox_inches='tight', format=file_format)
        # self.debug(f"Saving: {file_path}")
        plt.clf()
        plt.close()
        self.info(f"![{name}]({name}.{file_format})")

    def get_file_path(self, name, extra=None):
        if Logger.current_run is not None:
            subfolder = Logger.current_run
        else:
            subfolder = None
        folder = BASE_FOLDER + subfolder if subfolder is not None else BASE_FOLDER
        if extra is not None:
            folder = folder + extra
        Path(folder).mkdir(parents=True, exist_ok=True)
        file_path = Path(folder + name).resolve()
        return file_path

    def set_verbosity(self, v: Verbosity):
        self.verbosity = v

    def debug(self, *args):
        if self.verbosity.value >= 4:
            self.__print(*args)

    def info(self, *args):
        if self.verbosity.value >= 3:
            self.__print(*args)

    def warning(self, *args):
        if self.verbosity.value >= 2:
            self.__print(*args)

    def error(self, *args):
        if self.verbosity.value >= 1:
            self.__print(*args)

    def is_info(self):
        return self.verbosity.value >= 3

    def __print(self, *args):
        if self.output_file is not None:
            file_path = self.get_file_path(self.output_file)
            if os.path.exists(file_path):
                write_type = "a"
            else:
                write_type = "w"

            with open(file_path, write_type) as file:
                if self.markdown_mode:
                    print(*args, file=file, end='  \n')
                else:
                    print(*args, file=file)

                file.close()
        else:
            if not self.markdown_mode:
                print(*args)
            else:
                print(*args, "  ")
