import shutil
import os
import csv


def create_dir(dir_name: str) -> str:
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    return dir_name


def create_copy_dataset(dir_copy: str, annotation_name: str) -> None:
    create_dir(dir_copy)
    for dataset_item in os.listdir("dataset"):
        files_list = os.listdir(os.path.join("dataset", dataset_item))
        for file_name in files_list:
            shutil.copy(os.path.join(os.path.join("dataset", dataset_item),
                        file_name), os.path.join(dir_copy, f"{dataset_item}_{file_name}"))
        with open(os.path.join(dir_copy, annotation_name), mode="a", encoding="UTF-16", newline='') as file:
            file_writer = csv.writer(file, delimiter=",")
            for file_name in files_list:
                file_writer.writerow([f"{dataset_item}_{file_name}", dataset_item])


create_copy_dataset("dataset_copy", "annotation.csv")
