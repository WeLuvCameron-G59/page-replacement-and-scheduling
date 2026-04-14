def simulate_fifo(pages, capacity):
    frames = []
    page_faults = 0
    queue_index = 0  # tracks which page to replace

    for page in pages:
        if page not in frames:
            page_faults += 1

            # If there is space, add page
            if len(frames) < capacity:
                frames.append(page)
            else:
                # Replace oldest page (FIFO)
                frames[queue_index] = page
                queue_index = (queue_index + 1) % capacity

        # else: page hit → do nothing

    return {
        "page_faults": page_faults,
        "final_frames": frames
    }
