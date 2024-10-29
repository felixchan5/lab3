print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1

def bubble_sort(arr, sorting_order):
    # Check for non-integer values
    if any(not isinstance(i, int) for i in arr):
        return 2  

    # Check if array is empty
    if len(arr) == 0:
        return 0  

    # Check if array has 10 or more numbers
    if len(arr) >= 10:
        return 1  

    arr_result = arr.copy()
    n = len(arr_result)

    # Sort array based on sorting order
    if sorting_order == SORT_ASCENDING:
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr_result[j] > arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
    elif sorting_order == SORT_DESCENDING:
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr_result[j] < arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
    else:
        # Invalid sorting order, return an empty list
        return []

    return arr_result

def main():
    # Driver code to test the above
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Sort in descending order
    print("Sorted array in descending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)

if __name__ == "__main__":
    main()
