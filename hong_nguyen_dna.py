# A dictionary that maps each three-letter DNA codon (the key) to its
# corresponding amino acid abbreviation (the value). This serves as the
# primary lookup table for the translation.
# '***' is used to represent a "stop" codon, which terminates translation.
codon_map = {
    'TTT': 'Phe', 'TTC': 'Phe', 'TTA': 'Leu', 'TTG': 'Leu',
    'TCT': 'Ser', 'TCC': 'Ser', 'TCA': 'Ser', 'TCG': 'Ser',
    'TAT': 'Tyr', 'TAC': 'Tyr', 'TAA': '***', 'TAG': '***',
    'TGT': 'Cys', 'TGC': 'Cys', 'TGA': '***', 'TGG': 'Trp',
    'CTT': 'Leu', 'CTC': 'Leu', 'CTA': 'Leu', 'CTG': 'Leu',
    'CCT': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'CAT': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
    'CGT': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
    'ATT': 'Ile', 'ATC': 'Ile', 'ATA': 'Ile', 'ATG': 'Met',
    'ACT': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'AAT': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'AGT': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
    'GTT': 'Val', 'GTC': 'Val', 'GTA': 'Val', 'GTG': 'Val',
    'GCT': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'GAT': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
    'GGT': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
}

# --- Helper Functions ---
def clean_sequence(string: str) -> str:
    """
    Takes a raw string and prepares it for processing.
    It removes any non-alphabetic characters (like spaces or commas)
    and converts the entire sequence to uppercase for consistency.
    """
    clearedListStr = []  # A temporary list to hold the valid characters.

    # Iterate through each character in the input string.
    for char in string:
        # If the character is a letter, add its uppercase version to the list.
        if char.isalpha():
            clearedListStr.append(char.upper())

    # Join the characters in the list back into a single, clean string.
    return "".join(clearedListStr)


def is_valid_codon(codon: str) -> bool:
    """
    Checks if a given 3-letter codon contains only valid DNA nucleotides.
    Returns True if valid, False otherwise.
    """
    # A set containing the four valid nucleotide characters for fast lookups.
    valid_nucleotides = {"A", "C", "G", "T"}

    # Check each character within the codon.
    for char in codon:
        # If any character is not in our set of valid nucleotides, the codon is invalid.
        if char not in valid_nucleotides:
            return False

    # If the loop completes without finding invalid characters, the codon is valid.
    return True


# --- Main Program Loop ---

# This `while True` loop will run indefinitely until the user decides to quit.
while True:
    print()  # Adds a blank line for better readability in the terminal.

    # Prompt the user for input.
    user_input = input("Enter a nucleotide sequence, or just press ENTER to quit: ")

    # If the user presses Enter without typing anything, break out of the loop to end the program.
    if user_input == "":
        break

    # Step 1: Sanitize the user's input string.
    cleaned_input = clean_sequence(user_input)

    # Step 2: Validate the length of the cleaned sequence.
    # The total number of characters must be a multiple of 3.
    if len(cleaned_input) % 3 != 0:
        print("Error: You must give complete triples.")
        continue  # Skip the rest of this iteration and prompt for new input.

    # Step 3: Process the sequence in chunks of three.
    # The `range` function with a step of 3 (e.g., 0, 3, 6, ...) lets us grab
    # each codon by its starting index.
    for i in range(0, len(cleaned_input), 3):
        # Slice the string to get the current 3-letter codon.
        nucleotide = cleaned_input[i: i + 3]

        # Check if the codon contains valid characters (A, C, G, T).
        if not is_valid_codon(nucleotide):
            print(f"{nucleotide} invalid sequence")

        # If the codon is valid, look it up in the dictionary and print the result.
        else:
            print(f"{nucleotide} {codon_map[nucleotide]}")