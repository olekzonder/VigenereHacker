import Constants
def analyze(lang,word):
    alphabet = Constants.pick_alphabet(lang)
    k = len(alphabet)//2
    rotatedWord = word
    icdict = {}
    for i in range (1,k+1):
        icdict[i] = 0
        rotatedWord = rotatedWord[1:] + rotatedWord[:1]
        count = 0
        for j in range(len(word)):
            if rotatedWord[j] == word[j]:
                count += 1
        icdict[i] = round(count/len(word),4)
    icdict = dict(sorted(icdict.items(), key=lambda item: item[1],reverse=True))
    return icdict