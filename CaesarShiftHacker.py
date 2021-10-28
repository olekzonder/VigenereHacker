import FreqAnalysis
import VigenereDecrypt
import Constants
def hack(lang,word):
    potentialLetters = {}
    alphabet = Constants.pick_alphabet(lang)
    for i in alphabet:
        bruteDecrypt = VigenereDecrypt.decryption(lang,word,i)
        matchScore = FreqAnalysis.analyseMatchScore(lang,FreqAnalysis.analysePercentage(lang,bruteDecrypt))
        potentialLetters[i] = matchScore
    potentialLetters = sorted(potentialLetters, key=potentialLetters.get, reverse=True)[:3]
    return potentialLetters