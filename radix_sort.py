def counting_sort(arr, exp):
    """
    A function to perform a counting sort based on the digit represented by exp (exponent).
    
    @param arr: List of integers to be sorted.
    @param exp: The digit place (1 for units, 10 for tens, 100 for hundreds, etc.).
    """
    n = len(arr)
    output = [0] * n  # Output array that will hold the sorted values
    count = [0] * 10  # There are 10 possible digits (0 to 9)

    # Store the count of occurrences of each digit
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Change count[i] so that it contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array using the count array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the sorted elements into the original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    """
    Main function to implement Radix Sort.
    
    @param arr: List of integers to be sorted.
    """
    # Find the maximum number to determine the number of digits
    max1 = max(arr)

    # Perform counting sort for every digit. exp is 10^i, where i is the current digit number
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Example usage:
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original array:", arr)
    radix_sort(arr)
    print("Sorted array:", arr)
