name = input()
def solve(name):
    result_as_string = ""
    list_of_words = name.split(' ')

    for elem in list_of_words:
        if len(result_as_string) > 0:
            result_as_string = result_as_string + " " + elem.capitalize()
        else:
            result_as_string = elem.capitalize()

    if not result_as_string:
        return name
    else:
        return result_as_string
solve(name)