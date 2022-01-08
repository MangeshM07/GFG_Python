print("Imported my_module")

test = "Test String"


def find_index(to_search_in, target):
    """Find the index of a value in a sequence"""
    for i, value in enumerate(to_search_in):
        if value == target:
            return i

    return -1
