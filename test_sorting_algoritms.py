import pytest


def sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
    return arr


def sort_reverse(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
    return arr


def sort_stable(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i][0] > arr[i + 1][0]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
    return arr


def sort_stable_reverse(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i][0] < arr[i + 1][0]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
    return arr


@pytest.fixture
def test_data():
    return [3, -5, 6, 1, 8, 10, 3, 7, 12, 11]


@pytest.fixture
def test_data2():
    return [[3, 1], [-3, 1], [1, 2], [1, 1], [-8, 1], [-6, 1], [0, 2], [0, 1], [5, 1], [6, 1]]


def test_sort_decreasing(test_data):
    sorted_data = sort_reverse(test_data)
    assert sorted_data == [12, 11, 10, 8, 7, 6, 3, 3, 1, -5]


def test_sort_increasing(test_data):
    sorted_data = sort(test_data)
    assert sorted_data == [-5, 1, 3, 3, 6, 7, 8, 10, 11, 12]


def test_sort_increasing_stable(test_data2):
    sorted_data = sort_stable(test_data2)
    assert sorted_data == [[-8, 1], [-6, 1], [-3, 1], [0, 2], [0, 1], [1, 2], [1, 1], [3, 1], [5, 1], [6, 1]]


def test_sort_increasing_stable_reverse(test_data2):
    sorted_data = sort_stable_reverse(test_data2)
    assert sorted_data == [[6, 1], [5, 1], [3, 1], [1, 2], [1, 1], [0, 2], [0, 1], [-3, 1], [-6, 1], [-8, 1]]


def test_correct_data():
    with pytest.raises(TypeError):
        sort(1)
