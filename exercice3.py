words = ["apple", "banana", "avocado", "cherry", "apricot", "grape", "blueberry"]
filtered_words = list(filter(lambda word: word.startswith("a"), words))
print(filtered_words)  
def count_long_words(min_length):
    return lambda words_list: len([word for word in words_list if len(word) > min_length])

count_words = count_long_words(5)
print(count_words(words))  
