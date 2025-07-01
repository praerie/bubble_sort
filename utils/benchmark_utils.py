import time

def time_sorting(algorithm, data):
    """
    Measures how long it takes to sort 'data' using 'algorithm'.

    Parameters:
        algorithm (function): Sorting function
        data (list): Input list to sort

    Returns:
        float: Duration in milliseconds
    """
    start = time.perf_counter()  # perf_counter() always returns float value of time in seconds
    algorithm(data)
    end = time.perf_counter()
    return (end - start) * 1000  # milliseconds
