import os

from cmpa import compare_directories, CompareDirectories

from test_cmpa import get_test_data_root_same_single_level, get_test_data_root_different_single_level
from test_cmpa import get_test_data_root_different_multiple_level, get_test_data_root_same_multiple_level
from test_cmpa import get_test_data_root_unmatched


def test_cmpa():
    test_dirs = ['a', 'b']

    assert(compare_directories([os.path.join(get_test_data_root_same_single_level(), test_dir) for test_dir in test_dirs]))
    assert(compare_directories([os.path.join(get_test_data_root_same_multiple_level(), test_dir) for test_dir in test_dirs]))
    assert(not compare_directories([os.path.join(get_test_data_root_different_single_level(), test_dir) for test_dir in test_dirs]))
    assert(not compare_directories([os.path.join(get_test_data_root_different_multiple_level(), test_dir) for test_dir in test_dirs]))

    assert(compare_directories([os.path.join(get_test_data_root_same_single_level(), test_dir) for test_dir in test_dirs], file_filters=['*.txt']))
    assert(compare_directories([os.path.join(get_test_data_root_same_single_level(), test_dir) for test_dir in test_dirs], file_filters=['*.nah']))

    # use the dirs with different contents, but filter those files out
    assert(compare_directories([os.path.join(get_test_data_root_different_multiple_level(), test_dir) for test_dir in test_dirs], file_filters=['*.nah']))

    # different files
    assert(not compare_directories([os.path.join(get_test_data_root_unmatched(), test_dir) for test_dir in test_dirs]))

    cd = CompareDirectories([os.path.join(get_test_data_root_same_single_level(), test_dir) for test_dir in test_dirs])
    assert(cd.compare_ok_count == 1)
    assert(cd.compare_ok is True)
    assert(cd.get_file_counts() == [1, 1])
    assert(cd.get_total_files() == 1)

    cd = CompareDirectories([os.path.join(get_test_data_root_same_multiple_level(), test_dir) for test_dir in test_dirs])
    assert(cd.compare_ok_count == 3)
    assert(cd.compare_ok is True)
    assert(cd.get_file_counts() == [3, 3])
    assert(cd.get_total_files() == 3)