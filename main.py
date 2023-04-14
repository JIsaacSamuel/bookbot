letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def main():
    with open(r"C:\Users\isij2\Desktop\Isaac\Boot projects\github.com\JIsaacSamuel\bookbot\books\frankenstein.txt", "r") as f:
        file_contents = f.read()

    words = file_contents.split()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document\n") 

    no_of_occurances = countLetters(file_contents)
    for letter in letters:
        print(f"the '{letter}' character was found {no_of_occurances[letter]} times")

    print("--- End report ---")

def countLetters(allWords):
    allWords.lower()
    req_dict = {}
    for letter in letters:
        req_dict[letter] = allWords.count(letter)

    return req_dict

main()