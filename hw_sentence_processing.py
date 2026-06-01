sentence_input = input("Enter a sentence: ")

cleaned_sentence = sentence_input.strip()
uppercase_sentence = cleaned_sentence.upper()
replaced_sentence = uppercase_sentence.replace("BAD", "GOOD")

print("Cleaned:", cleaned_sentence)
print("Uppercase:", uppercase_sentence)
print("Modified:", replaced_sentence)