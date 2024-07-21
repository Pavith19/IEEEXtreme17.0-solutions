"""
Author: Pavith Bambaravanage
URL: https://github.com/Pavith19
"""

def get_most_frequent_letter(secret_msg):
    # Initialize dictionary to count occurrences of specific letters
    letter_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
    
    # Count occurrences of the specified letters in the secret message
    for letter in secret_msg:
        if letter in letter_count:
            letter_count[letter] += 1
    
    # Find the letter with the maximum count
    max_count = -1
    most_frequent_letter = ''
    for letter in 'abcdefg':
        if letter_count[letter] > max_count:
            max_count = letter_count[letter]
            most_frequent_letter = letter
        elif letter_count[letter] == max_count:
            if letter < most_frequent_letter:  # Ensures lexicographical order in case of ties
                most_frequent_letter = letter
    
    return most_frequent_letter.upper()

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0].strip())
    if 1 <= n <= 20:
        for i in range(1, n + 1):
            secret_msg = data[i].strip().lower()
            print(get_most_frequent_letter(secret_msg))

if __name__ == "__main__":
    main()

