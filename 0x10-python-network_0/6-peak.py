#!/usr/bin/python3
""" a function to find an element in list whose neighbors are both < it"""


def find_peak(list_of_integers):
    """ function using recursion """
    nums = list_of_integers

    if len(nums) == 0 or nums is None:
        return None

    if (len(nums) == 1):
        return (nums[0])

    if nums[0] > nums[1]:
        return nums[0]
    if nums[-1] > nums[-2]:
        return nums[-1]

    middle = len(nums) // 2

    if (nums[middle - 1] > nums[middle]):
        return(find_peak(nums[:middle]))
    elif (nums[middle + 1] > nums[middle]):
        return(find_peak(nums[middle + 1:]))
    else:
        return(nums[middle])
