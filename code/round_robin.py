def round_robin(processes, burst_times, quantum):

    if __name__ == "__main__":
    processes = ["P1", "P2", "P3"]
    burst_times = [10, 5, 8]
    quantum = 2

    result = round_robin(processes, burst_times, quantum)

    print("Waiting Times:", result["waiting_times"])
    print("Turnaround Times:", result["turnaround_times"])
    print("Average Waiting Time:", result["avg_waiting_time"])
    print("Average Turnaround Time:", result["avg_turnaround_time"])

    n = len(processes)
    remaining_times = burst_times.copy()
    waiting_times = [0] * n
    turnaround_times = [0] * n

    time = 0  # current time

    while True:
        done = True

        for i in range(n):
            if remaining_times[i] > 0:
                done = False

                # If process needs more than quantum
                if remaining_times[i] > quantum:
                    time += quantum
                    remaining_times[i] -= quantum
                else:
                    # Process finishes
                    time += remaining_times[i]
                    waiting_times[i] = time - burst_times[i]
                    remaining_times[i] = 0

        if done:
            break

    # Calculate turnaround times
    for i in range(n):
        turnaround_times[i] = burst_times[i] + waiting_times[i]

    avg_waiting = sum(waiting_times) / n
    avg_turnaround = sum(turnaround_times) / n

    return {
        "waiting_times": waiting_times,
        "turnaround_times": turnaround_times,
        "avg_waiting_time": avg_waiting,
        "avg_turnaround_time": avg_turnaround
    }
