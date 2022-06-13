# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename, 'r') as f:
        file_data = f.read()
    
    return file_data


def count_words():
    text = read_file_content("./story.txt")
    word_dict = {}
    for word in text.split():
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict
