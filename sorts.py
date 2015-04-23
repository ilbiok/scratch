#!/usr/bin/python3

import random

######## Bubble Sort ##########################################################


def chris_bubble_sort(values):
    modified = True
    while modified:
        modified = False
        for i in range(1, len(values)):
            if values[i - 1] > values[i]:
                values[i], values[i - 1] = values[i - 1], values[i]
                modified = True
    return values


def peter_bubble_sort(nums):
    count = 0
    # XXX: Chris added this to stop infinite loop on inputs of lenth 1.
    if len(nums) == 1:
        return nums
    while count < len(nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                count = 0
            count += 1
    return nums

######## Select Sort ##########################################################


def chris_select_sort(values):
    result = []
    while values:
        value = min(values)
        values.remove(value)
        result.append(value)
    return result


def peter_select_sort(nums):
    newlist = []
    while len(newlist) < nums:
        newlist.append(min(nums))
        nums.remove(min(nums))
        if len(nums) == 0:
            nums.append(newlist)
            break
    return newlist

######## Insert Sort ##########################################################


class Link(object):
    def __init__(self, value, nextval=None):
        self.value = value
        self.nextval = nextval


def chris_insert_sort(values):
    # Test for empty input.
    if not values:
        return values
    # Build sorted linked list from input using Link class.
    head = Link(values[0])
    for value in values[1:]:
        if value < head.value:
            head = Link(value, head)
        else:
            current = head
            while True:
                if current.nextval is None or value < current.nextval.value:
                    current.nextval = Link(value, current.nextval)
                    break
                current = current.nextval
    # Copy sorted linked list into Python list.
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.nextval
    return values


def peter_insert_sort(values):
    # TODO: Test for empty input.
    # TODO: Build sorted linked list from input using Link class.
    # TODO: Copy sorted linked list into Python list.
    pass

######## Test Sort Functions ##################################################


def shuffle_sort(values):
    '''
    This has O(n) complexity!!!
    But is statistically unlikely to ever be correct for long inputs.
    '''
    random.shuffle(values)
    return values


def test_sort_func(sort_func):
    for i in range(20):
        test_input = list(range(i - 1, -1, -1))
        result = sort_func(test_input[:])
        if result != list(range(i)):
            raise Exception('sorted {} as {}'.format(test_input, result))


if __name__ == '__main__':
    for name, sort_func in [('sorted', sorted),
                            ('shuffle_sort', shuffle_sort),
                            ('chris_bubble_sort', chris_bubble_sort),
                            ('peter_bubble_sort', peter_bubble_sort),
                            ('chris_select_sort', chris_select_sort),
                            ('peter_select_sort', peter_select_sort),
                            ('chris_insert_sort', chris_insert_sort),
                            ('peter_insert_sort', peter_insert_sort)]:
        print('Testing {}'.format(name))
        try:
            test_sort_func(sort_func)
            print('  Pass!')
        except Exception as exception:
            print('  Fail! {}'.format(exception))
