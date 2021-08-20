# Copyright (c) 2018, Toby Slight. All rights reserved.
# ISC License (ISCL) - see LICENSE file for details.

import re
import readline
from .display import menu
from .ranges import get_ranges
from .matches import get_matches
from .mark import mark, chkmrk


def chopt(options):
    '''
    Takes a list of options as an argument and returns a list of selected
    options from that list.
    '''
    # initialize chosen to be same length as options but with empty items
    chosen = ["   "] * len(options)
    markall = False
    output = ""

    while True:
        failed = False

        menu(options, chosen)

        if output:
            print(output)

        # get list of inputs split on spaces
        inputs = input("\n----> ").split(" ")

        if re.match('^t(oggle)?$', inputs[0], re.IGNORECASE):
            if markall:
                for o in options:
                    chosen[options.index(o)] = "   "
            else:
                for o in options:
                    chosen[options.index(o)] = " + "
        elif re.match('^r(eset)?$', inputs[0], re.IGNORECASE):
            for o in options:
                chosen[options.index(o)] = "   "
        elif re.match('^a(ccept)?$', inputs[0], re.IGNORECASE):
            # list comprehension that returns all chosen options
            return [o for o in options if chosen[options.index(o)] == " + "]
        elif re.match('^q(uit)?$', inputs[0], re.IGNORECASE):
            return
        else:
            inputs = get_ranges(inputs, options)
            matched, invalid, failed = get_matches(inputs, options)
            chosen = mark(matched, chosen)

        markall = chkmrk(options, chosen)

        if failed:
            fmt = "\nINVALID INPUTS: {}"
            msg = ", ".join(invalid)
        else:
            fmt, msg = ("",)*2

        output = fmt.format(msg)
