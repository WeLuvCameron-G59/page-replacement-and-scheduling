def simulate_lru(pages, capacity):
    frames = []
    page_faults = 0

    for page in pages:
        if page in frames:
            frames.remove(page)
            frames.append(page)
        else:
            page_faults += 1

            if len(frames) < capacity:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)

    return {
        "page_faults": page_faults,
        "final_frames": frames
    }
