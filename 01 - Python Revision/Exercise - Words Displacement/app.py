sentence = input("Enter your sentence: ")
print("Your sentence is: "+ sentence)
word_to_replace = input("Enter the word you want to replace: ")
word_to_replace_with = input("Enter the word you want to replace it with: ")
new_sentence = sentence.replace(word_to_replace, word_to_replace_with)
print("Your new sentence is: " + new_sentence);