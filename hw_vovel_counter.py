word = input("Enter a word: ")
vovels = "aeiouAEIOU"
counter = 0

for harf in word:
    if harf in vovels:
        counter += 1

print("The amount of vovels in the word:", counter)