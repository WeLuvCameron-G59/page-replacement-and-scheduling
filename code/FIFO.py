def simulate_fifo(pages, capacity):
  
   if __name__ == "__main__":
    pages = [1, 2, 3, 1, 4, 5]
    capacity = 3

    result = simulate_fifo(pages, capacity)

    print("Page Faults:", result["page_faults"])
    print("Final Frames:", result["final_frames"])

    frames = []           # current pages in memory
    queue_index = 0       # pointer for FIFO replacement
    page_faults = 0

    for page in pages:
        # If page is not in memory → page fault
        if page not in frames:
            page_faults += 1

            # If there is space, just add the page
            if len(frames) < capacity:
                frames.append(page)
            else:
                # Replace the oldest page (FIFO)
                frames[queue_index] = page
                queue_index = (queue_index + 1) % capacity
        # else: page hit (do nothing)

    return {
        "page_faults": page_faults,
        "final_frames": frames
    }
