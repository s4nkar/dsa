# T(On) S(On
# eg s = "abcabcbb" out=3

def length_of_longest_substring(s):
    seen = {}
    left = 0
    longest = 0

    for i, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1

        seen[ch] = i

        current_window = i + 1 - left
        longest = max(longest, current_window)

    return longest

print(length_of_longest_substring("abcabcb"))