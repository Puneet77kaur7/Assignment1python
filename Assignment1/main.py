import string

# QUESTION 1 :-Read the text file
with open("Assignment1/sample.txt", "r") as file:
    text = file.read().lower()

# Remove punctuation and split the text into words
translator = str.maketrans('', '', string.punctuation)
cleaned_text = text.translate(translator)
words = cleaned_text.split()

#  QUESTION 2:-Count word frequencies
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Sort words from most to least frequent
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# QUESTION 3 :-Save the report to a text file
with open("sampleReport.txt", "w") as report_file:
    for word, count in sorted_word_counts:
        report_file.write(f"{word}: {count}\n")

print(" Report saved to sampleReport.txt")




                      