
from stats import get_num_words
from stats import get_char_count
from stats import sort_chars

import sys


BOOK = ''


def get_book_text( fp):
    with open(fp) as f:
        content = f.read()
    return content


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')

    #book = 'books/frankenstein.txt'
    BOOK = sys.argv[1]
    text = get_book_text(BOOK)
    num_of_words = get_num_words( text)

    char_count = get_char_count( text)
    sorted_chars = sort_chars( char_count)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {BOOK}...')
    print('----------- Word Count ----------')
    print( f'Found {num_of_words} total words')
    print('--------- Character Count -------')
    for char,count in sorted_chars:
        if char.isalpha():
            print(f'{char}: {count}')
    print('============= END ===============')



main()
