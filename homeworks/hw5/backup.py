def min_needed(sections, target):
    # Create a dictionary to store the minimum sections needed
    # for each remaining target length.
    cache = {0: (0, [])}
    # Iterate through each remaining target length starting from 1 up to target.
    for length in range(1, target+1):
        # stores an int min count and arr sections used
        min_count = float('+inf')
        min_used = []
        # go through each section starting at the end
        for section in sections:
            # Calculate the remaining target length after subtracting the current section
            remaining_length = length - section
            # Check if the remaining length is valid and if the minimum count for that length has already been computed
            if remaining_length >= 0 and remaining_length in cache:
                count, used = cache[remaining_length]
                # update min if curr count is lower than before
                if count + 1 < min_count:
                    min_count = count + 1
                    min_used = used + [section]
        # Store the minimum count and sections used for the current length in the cache
        cache[length] = (min_count, min_used)
    # Return the minimum count and sections used for the target length
    return cache[target]