import pandas


def nato_phonetic_alphabet():
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    nato_dataframe = pandas.DataFrame(data)
    nato_phonetic_alphabet_dictionary = {row.letter: row.code
                                         for (index, row) in
                                         nato_dataframe.iterrows()}
    user_input = input("Enter a word:  ").upper()
    # for letter in user_input:
    #     print(nato_phonetic_alphabet_dictionary[letter])
    # Alternative: list comprehension
    print([nato_phonetic_alphabet_dictionary[letter] for letter in user_input if
           letter in nato_phonetic_alphabet_dictionary.keys()])  # fetches the input from the dictionary,
    # returns the nato code for the  defined letters, ignores all undefined characters (that are not keys in the dict)


nato_phonetic_alphabet()
