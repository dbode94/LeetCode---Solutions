def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    minLength = len(word2) if len(word1) >= len(word2) else len(word1)
    mix = ''

    for i in range(minLength):
        mix += word1[i] + word2[i]

    mix += word1[len(word2): len(word1)
                 ] if len(word1) >= len(word2) else word2[len(word1): len(word2)]

    return mix
