 
import re, sys


def get_input():
    """Gets input from the user and saves it to a variable."""
    input_text = sys.stdin.read()
    return input_text


def save_input(input_text):
    """Saves the input text to a variable."""
    global user_input
    user_input = input_text


def main():
    """The main function."""
    input_text = get_input()
    save_input(input_text)
    # Convert the user_input into a list with each element a new line.
    lines = re.split("\n", input_text)
    return lines

if __name__ == "__main__":
    print('\nPaste in the first set of data:  hit <enter> and ctrl + d when done')
    first = main()
    print('\nPaste in the second set of data:  hit <enter> and ctrl + d when done')
    second = main()

    new_list = [x for x in second if x not in first]
    fell_off = [x for x in first if x not in second]

    print('\nThese items below are on the second list and were not on the first: -- New --\n')
    for item in new_list:
        print(item)
    print('\n -- end --')
    print('\nThese items below are on the second list and were not on the first: -- Fell Off --\n')
    for item in fell_off:
        print(item)
    print('\n -- end --')

    #print(type(first))
    #print(first)