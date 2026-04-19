# FIFO & LRU vs. Round Robin
Team members:
Cameron Bailey, Bryant Peden

Efficient resource management is a critical function of operating systems. This project analyzes and compares the performance of two page replacement algorithms and one CPU scheduling algorithm.

The goal is to evaluate how different algorithms handle:
Memory management (page replacement) and 
CPU scheduling (process execution)

We focus on measuring efficiency using:
Page faults (for memory algorithms) and 
Waiting time and turnaround time (for scheduling)

Algorithms used in project:

FIFO (First In First Out) - replaces the oldest page in memory.
LRU (Least Recently Used) - Replaces the Page that has not been used for the longest time.
Round Robin Scheduling - Allocates CPU time in fixed time slices (or quantums) in a cyclic order.

This project uses synthetic datasets generated within the code:

Page Reference String - [1, 2, 3, 1, 4, 5]
Frame Capacity - 3
Processes - ["P1", "P2", "P3"]
Burst Times - [10, 5, 8]
Time Quantum - 2

To run this project, clone the repository with the following code:

git clone LRU_FIFO_vs_Round_Robin / 
cd code / 
python main.py
