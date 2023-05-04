
""")
# t0=time.time()
program = get_program("assembly(robot)")
# t1 = time.time()

print("--- %s seconds ---" % (t1 - t0))
# print (program)
if check(program):
    print("Well done. The program is correct.")

if not check(program):
    print("I am sorry. There seems to be a problem with the program. Please try again.")
[eod] [code]from typing import List, Optional
from functools import lru_cache


def binary_search_left(
    arr: List, target: int, start: int = 0, end: Optional[int] = None
) -> int:
    """
    二分搜索的左边界
    """
    end = end if end is not None else len(arr)
    i = start
    while i < end:
        middle = (start + end) >> 1
        if arr[middle] >= target:
            end = middle
        else:
            start = middle + 1
        i = start
    return start - 1


def binary_search_right(
    arr: List, target: int, start: int = 0, end: Optional[int] = None
) -> int:
    """
    二分搜索的右边界
    """
    end = end if end is not None else len(arr)
    i = start
    while i < end:
        middle = (start + end) >> 1
        if arr[middle] <= target:
            start = middle + 1
        else:
            end = middle
        i = start
    return end - 1


@lru_cache(maxsize=None)
def binary_search_left_with_memo(
    arr: List, target: int, start: int = 0, end: Optional[int] = None
) -> int:
    """
    二分搜索的左边界
    """
    end = end if end is not None else len(arr)
    i = start
    while i < end:
        middle = (start + end) >> 1
        if arr[middle] >= target:
            end = middle
        else:
            start = middle + 1
        i = start
    return start - 1


@lru_cache(maxsize=None)
def binary_search_right_with_memo(
    arr: List, target: int, start: int = 