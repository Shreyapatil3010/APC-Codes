
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    freq = {}

    for ch in str1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in str2:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False

    return True


word1 = input("Enter first string: ")
word2 = input("Enter second string: ")

if are_anagrams(word1, word2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

