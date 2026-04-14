from FIFO import simulate_fifo
from LRU import simulate_lru
from round_robin import round_robin


def test_page_algorithms():
    pages = [1, 2, 3, 1, 4, 5]
    capacity = 3

    print("=== FIFO ===")
    print(simulate_fifo(pages, capacity))

    print("\n=== LRU ===")
    print(simulate_lru(pages, capacity))


def test_round_robin():
    processes = ["P1", "P2", "P3"]
    burst_times = [10, 5, 8]
    quantum = 2

    print("\n=== Round Robin ===")
    print(round_robin(processes, burst_times, quantum))


if __name__ == "__main__":
    test_page_algorithms()
    test_round_robin()
