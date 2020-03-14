#Ask user for a sentence.

original = input("Please enter a sentence: ").strip().lower()


#Split sentence into individual words.

words = original.split()


#Loop through all words and convert to pig-latin.
    #If starts with vowel, add "yay".
    #If starts with consonant, move first consonant cluster to end and add "ay".

new_words = []
for word in words :
    if word[0] in "aeiou" :
        new_word = word + "yay"
        new_words.append(new_word)

    else:
       vowel_pos = 0
       for letter in word:
           if letter not in "aeiou" :
               vowel_pos = vowel_pos + 1
           else:
               break
       cons = word[:vowel_pos]
       rest = word[vowel_pos:]
       new_word = rest + cons + "ay"
       new_words.append(new_word)


#Stick words back together.

output = " ".join(new_words)

#Output the final string.

print(output)
