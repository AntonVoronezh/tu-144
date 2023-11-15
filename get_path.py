import os
import shutil

from settings.main import current_result_for

result_folder_name = '1results'
setting_folder_name = 'settings'
tmp_folder_name = 'tmp'

realpath = os.path.dirname(os.path.realpath(__file__))
result_path = os.path.join(realpath, result_folder_name, current_result_for)
result_tmp_path = os.path.join(realpath, result_folder_name, tmp_folder_name)
setting_path = os.path.join(realpath, setting_folder_name, current_result_for)


def make_current_dir():
    if not os.path.isdir(result_path):
        os.mkdir(result_path)
    if not os.path.isdir(result_tmp_path):
        os.mkdir(result_tmp_path)


def delete_current_dir():
    if os.path.isdir(result_path):
        shutil.rmtree(result_path)


def clear_tmp_dir():
    if os.path.isdir(result_tmp_path):
        shutil.rmtree(result_tmp_path)
        os.mkdir(result_tmp_path)