
import argparse
import sys

from cmpa import __title__

from balsa import get_logger, Balsa

from cmpa import Compare, __version__, __author__

log = get_logger(__title__)


def main():

    epilog = """
    cmpa - directory compare (by abel.co)

    Prints the result of the directory comparison.  Only the differences and the summary flag will be printed, unless 
    verbose is given (or if silent given then nothing will be printed). 

    - means extra files in first directory
    + means extra files in second directory
    ! means file contents mismatch
    = equality flag
    s summary

    process returns 1 if any mis-compares
    """

    parser = argparse.ArgumentParser(epilog=epilog, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('directories', nargs=2, help='two directories to compare')
    parser.add_argument('-f', '--filters', nargs='*', default=['*'], help='file filters')
    parser.add_argument('-e', '--exclude', nargs='*', default=[], help='exclude directories that start with these name(s)')
    parser.add_argument('-s', '--silent', action='store_true', help='do not print')
    parser.add_argument('-t', '--text', action='store_true', help='text based compare that ignores CR/LF differences')
    parser.add_argument('-i', '--image', action='store_true', help='image based compare')
    parser.add_argument('--version', action='store_true', help='display version')
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose')
    args = parser.parse_args()

    balsa = Balsa(__title__, __author__)
    balsa.init_logger_from_args(args)

    if args.version:
        print(__version__)

    cd = Compare(args.directories, args.filters, args.silent, args.text, args.exclude, args.verbose)
    sys.exit(int(not cd.compare_ok_all))  # 0 is all compared OK, 1 otherwise


if __name__ == '__main__':
    main()
