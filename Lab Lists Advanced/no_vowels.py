vowels_list = ['a', 'o', 'u', 'e', 'i']
command = input()
word_without_vowels = [character for character in command if character.lower() not in vowels_list]
print("".join(word_without_vowels))