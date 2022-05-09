from pathlib import Path
from helpers import util
from helpers.model_saver import *
from models.config_helper import *
import json

import os

base_data_path = "../../../../data/training_pipeline_results/"
# # single model
# path_jira_dt = base_data_path + r"[7982] 2021-11-19 19_36_46_jiraset_ml_preprocess_single_balanced" + "/containers" \
#                + "/summary_Decision Tree_model_container_454821.4465781571"
# # multi model
# path_jira_rf = base_data_path + r"[7982] 2021-11-16 23_01_05_jiraset_ml_preprocess_ensemble_balanced" + "/containers" \
#                + "/description_RandomForrest_model_container_454755.3625842828"

container_path_string = r"N:\Users\Dries\projects\Risk-Assessment\code\python\training_pipeline\output\2022-05-08 12_01_34_dev_test_debug\containers\\"

def files_in_dir(path: str, with_folders = False, print_files=False):
    files_names = sorted([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) or with_folders])
    file_paths = [os.path.join(path, f) for f in files_names]
    if print_files:
        print(files_names)

    return file_paths

def main():
    containers = files_in_dir(container_path_string, with_folders=True)
    print(containers)
    first = containers[0]
    model = LoadedModel(first)
    print(model)
    # no_json = [n for n in containers if 'json' not in n]
    # for c in no_json:
    #     print_stats(c)
    # first = containers[2]
    # print(first)
    # print_stats(first)


def print_stats(path: str):
    print("loading: " + path)
    try:
        container = util.load_pickle(path)
        print(f"\nSUCCESS\n---\n{path}\n---\n")
        print(container)
    except:
        print(f"Failure\n---\n{path}\n---\n")




class LoadedModel:
    def __init__(self, path):
        files = files_in_dir(path, print_files=True)
        # files are sorted alphabetically if the folder is the generated one it should work based on the order
        self.meta = load_json(files[0])
        self.model = util.load_pickle(files[1])
        self.ordinal_encoder = util.load_pickle(files[2])
        self.scaler = util.load_pickle(files[3])
        self.standardizer = util.load_pickle(files[4])
        self.topic_analyzer = util.load_pickle(files[5])
        self.vectorizers = util.load_pickle(files[6])

    def __str__(self) -> str:
        return f"{self.meta['variation']}\n{self.model}\n{self.topic_analyzer}\n{self.vectorizers}"



def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)


if __name__ == "__main__":
    main()
