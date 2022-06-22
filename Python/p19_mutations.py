string = input()
position, character = input().split()

def mutate_string(string, position, character):

    new_string = list(string)
    new_string[int(position)] = character
    string = "".join(new_string)
    return string
print(mutate_string(string, position, character))