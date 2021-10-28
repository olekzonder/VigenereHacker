import Constants
def decryption(lang, word, key):
    alphabet  = Constants.pick_alphabet(lang)
    output = []
    N = len(alphabet)
    key_num = 0
    word = word.upper()
    key = key.upper()
    for i in word:
        if i.isalpha():
            Ci = alphabet.index(i)
            Ki = alphabet.index(key[key_num])
            key_num += 1
            if key_num == len(key):
                key_num = 0
            output.append(alphabet[(Ci + N - Ki) % N])
        else:
            output.append(i)
    output = ''.join(output)
    return output
