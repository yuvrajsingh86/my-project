def find_longest_substring(input_str):

    # Replace this placeholder return statement with your code
    mapping = [-1] * 26
    longest_start = 0
    longest_end = 0
    longest_length = 0
    start = 0
    end = 0
    # abcdbea

    while end < len(input_str):
        pos = ord(input_str[end].lower()) - ord("a")
        if mapping[pos] == -1:
            if end - start + 1 > longest_length:
                longest_start = start
                longest_end = end
                longest_length = longest_end - longest_start + 1
            mapping[pos] = end
            end = end + 1
        else:
            while start <= mapping[pos]:
                mapping[start] = -1
                start = start + 1
            mapping[pos] = end
            end += 1

    return longest_length


find_longest_substring("abcdbea")
