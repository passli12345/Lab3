print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1

def bubble_sort(arr, sorting_order):
    # REQ-05: Return 2 if any value is not an integer
    if not all(isinstance(x, int) for x in arr):
        return 2

    # REQ-04: Return 0 if list is empty
    if len(arr) == 0:
        return 0

    # REQ-03: Return 1 if list has 10 or more integers
    if len(arr) >= 10:
        return 1

    # REQ-01 & REQ-02: Sort list based on sort_order
    arr_result = arr.copy()
    n = len(arr_result)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if sorting_order == SORT_ASCENDING:
                if arr_result[j] > arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
            elif sorting_order == SORT_DESCENDING:
                if arr_result[j] < arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
            else:
                return []  # Invalid sort order

    return arr_result

def main():
    arr = [64, 34, 25, 12, 22, 11, 90]

    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order:")
    print(result)

    result = bubble_sort(arr, SORT_DESCENDING)
    print("Sorted array in descending order:")
    print(result)

if __name__ == "__main__":
    main()
