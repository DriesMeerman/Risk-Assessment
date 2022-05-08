import math
import pickle

from pathlib import Path
import matplotlib.pyplot as plt
import arrow
import yaml

from joblib import dump, load


def field_getter(input_field):
    parts = input_field.split('.')
    field = parts[0]
    field_display = 'value'

    if len(parts) > 1:
        field_display = parts[1]

    def getter(item):
        return item[field][field_display]

    return getter


def sn_string_to_bool(input):
    bool_map = {
        '1': True,
        't': True,
        'true': True,
        'True': True,
        '0': False,
        'f': False,
        'false': False,
        'False': False,
        '': False
    }

    return bool_map[input]


def compose(fx, fy):
    return lambda x: fy(fx(x))


def days_between(a: str, b: str) -> int:
    date1 = arrow.get(a)
    date2 = arrow.get(b)
    diff = date2 - date1
    DAY_SECONDS = 24 * 60 * 60

    return diff.total_seconds() / DAY_SECONDS


def seconds_humanized(duration):
    minutes, seconds = divmod(duration, 60)
    hours, minutes = divmod(minutes, 60)
    exact = "HH:{:.2f} \tMM:{:.2f} \t ss:{:.2f}".format(hours, minutes, seconds)
    human = "{:0>2}:{:0>2}:{:0>2}".format(round(hours), math.ceil(minutes), math.ceil(seconds))
    return exact, human


def print_seconds_humanized(duration, logger=None):
    text = "Total seconds: {}:  \nExact: {}  \nTime: {}".format(duration, *seconds_humanized(duration))
    if logger is None:
        print(text)
    else:
        logger.info(text)


# https://www.geeksforgeeks.org/python-difference-two-lists/
def list_diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))


def build_config(base, overrides):
    return {**base, **overrides}


PICKLE_FOLDER = "output/"
IMG_FOLDER = "output/"


def pickle_make(file: str, thing, subfolder=None, folder_override=None):
    file = file + ".joblib"
    file_path = path_helper(file, subfolder, folder_override)
    dump(thing, file_path)


def path_helper(file: str, subfolder=None, folder_override=None):
    folder = PICKLE_FOLDER + subfolder if subfolder is not None else PICKLE_FOLDER
    if folder_override is not None:
        folder = folder_override

    Path(folder).mkdir(parents=True, exist_ok=True)  # make the pickles folder if not exists
    file_path = Path(folder + file).resolve()
    return file_path


def save_fig(name: str, subfolder=None, logger=None):
    folder = IMG_FOLDER + subfolder if subfolder is not None else IMG_FOLDER
    Path(folder).mkdir(parents=True, exist_ok=True)
    file_path = Path(folder + name).resolve()

    name = name.replace(" ", "_")

    if logger is None:
        print(f"Saving: {file_path}")
        print(f"![{name}]({name})")
    else:
        logger.debug(f"Saving: {file_path}")
        logger.info(f"![{name}]({name})")

    plt.savefig(file_path, bbox_inches='tight')


def load_pickle(file: str):
    file_path = Path(file).resolve()
    return load(file_path)


def load_yaml(file: str):
    file_path = Path(file).resolve()
    with open(file_path, "r") as fp:
        return yaml.safe_load(fp)


def flatten_list(meta_list):
    res = []
    for l in meta_list:
        res = res + l
    return res


def now_timestring():
    return arrow.utcnow().format('YYYY-MM-DD HH:mm:ss')
