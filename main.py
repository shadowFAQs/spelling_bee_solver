"""
Solution finder for the New York Times' Spelling Bee puzzles

To use:

    1. From a CLI, run main.py
    2. When prompted, input the letters in the puzzle in any order
    3. When prompted, specify which letter is required
    4. spelling_bee_solver will generate and score a word list for you
"""
def load_dictionary():
    """Read dictionary file and return words with at least 5 letters"""
    with open('dictionary.txt') as file:
        data = file.read().split('\n')
    return [word for word in data if len(word) >= 5]

def search_dictionary(dictionary, letters, primary):
    """Return all matching words from dictionary"""
    # Words must contain primary letter
    words = [w for w in dictionary if primary in w]

    # Words must not contain any nonspecified letters
    return [w for w in words if all([l in letters for l in w])]

def main():
    """Get user input; look up matching words"""
    dictionary = load_dictionary()

    # Get letters
    letters = [l.upper() for l in input('Enter hive letters: ') if l.isalpha()]
    if not len(letters) == 7:
        raise IndexError('Must enter 7 letters')

    # Get primary letter
    primary = input(f'Which is the primary letter: {letters}? ').upper()
    if not primary in letters:
        raise AttributeError(
            f'Supplied primary "{primary}" not found in letters')

    # Find word list
    print(f'Searching for words using the letters {letters};')
    print(f'    (Must include primary letter "{primary}")...')
    words = search_dictionary(
        dictionary=dictionary, letters=letters, primary=primary)

    # Display found words
    points = 0
    print(f'\nFound {len(words)} matching words:\n')
    for word in words:
        if set(letters).issubset(word):
            print(f'*{word}')
            points += 3
        else:
            print(word)
            points += 1

    # Display point value of word list
    print(f'\nWord list is worth {points} points.')
    print('Words which use all 7 letters are marked with an asterisk.\n')

if __name__ == '__main__':
    main()
