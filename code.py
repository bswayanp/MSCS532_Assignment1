def insertion_sort_descending(arr):
    """
    Sorts the input list in monotonically decreasing order
    using the Insertion Sort algorithm.


    
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements that are smaller than key
        # one position ahead to make space for key
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Example usage
if __name__ == "__main__":
    data = [8, 3, 5, 2, 9, 1, 6]
    print("Original array:", data)
    sorted_data = insertion_sort_descending(data)
    print("Sorted array (descending):", sorted_data)

