import Constants

def findSequences(word):
    seqDistance = {}
    minLen = Constants.kasiskiMinSize
    maxLen = Constants.kasiskiMaxSize
    wordLen = len(word)
    for seqLen in range(minLen,maxLen):
        for seqNew in range(wordLen-seqLen):
            seq = word[seqNew:seqNew+seqLen]
            for i in range(seqNew+seqLen,wordLen):
                if word[i:i+seqLen] == seq:
                    seqDistance[seq] = []
                    seqDistance[seq].append(i-seqNew)
    return seqDistance

def findFactors(number):
    if number < 2:
        return []
    factors = []
    maxLen = Constants.kasiskiMaxSize
    for i in range(2,maxLen+1):
        if number % i == 0:
            factors.append(i)
    return factors

def topFactors(seqFactors):
    factor = {}
    for i in seqFactors:
        factorList = seqFactors[i]
        for j in factorList:
            if j not in factor:
                factor[j] = 0
            factor[j] += 1
    factor = dict(sorted(factor.items(), key=lambda item: item[1],reverse=True))
    return factor

def analyze(lang,word):
    word =''.join(word.strip().split())
    repSeq = findSequences(word)
    #print(repSeq)
    seqFactors = {}
    for i in repSeq:
        seqFactors[i] = []
        for j in repSeq[i]:
            seqFactors[i].extend(findFactors(j))
    possiblekeys = list(topFactors(seqFactors))
    return possiblekeys[:10]