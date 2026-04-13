def simulate_lru(pages, capacity):

  if __name__ == "__main__":
    pages = [1, 2, 3, 1, 4, 5]
    capacity = 3

    result = simulate_lru(pages, capacity)

    print("Page Faults:", result["page_faults"])
    print("Final Frames:", result["final_frames"])

    frames = []              # current pages in memory
    page_faults = 0

    for page in pages:
        # If page is already in memory → move it to most recently used
        if page in frames:
            frames.remove(page)
            frames.append(page)

        else:
            page_faults += 1

            # If space available → add page
            if len(frames) < capacity:
                frames.append(page)
            else:
                # Remove least recently used (first element)
                frames.pop(0)
                frames.append(page)

    return {
        "page_faults": page_faults,
        "final_frames": frames
    }
