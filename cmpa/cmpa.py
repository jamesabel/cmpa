
import os
import filecmp
from glob import glob
import difflib

from cmpa import __title__

from balsa import get_logger

log = get_logger(__title__)


def _cmpa_print(print_string, output_flag):
    log.info(print_string)
    if output_flag:
        print(print_string)


def _text_compare(left_file_path, right_file_path, print_diffs):
    """
    do a text comparison of two files, ignoring CR/LF differences
    :param left_file_path: path to the 'left' file
    :param right_file_path: path to the 'right' file
    :return: True if files have the same textual contents, False if they are not
    """
    lines = {}
    for path_number, file_path in enumerate([left_file_path, right_file_path]):
        file_lines = []
        with open(file_path) as f:
            for line in f.readlines():
                line = line.strip()
                if len(line) > 0:
                    file_lines.append(line)
        lines[path_number] = file_lines
    are_equal = (lines[0] == lines[1])
    if not are_equal and print_diffs:
        print(''.join(difflib.context_diff(lines[0], lines[1], fromfile=left_file_path, tofile=right_file_path)))
    return are_equal


class Compare:
    def __init__(self, directories, file_filters=['*'], silent=False, text_mode=False, excludes=[], verbose=False):
        self.directories = directories
        self.file_filters = file_filters
        self.silent = silent
        self.text_mode = text_mode
        self.excludes = excludes
        self.verbose = verbose
        self.file_sets = {0: set(), 1: set()}

        assert (len(self.directories) == 2)
        log.info('comparing : %s' % self.directories)
        log.info('filters : %s' % self.file_filters)

        self.compare_ok_all = True
        self.compare_ok_count = 0

        for dir_index, directory in enumerate(self.directories):
            file_paths = set()
            for file_filter in self.file_filters:
                for p in (glob(os.path.join(directory, '**', file_filter), recursive=True)):
                    if os.path.isfile(p):
                        partial_path = p.replace(directory, '', 1)[1:]
                        if not any([partial_path.startswith(exclude) for exclude in excludes]):
                            file_paths.add(partial_path)  # just the partial paths
                self.file_sets[dir_index] = file_paths

        # prefix signifies which dir has the 'extra' file(s)
        diff_type_character = {0: '-', 1: '+'}
        for dir_index, directory in enumerate(self.directories):
            log.info('%d files in "%s"' % (len(self.file_sets[dir_index]), directory))
            diff = self.file_sets[dir_index % 2] - self.file_sets[(dir_index + 1) % 2]
            for file_path in diff:
                self.compare_ok_all = False
                _cmpa_print('%s,"%s"' % (diff_type_character[dir_index], file_path), not self.silent)

        for partial_path in self.file_sets[0].intersection(self.file_sets[1]):
            path_a = os.path.join(self.directories[0], partial_path)
            path_b = os.path.join(self.directories[1], partial_path)
            if filecmp.cmp(path_a, path_b) or (self.text_mode and _text_compare(path_a, path_b, self.verbose)):
                self.compare_ok_count += 1
                _cmpa_print('=,"%s","%s"' % (path_a, path_b), self.verbose)
            else:
                # ! for contents not equal
                _cmpa_print('!,"%s","%s"' % (path_a, path_b), not self.silent)
                self.compare_ok_all = False

        if not self.silent:
            print('f,%d,%d' % (self.get_total_files(), self.compare_ok_count))

        # 's'=summary - False if any differences, True otherwise
        _cmpa_print('s,%s' % self.compare_ok_all, not self.silent)

    def get_total_files(self):
        return len(set.union(*[fs for fs in self.file_sets.values()]))

    def get_file_counts(self):
        """
        get the file counts of each of the directories as a 2-valued list
        :return: a 2 values list of file counts
        """
        return [len(fs) for fs in self.file_sets.values()]


def compare(directories, file_filters=['*'], silent=False, text_mode=False, excludes=[], verbose=False):
    cd = Compare(directories, file_filters, silent, text_mode, excludes, verbose)
    return cd.compare_ok_all
