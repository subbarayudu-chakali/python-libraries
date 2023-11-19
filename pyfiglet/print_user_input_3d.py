import pyfiglet


def print_jai_shree_ram(text_to_print: str) -> None:
    # Print the text art to the console
    print(pyfiglet.figlet_format(text_to_print))


if __name__ == "__main__":
    # take user input and pass it to the function
    user_input = input("Enter a string: ")
    print_jai_shree_ram(user_input)
