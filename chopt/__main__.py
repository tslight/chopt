# Copyright (c) 2018, Toby Slight. All rights reserved.
# ISC License (ISCL) - see LICENSE file for details.

import os


def getargs():
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Choose Options from a list.')
    parser.add_argument("options", nargs='+', help="Options for the menu.")
    return parser.parse_args()


def main():
    from .chopt import chopt
    from columns import prtcols
    args = getargs()
    options = args.options
    chosen = chopt(options)
    os.system('cls') if os.name == 'nt' else os.system('clear')
    if chosen:
        print("\nChosen items:\n")
        prtcols(chosen, 6)
        print()
    else:
        print("\nNothing to see here.\n")


if __name__ == '__main__':
    main()
