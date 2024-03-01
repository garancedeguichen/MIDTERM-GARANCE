def is_valid_url():
    """
    Prompts the user to input a URL and checks if it's valid.
    :return: True if the URL is valid, False otherwise
    """
    # Enter an URL that the code will analyze
    url = input("Please enter a URL: ")

    # Check if the URL starts with 'http://' or 'https://' which is a basic assumption to make it valid or not
    if url.startswith("http://") or url.startswith("https://"):
        # Check if there is at least one period '.' after 'http://' or 'https://' which is a basic assumption to make it valid or not
        if '.' in url[url.index("//")+2:]:
            return True
    return False

# Call the function to check if the provided URL is valid and answer the question
if is_valid_url():
    print("The provided URL is valid.")
else:
    print("The provided URL is not valid.")