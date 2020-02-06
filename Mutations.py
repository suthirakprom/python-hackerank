def mutation(string, position, character):
    new_str = string[:position] + character + string[position + 1:]
    return new_str

if __name__ == '__main__':
    string = input("Enter a string: ")
    position = int(input("Enter a position where you insert a character: "))
    character = input("Enter a character: ")
    s_new = mutation(string, position, character)
    print(s_new)