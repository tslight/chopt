# Copyright (c) 2018, Toby Slight. All rights reserved.
# ISC License (ISCL) - see LICENSE file for details.

import fnmatch
import re


def get_matches(inputs, options):
    '''
    Compares two lists.

    For each item in the first list we see how many items in the second list
    match - with globbing or number selection.

    Returns a tuple:

    The first element of which is a list of indexes of the second list that the
    first list matches.

    The second is a list of items of the first list that failed to match
    against any items in the second list.

    The third is a boolean that indicates whether or not any items in
    the first list failed to match with any items in the second.
    '''
    matches = []
    invalid = []
    failed = False

    for i in inputs:
        count = 0
        total = len(options)
        for j in options:
            index = options.index(j)
            number = index + 1
            number = str(number)
            regex = fnmatch.translate(str(i))  # convert globs to regex
            if re.match(regex, j) or re.match(regex, number):
                matches.append(index)
            else:
                count += 1

        # if we failed to match an input against any of the options.
        if count == total:
            invalid.append(i)
            failed = True

    return matches, invalid, failed
