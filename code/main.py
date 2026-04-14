# main.py

from fifo import simulate_fifo
from lru import simulate_lru
from round_robin import round_robin


def test_page_algorithms():
    pages = [1, 2, 3, 1, 4, 5]
    capacity = 3

    print("=== FIFO ===")
    fifo_result = simulate_fifo(pages, capacity)
    print("Page Faults:", fifo_result["page_faults"])
    print("Final Frames:", fifo_result["final_frames"])

    print("\n=== LRU ===")
    lru_result = simulate_lru(pages, capacity)
    print("Page Faults:", lru_result["page_faults"])
    print("Final Frames:", lru_result["final_frames"])


def test_round_robin():
    processes = ["P1", "P2", "P3"]
    burst_times = [10, 5, 8]
    quantum = 2

    print("\n=== Round Robin ===")
    rr_result = round_robin(processes, burst_times, quantum)

    print("Waiting Times:", rr_result["waiting_times"])
    print("Turnaround Times:", rr_result["turnaround_times"])
    print("Average Waiting Time:", rr_result["avg_waiting_time"])
    print("Average Turnaround Time:", rr_result["avg_turnaround_time"])


if __name__ == "__main__":
    test_page_algorithms()
    test_round_robin()
