
def main ():
    word_count = {}
    count = 0

    with open("text1.txt", encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            line_words = line.split(" ")

            for word in line_words:
                word = word.strip('\ufeff')
                if word not in word_count:
                    word_count[word] = 0
                word_count[word] += 1
            count +=1
            if count == 100:
                break

    print(word_count)
if __name__ == '__main__':
    main()