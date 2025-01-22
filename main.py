def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count = len(file_contents.split())
        file_contents = file_contents.lower()

        char_dict = dict()
        for char in file_contents:
            #if str(char).isalpha() or char == ' ':
            if str(char).isalpha():
                if char in char_dict:
                    char_dict[char] += 1   
                else:
                    char_dict[char] = 1
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count} words found in the document")

        for char in char_dict:
            print(f"The '{char}' character was found {char_dict.get(char)} times")

        print("--- End report ---")

main()
