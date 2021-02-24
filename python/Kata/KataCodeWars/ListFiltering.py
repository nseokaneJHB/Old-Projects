# Create a function that takes in a list of non-negative values and strings and return a new list with strings filtered out


def filter_list(list):
    new_list = []
    for x in list:
        if not type(x) == str:
            new_list.append(x)

    return new_list


print(f"First list {filter_list([1, 2, 'a', 'b'])}")
print(f"Second list {filter_list([1, 'a', 'b', 0, 15])}")
print(f"Third list {filter_list([1, 2, 'aasf', '1', '123', 123])}")
