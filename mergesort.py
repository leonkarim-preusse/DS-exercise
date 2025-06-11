import matplotlib.pyplot as plt


def merge_sort(numbers):
    """
    Sorts a list of numbers in ascending order using merge sort algorithm.

    Parameters:
        numbers (list): List of integers to sort. Modified in place.

    Returns:
        None
    """
    if len(numbers) <= 1:
        return

    mid_index = len(numbers) // 2
    left = numbers[:mid_index]
    right = numbers[mid_index:]

    merge_sort(left)
    merge_sort(right)

    left_index = 0
    right_index = 0
    merged_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            numbers[merged_index] = left[left_index]
            left_index += 1
        else:
            numbers[merged_index] = right[right_index]
            right_index += 1
        merged_index += 1

    while left_index < len(left):
        numbers[merged_index] = left[left_index]
        left_index += 1
        merged_index += 1

    while right_index < len(right):
        numbers[merged_index] = right[right_index]
        right_index += 1
        merged_index += 1
        
if __name__ == "__main__":
    sample_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    plt.plot(range(len(sample_list)), sample_list)
    plt.title("Vorher")
    plt.show()

    merge_sort(sample_list)

    plt.plot(range(len(sample_list)), sample_list)
    plt.title("Nachher")
    plt.show()

