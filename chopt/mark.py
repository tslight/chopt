# Copyright (c) 2018, Toby Slight. All rights reserved.
# ISC License (ISCL) - see LICENSE file for details.


def mark(matched, chosen):
    '''
    Populate list of chosen options based on output of get_matches
    '''
    for m in matched:
        if chosen[m] == " + ":
            chosen[m] = "   "
        elif chosen[m] == "   ":
            chosen[m] = " + "
    return chosen


def chkmrk(options, chosen):
    '''
    Check if all options are chosen or not.
    '''
    for o in options:
        if chosen[options.index(o)] == "   ":
            return False
    return True
