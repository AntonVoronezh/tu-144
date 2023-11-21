from get_channels_by_filter.get_chanels_by_filter import get_channels_by_filter
from get_chanel_data.get_channels_data_one_by_one import get_channels_data_one_by_one
from get_path import delete_current_dir, make_current_dir

in_new_request = False

if in_new_request:
    delete_current_dir()
    make_current_dir()

# get_channels_by_filter()
get_channels_data_one_by_one()
