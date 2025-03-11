import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def bubble_sort(arr):
    """Bubble Sort with animation frames"""
    frames = []
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            frames.append(arr.copy())
    return frames

def selection_sort(arr):
    """Selection Sort with animation frames"""
    frames = []
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        frames.append(arr.copy())
    return frames

def insertion_sort(arr):
    """Insertion Sort with animation frames"""
    frames = []
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            frames.append(arr.copy())
        arr[j + 1] = key
        frames.append(arr.copy())
    return frames

def merge_sort(arr):
    """Merge Sort with animation frames"""
    frames = []
    def merge(arr, left, mid, right):
        left_half = arr[left:mid + 1]
        right_half = arr[mid + 1:right + 1]
        i = j = 0
        k = left

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            frames.append(arr.copy())
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            frames.append(arr.copy())

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            frames.append(arr.copy())

    def merge_sort_recursive(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_recursive(arr, left, mid)
            merge_sort_recursive(arr, mid + 1, right)
            merge(arr, left, mid, right)

    merge_sort_recursive(arr, 0, len(arr) - 1)
    return frames

def quick_sort(arr):
    """Quick Sort with animation frames"""
    frames = []
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            frames.append(arr.copy())
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        frames.append(arr.copy())
        return i + 1

    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)

    quick_sort_recursive(arr, 0, len(arr) - 1)
    return frames

def visualize_sorting(frames, sort_name):
    """Visualizes sorting animation"""
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(frames[0])), frames[0], color="blue")

    def update(frame):
        for bar, height in zip(bars, frame):
            bar.set_height(height)
        ax.set_title(f"{sort_name} Sorting")

    ani = animation.FuncAnimation(fig, update, frames=frames, repeat=False, interval=100)
    ani.save(f"{sort_name.lower()}_sort.gif", writer="pillow")
    plt.show()

def main():
    """Main function to run sorting visualizer"""
    size = int(input("Enter array size: "))
    algorithm = input("Choose sorting algorithm (bubble, selection, insertion, merge, quick): ").strip().lower()

    arr = np.random.randint(10, 10000, size).tolist()

    if algorithm == "bubble":
        frames = bubble_sort(arr)
    elif algorithm == "selection":
        frames = selection_sort(arr)
    elif algorithm == "insertion":
        frames = insertion_sort(arr)
    elif algorithm == "merge":
        frames = merge_sort(arr)
    elif algorithm == "quick":
        frames = quick_sort(arr)
    else:
        print("Invalid algorithm name!")
        return

    visualize_sorting(frames, algorithm.capitalize())
    print(f"Sorting animation saved as {algorithm}_sort.gif")

if __name__ == "__main__":
    main()