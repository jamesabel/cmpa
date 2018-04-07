
import os
import logging

import pytest

from test_cmpa import get_test_data_root, rmdir, mkdirs
from test_cmpa import get_test_data_root_same_single_level, get_test_data_root_same_multiple_level
from test_cmpa import get_test_data_root_different_single_level, get_test_data_root_different_multiple_level
from test_cmpa import get_test_data_root_unmatched

log = logging.getLogger()


def _write_test_file(file_path, contents):
    mkdirs(os.path.dirname(file_path))
    with open(file_path, 'w') as f:
        f.write(contents)


@pytest.fixture(scope="session", autouse=True)
def cmpa_setup():
    test_data_root = get_test_data_root()
    print('making %s' % test_data_root)
    rmdir(test_data_root)

    file_name_a = 'a.txt'
    file_name_b = 'b.txt'
    default_contents = 'xyz'

    parent_dir = get_test_data_root_same_single_level()
    _write_test_file(os.path.join(parent_dir, 'a', file_name_a), default_contents)
    _write_test_file(os.path.join(parent_dir, 'b', file_name_a), default_contents)

    parent_dir = get_test_data_root_same_multiple_level()
    _write_test_file(os.path.join(parent_dir, 'a', file_name_a), default_contents)
    _write_test_file(os.path.join(parent_dir, 'a', 's', file_name_a), default_contents)
    _write_test_file(os.path.join(parent_dir, 'a', 's', file_name_b), default_contents)
    _write_test_file(os.path.join(parent_dir, 'b', file_name_a), default_contents)
    _write_test_file(os.path.join(parent_dir, 'b', 's', file_name_a), default_contents)
    _write_test_file(os.path.join(parent_dir, 'b', 's', file_name_b), default_contents)

    parent_dir = get_test_data_root_different_single_level()
    _write_test_file(os.path.join(parent_dir, 'a', file_name_a), default_contents)
    _write_test_file(os.path.join(parent_dir, 'b', file_name_a), 'not the same')

    parent_dir = get_test_data_root_different_multiple_level()
    _write_test_file(os.path.join(parent_dir, 'a', file_name_a), default_contents)
    _write_test_file(os.path.join(parent_dir, 'a', 's', file_name_a), default_contents)
    _write_test_file(os.path.join(parent_dir, 'a', 's', file_name_b), default_contents)
    _write_test_file(os.path.join(parent_dir, 'b', file_name_a), default_contents)
    _write_test_file(os.path.join(parent_dir, 'b', 's', file_name_a), default_contents)
    _write_test_file(os.path.join(parent_dir, 'b', 's', file_name_b), 'not the same either')

    parent_dir = get_test_data_root_unmatched()
    _write_test_file(os.path.join(parent_dir, 'a', file_name_a), default_contents)

