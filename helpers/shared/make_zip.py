import os
import shutil

from get_path import realpath, result_folder_name
from settings.main import current_result_for


def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def make_zip():
    dest_path = os.path.join(realpath, result_folder_name, current_result_for)
    shutil.make_archive(current_result_for, 'zip', dest_path)

    source_path = os.path.join(realpath, f'{current_result_for}.zip')
    source_path_2 = os.path.join(realpath, result_folder_name, f'{current_result_for}.zip')
    shutil.copy(source_path, source_path_2)

    os.remove(source_path)
