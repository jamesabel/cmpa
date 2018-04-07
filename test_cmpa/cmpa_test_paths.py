
import os


def get_test_root():
    return 'test_cmpa'


def get_test_data_root():
    return os.path.join(get_test_root(), 'data')


def get_test_data_root_same_single_level():
    return os.path.join(get_test_data_root(), 'same_single')


def get_test_data_root_same_multiple_level():
    return os.path.join(get_test_data_root(), 'same_multiple')


def get_test_data_root_different_single_level():
    return os.path.join(get_test_data_root(), 'different_single')


def get_test_data_root_different_multiple_level():
    return os.path.join(get_test_data_root(), 'different_multiple')


def get_test_data_root_unmatched():
    return os.path.join(get_test_data_root(), 'unmatched')
