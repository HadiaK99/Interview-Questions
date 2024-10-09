"""
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
    If a string is longer than the other, append the additional letters onto the end of the merged string.
    Return the merged string.
"""


def mergeAlternately(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    i = 0
    j = 0
    result = []

    while(i < len(word1) or j < len(word2)):
        if i < len(word1):
            result += word1[i]
            i+=1
        if j < len(word2):
            result += word2[j]
            j+=1

    return "".join(result)

mergeAlternately("ab", "pqrs")