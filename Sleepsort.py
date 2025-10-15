
import time
import threading

def sleep_sort(numbers):
    """
    Sorts a list of positive numbers using the Sleep Sort algorithm.
    WARNING: This is a conceptual and impractical algorithm. Do not use
    it for serious applications. It may not work reliably and is
    inefficient for large numbers or lists.
    """
    sorted_result = []

    def sleep_and_append(num):
        # The number determines the sleep duration
        # We divide by a factor to make it run faster for the example
        time.sleep(num / 100) 
        sorted_result.append(num)

    threads = []
    for num in numbers:
        # Create and start a new thread for each number
        thread = threading.Thread(target=sleep_and_append, args=(num,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete their sleep and append cycle
    for thread in threads:
        thread.join()
        
    return sorted_result

# --- Example Usage ---
my_numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {my_numbers}")

# Note: The output is printed as it's being "sorted" by time.
sorted_numbers = sleep_sort(my_numbers)
print(f"Sorted:   {sorted_numbers}")
