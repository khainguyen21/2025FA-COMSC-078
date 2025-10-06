# Part 2: Pig Latin
# Write a program that accepts a sentence as input and converts each word to “Pig Latin.” To convert a word to Pig Latin:
#
# If the word begins with a vowel, add “way” at the end of the word.
# Otherwise, move all the consonants from the beginning of the word to the end, and append “ay” to the string.
# For the purposes of this program, a, e, i, o, u, and y are all considered as vowels. You may convert the output to all lower case and ignore all punctuation (other than spaces). Here are some examples of input and output:
#
# Python is a programming language → ythonpay isway away ogrammingpray anguagelay
# Your strong ox plows the field → yourway ongstray oxway owsplay ethay ieldfay
# Your program will repeatedly request user input and convert it to Pig Latin until the user just presses ENTER (with no text) to quit.

while True:
    # Ask the user for a string
    string = input("Enter a string (or just press Enter to stop): ")

    # If the user's input is empty, which means user hit enter, then stop asking
    if string == "":
        break

    # Split each word from a string and store them into the array
    words = string.split()

    # Create vowels set for constant time look up
    vowels_set = {'a', 'e', 'i', 'o', 'u', 'y'}

    # Create a list to hold the new Pig Latin words
    pig_latin_words = []

    # Loop through each word in a string
    for word in words:

        # If the first character of a word is vowel, then add the "way" at the end of the current word
        if word[0].lower() in vowels_set:
            word = word.lower()
            word += "way"
            pig_latin_words.append(word)

        # Otherwise, move all the consonants to behind the word and then add "ay" at the end of the current word
        else:
            # Loop through each character in the current word
            for j, char in enumerate(word):
                # If the character is a vowel
                if char in vowels_set:

                    # Get all the consonants before a vowel
                    consonants = word[:j].lower()

                    # Get the rest of word starting from a vowel
                    afterVowel = word[j:].lower()

                    # Then add the rest of word starting from a vowel and all the consonants
                    word = afterVowel + consonants
                    break

            word += "ay"
            pig_latin_words.append(word)

    print(" ".join(pig_latin_words))
    print()