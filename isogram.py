# Check if the word is an isogram

import collections

def main(word):
    """Check if Word is an isoggram or not"""
    word_count = collections.Counter(word)

    for item in word_count.items():
        if item[1] > 1:
            print(f"{word} is not an isogram!")
            break
    else:
        print(f"Yippee... {word} is an isogram")

if __name__ == "__main__":    
    word = input("pls supply a word: \n")
    main(word=word)
