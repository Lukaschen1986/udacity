s = "betty bought a bit of butter but the butter was bitter"
def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    s_split = s.split(" ")
    count = {}
    for w in s_split:
        count.setdefault(w, 0)
        count[w] += 1
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    count_sort = sorted(count.items(), key=lambda x:x[1], reverse=True)
    top_n = count_sort[0:n]
    # TODO: Return the top n most frequent words.
    return top_n
