# Copyright (c) 2018, Toby Slight. All rights reserved.
# ISC License (ISCL) - see LICENSE file for details.

import re


def insert_range(element, inputs, options, nums):
    '''
    Remove element of original list that defines range, then insert integers in
    the range of the first and last elements of a list created by the defining
    element of original list back into original list.
    '''
    # catch attempts to mark outside options
    if len(options) >= nums[len(nums) - 1]:
        inputs.remove(element)
        for n in range(nums[0], nums[len(nums) - 1] + 1):
            # append after remove, means we'll end up skipping the next
            # element, and we don't need to iterate over added elements.
            inputs.insert(0, str(n))
    return inputs


def get_ranges(inputs, options):
    '''
    Find any numeric ranges in a list. A numeric range is defined as two
    numbers separated either by two periods or a dash.

    If we find a numeric range element, use list comprehension to extract the
    integers, remove the original element, and then insert a new element for
    every number in that range back into the original list.
    '''
    for i in inputs:
        if re.match('^\\d+\\.\\.\\d+$', i):
            nums = [int(n) for n in i.split("..") if n.isdigit()]
            inputs = insert_range(i, inputs, options, nums)
        elif re.match('^\\d+\\.\\.$', i):
            nums = [int(n) for n in i.split("..") if n.isdigit()]
            nums.append(len(options))
            inputs = insert_range(i, inputs, options, nums)
        elif re.match('^\\.\\.\\d+$', i):
            nums = [int(n) for n in i.split("..") if n.isdigit()]
            nums.insert(0, 1)
            inputs = insert_range(i, inputs, options, nums)
        elif re.match('^\\d+-\\d+$', i):
            nums = [int(n) for n in i.split("-") if n.isdigit()]
            inputs = insert_range(i, inputs, options, nums)
        elif re.match('^\\d+-$', i):
            nums = [int(n) for n in i.split("-") if n.isdigit()]
            nums.append(len(options))
            inputs = insert_range(i, inputs, options, nums)
        elif re.match('^-\\d+$', i):
            nums = [int(n) for n in i.split("-") if n.isdigit()]
            nums.insert(0, 1)
            inputs = insert_range(i, inputs, options, nums)
    return inputs
