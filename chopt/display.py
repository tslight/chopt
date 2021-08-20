# Copyright (c) 2018, Toby Slight. All rights reserved.
# ISC License (ISCL) - see LICENSE file for details.

import os
from textwrap import dedent, fill
from columns import prtcols


def prtheader():
    width = os.get_terminal_size()[0]
    head = '''
           Enter option names (wildcards accepted), or numbers (ranges accepted),
           to toggle selections.
           '''
    keys = '(t)oggle all, (r)esets, (a)ccept choices, (q)uit'
    msg = dedent(head).strip()
    print("\n" + fill(msg, width=width) + "\n\n" + keys + "\n")


def menu(options, chosen):
    '''
    Takes a list of options and selections as an argument and presents a
    checkbox menu with previously selected items still selected.
    '''
    optstrs = []
    os.system('cls') if os.name == 'nt' else os.system('clear')
    prtheader()
    for option in options:
        index = options.index(option)
        # print("{0:>1} {1:>2}) {2:}".format(chosen[index], index+1,  option))
        optstrs.append(chosen[index] + str(index + 1) + ") " + option)
    prtcols(optstrs, 10)
