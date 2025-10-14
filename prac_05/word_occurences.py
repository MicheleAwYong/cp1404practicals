def main():
    text = input("Text: ")

    words = text.lower().split()

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_words = sorted(word_counts.keys())

    if sorted_words:
        longest_word = max(sorted_words, key=len)
        max_width = len(longest_word)
    else:
        max_width = 0

    for word in sorted_words:
        count = word_counts[word]
        print(f"{word:<{max_width}} : {count}")


if __name__ == '__main__':
    main()