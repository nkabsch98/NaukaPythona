def longestCommonPrefix(strs):
    longest_prefix = strs[0]
    for word in strs:
        while len(longest_prefix) > 0 and longest_prefix not in word[:len(longest_prefix)]:
            longest_prefix = longest_prefix[:-1]
    return longest_prefix



print(longestCommonPrefix(["c","acc","ccc"]))