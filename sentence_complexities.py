# Opgave 7 (Sentence Complexities)
def sentence_complexities(filename):
    punctuation = ".,!?"
    complexities = []

    with open(filename) as f:
        content = f.read().splitlines()
    
    for line in content:
        words = line.split(" ")
        lenghts = []
        word_cnt = 0
        for word in words:
            for char in word:
                if char in punctuation:
                    word = word.replace(char, "")
            lenghts.append(len(word))
            word_cnt += 1
        complexities.append(word_cnt + max(lenghts))
    return complexities