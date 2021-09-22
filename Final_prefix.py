strs_trial = ['flower','flow','flies']

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]

    first = strs[0]
    leng = len(first)
    for i in strs[1:]:
        while i[0:leng] != first:
            first = first[0:leng-1]
            leng = leng - 1
            if leng == 0:
                return ""
    return "".join(first)

print(longestCommonPrefix(strs_trial))