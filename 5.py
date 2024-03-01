def find_pattern_occurrences(text):
    """
    Finds all occurrences of a pattern that starts with "C", has unlimited number of letters,
    and ends with "jeb" in the given text.
    :param text: The text to search within
    :return: The number of matches found
    """
    pattern = "C"  # Define the start of the pattern
    target = "jeb"  # Define the end of the pattern
    occurrences = 0  # Counter for occurrences

    # Iterate through the text to search for the pattern
    for i in range(len(text)):
        # Check if the current character matches the start of the pattern
        if text[i] == pattern[0]:
            # Check if the substring starting from the current index has the same pattern
            if text[i:].startswith(pattern):
                # Find the index of the end of the pattern
                end_index = text.find(target, i)
                # Check if the end of the pattern is found and if it's after the start
                if end_index != -1:
                    # Increment the occurrences counter
                    occurrences += 1
                    # Move the iterator to the end of the found pattern
                    i = end_index + len(target) - 1

    return occurrences


# Example usage:
text = "CabcjebCdefjebCghijeb"
print("Number of pattern occurrences:", find_pattern_occurrences(text))