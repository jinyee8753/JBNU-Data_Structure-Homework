import sys
import time

import numpy as np

sys.setrecursionlimit(10000)

STUDENT_ID = "학번"
STUDENT_NAME = "이름"


def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


def selection_sort(data):
    n = len(data)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data


def heap_sort(data):
    n = len(data)

    def sift_down(root, end):
        while 2 * root + 1 <= end:
            child = 2 * root + 1
            if child + 1 <= end and data[child] < data[child + 1]:
                child += 1
            if data[root] < data[child]:
                data[root], data[child] = data[child], data[root]
                root = child
            else:
                return

    for start in range(n // 2 - 1, -1, -1):
        sift_down(start, n - 1)
    for end in range(n - 1, 0, -1):
        data[0], data[end] = data[end], data[0]
        sift_down(0, end - 1)
    return data


def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        data[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        data[k] = right[j]
        j += 1
        k += 1
    return data


def quick_sort(data):
    def partition(lo, hi):
        pivot = data[hi]
        i = lo
        for j in range(lo, hi):
            if data[j] < pivot:
                data[i], data[j] = data[j], data[i]
                i += 1
        data[i], data[hi] = data[hi], data[i]
        return i

    def sort_range(lo, hi):
        while lo < hi:
            p = partition(lo, hi)
            if p - lo < hi - p:
                sort_range(lo, p - 1)
                lo = p + 1
            else:
                sort_range(p + 1, hi)
                hi = p - 1

    sort_range(0, len(data) - 1)
    return data


def built_in_sort(data):
    data.sort()
    return data


def measure(sort_func, data, expected):
    target = list(data)
    start = time.perf_counter()
    sort_func(target)
    elapsed_ms = (time.perf_counter() - start) * 1000.0
    assert target == expected, sort_func.__name__ + " produced wrong result"
    return elapsed_ms


sort_functions = [
    ("selection", selection_sort),
    ("heap", heap_sort),
    ("insertion", insertion_sort),
    ("quick", quick_sort),
    ("merge", merge_sort),
    ("python", built_in_sort),
]

data_files = ['test1.dat', 'test2.dat', 'test3.dat', 'test4.dat', 'test5.dat']
size_labels = ['500', '1K', '5K', '10K', '100K']

results = {name: [] for name, _ in sort_functions}

for f in data_files:
    data_file = open("./{0}".format(f), 'r')
    data = np.array(data_file.readlines(), dtype=np.int64).tolist()
    expected = sorted(data)
    for name, sort_func in sort_functions:
        results[name].append(measure(sort_func, data, expected))
    data_file.close()

print("Student ID: {0}  Name: {1}".format(STUDENT_ID, STUDENT_NAME))
print()
header = "{0:>9}".format("")
for label in size_labels:
    header += "  {0:>12}".format(label)
print(header)
for name, _ in sort_functions:
    row = "{0:>9}".format(name)
    for ms in np.array(results[name]):
        row += "  {0:>10.2f}ms".format(ms)
    print(row)
