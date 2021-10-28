import mmap
import Constants
def DetectLanguage(lang, word):
    langwords = 0
    dictfile = Constants.pick_dict(lang)
    with open(dictfile, 'rb') as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
        for i in word:
            if s.find(i.encode()) != -1:
                langwords += 1
    return round(langwords / len(word),2)