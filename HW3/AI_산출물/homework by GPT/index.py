import sys
import time

import numpy as np


sys.setrecursionlimit(300000)


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
    for i in range(len(data) - 1):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data


def heap_sort(data):
    def sift_down(start, end):
        root = start
        while True:
            child = root * 2 + 1
            if child > end:
                break
            if child + 1 <= end and data[child] < data[child + 1]:
                child += 1
            if data[root] < data[child]:
                data[root], data[child] = data[child], data[root]
                root = child
            else:
                break

    n = len(data)
    for start in range(n // 2 - 1, -1, -1):
        sift_down(start, n - 1)
    for end in range(n - 1, 0, -1):
        data[0], data[end] = data[end], data[0]
        sift_down(0, end - 1)
    return data


def merge_sort(data):
    aux = [0] * len(data)

    def sort(left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        sort(left, mid)
        sort(mid + 1, right)
        merge(left, mid, right)

    def merge(left, mid, right):
        i = left
        j = mid + 1
        k = left

        while i <= mid and j <= right:
            if data[i] <= data[j]:
                aux[k] = data[i]
                i += 1
            else:
                aux[k] = data[j]
                j += 1
            k += 1

        while i <= mid:
            aux[k] = data[i]
            i += 1
            k += 1

        while j <= right:
            aux[k] = data[j]
            j += 1
            k += 1

        for idx in range(left, right + 1):
            data[idx] = aux[idx]

    sort(0, len(data) - 1)
    return data


def quick_sort(data):
    def partition(low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            if data[j] <= pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[high] = data[high], data[i + 1]
        return i + 1

    def sort(low, high):
        if low < high:
            pivot_idx = partition(low, high)
            sort(low, pivot_idx - 1)
            sort(pivot_idx + 1, high)

    sort(0, len(data) - 1)
    return data


def built_in_sort(data):
    data.sort()
    return data


def read_data(filename):
    f = open("./{0}".format(filename), 'r')
    lines = f.readlines()
    f.close()
    return np.array([int(line.strip()) for line in lines if line.strip() != ""], dtype=np.int64).tolist()


def measure_sort(sort_func, original, expected):
    data = original.copy()
    start = time.perf_counter()
    result = sort_func(data)
    end = time.perf_counter()
    assert result == expected
    assert data == expected
    return (end - start) * 1000


def main():
    print("학번 이름")

    data_files = ['test1.dat', 'test2.dat', 'test3.dat', 'test4.dat', 'test5.dat']
    sizes = ['500', '1K', '5K', '10K', '100K']
    algorithms = [
        ('selection', selection_sort),
        ('heap', heap_sort),
        ('insertion', insertion_sort),
        ('quick', quick_sort),
        ('merge', merge_sort),
        ('python', built_in_sort),
    ]

    results = {name: [] for name, _ in algorithms}

    for filename in data_files:
        original = read_data(filename)
        expected = sorted(original)
        for name, sort_func in algorithms:
            elapsed_ms = measure_sort(sort_func, original, expected)
            results[name].append("{0:.2f}ms".format(elapsed_ms))

    print("{0:<10}".format(""), end="")
    for size in sizes:
        print("{0:>12}".format(size), end="")
    print()

    for name, _ in algorithms:
        print("{0:<10}".format(name), end="")
        for value in results[name]:
            print("{0:>12}".format(value), end="")
        print()


if __name__ == "__main__":
    main()
