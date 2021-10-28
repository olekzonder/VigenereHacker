import Constants


def analysePercentage(lang, word):
    alphabet = Constants.pick_alphabet(lang)
    freqdict = {}
    total = 0
    for i in alphabet:
        freqdict[i] = 0
    for i in word:
        if i.isalpha():
            freqdict[i] += 1
            total += 1
    for k in freqdict:
        freqdict[k] = round((freqdict[k]/total)*100,2)
    freqdict = dict(sorted(freqdict.items(), key=lambda item: item[1],reverse=True))
    return freqdict


def analyseMatchScore(lang,freqdict):
    import itertools
    alphabet = Constants.pick_frequent(lang)
    matchScoreQuarts = len(alphabet)//4
    mostFreqAlphabet = list(itertools.islice(alphabet,matchScoreQuarts))
    leastFreqAlphabet = list(itertools.islice(reversed(alphabet),matchScoreQuarts))
    mostFreqWord = list(itertools.islice(list(freqdict),matchScoreQuarts))
    leastFreqWord = list(itertools.islice(reversed(list(freqdict)),matchScoreQuarts))
    matchScore = 0
    maxMatchScore = 2*matchScoreQuarts
    for i in mostFreqWord:
        if i in mostFreqAlphabet:
            matchScore += 1
    for i in leastFreqWord:
        if i in leastFreqAlphabet:
            matchScore += 1
    return round(matchScore/maxMatchScore,2)

def findIC(lang,word):
    alphabet = Constants.pick_alphabet(lang)
    N = len(word)
    denominator = N*(N-1)
    freqdict = {}
    for i in alphabet:
        freqdict[i] = 0
    for i in word:
        if i.isalpha():
            freqdict[i] += 1
    for i in freqdict:
        freqdict[i] *= freqdict[i]-1
    ic = round(sum(freqdict.values())/denominator,4)
    return ic
