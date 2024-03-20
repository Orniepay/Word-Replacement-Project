print("")
print("Welcome to Word Replacer")
print("")

def replace_word():
    """
    Prompts the user for a sentence, a word to replace, and its replacement in the given sentence.

    The function first asks the user to input a sentence. Then it asks for the user's input on which word to replace 
    and what to replace it with. It then prints the modified string where the specified word has been replaced with 
    the user's input.

    @param None
    @returns None
    """
    user_string = input("Enter a sentence: ")
    print("")
    word_to_replace = input("Enter the word to replace: ")
    print("")
    word_replacement = input("Enter the word replacement: ")
    print("")
    print(user_string.replace(word_to_replace, word_replacement))
    print("")

replace_word()