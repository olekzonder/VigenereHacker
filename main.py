import os
def pause():
    if os.name == 'nt':
        os.system('pause')  # windows, doesn't require enter
    else:
        os.system('read -p "Нажмите любую клавишу, чтобы продолжить..."')  # linux

#Грубый перебор сообщения словарём
def picklang():
    lang = ''
    while not(lang == "en" or lang == "ru"):
        lang = input("Выберите язык (en/ru) >")
    return lang

def pickword():
    choice = ''
    while not(choice == 'f' or choice == 'w'):
        choice = input("Выберите, откуда получить сообщение: из файла in.txt (f) или из прямого ввода (w): ")
    if choice == 'w':
        word = input("Введите сообщение:")
    else:
        with open('in.txt', encoding="utf-8") as f:
            word = f.read()
    return word

def checklang(lang):
    if lang == '':
        lang = picklang()
    return lang
def checkword(word):
    if word == '':
        word = pickword()
    return word

def vigeneredecrypt(lang,word,key):
    import VigenereDecrypt
    result = VigenereDecrypt.decryption(lang,word,key)
    print(result)
    choice = ''
    while not (choice == "y" or choice == "n"):
        choice = input("Записать в файл? (y/n) >")
    if choice == 'y':
        with open('out.txt','w') as f:
            f.write(result)
        print("Результат записан в файл out.txt")

def brute(lang,word):
    import DictionaryHacker
    print("<<Взлом с помощью \"грубого\" перебора словарём>>")
    word = ''.join(filter(str.isalpha, word))
    print(DictionaryHacker.dictionaryhack(lang, word))
    pause()


#Частотный анализ сообщения
def freqanalysis(lang,word):
    import json
    import FreqAnalysis
    word = ''.join(filter(str.isalpha, word))
    percentage = FreqAnalysis.analysePercentage(lang, word)
    percentage = json.dumps(percentage)
    print("Результат в JSON:",percentage)
    pause()

#Взлом шифра Цезаря
def hackcaesar(lang,word):
    import KeyFinder
    print("<<Взлом шифра Цезаря>>")
    word = ''.join(filter(str.isalpha, word))
    decipherDict = KeyFinder.findPossibleKeys(lang,word,1)
    print("Ключ:", KeyFinder.finalProcessing(lang,decipherDict,word,1))
    pause()

#Криптоанализ с помощью метода Касиски
def kasiski(lang,word):
    import Kasiski
    import KeyFinder
    print("<<Взлом с помощью метода Касиски>>")
    word = ''.join(filter(str.isalpha, word))
    possibleKeys = Kasiski.analyze(lang,word)
    if bool(possibleKeys):
        print("Обнаруженные возможные длины ключа:", *possibleKeys, sep = '\n')
        keylen = int(input("Введите длину ключа: "))
        decipherDict = KeyFinder.findPossibleKeys(lang, word, keylen)
        key = KeyFinder.finalProcessing(lang,decipherDict,word,keylen)
        print("Ключ:", key)
        choice = ''
        while not (choice == "y" or choice == "n"):
            choice = input("Расшифровать полученным ключом? (y/n) >")
        if choice == "y":
            vigeneredecrypt(lang,word,key)
    else:
        print("Длины ключей не обнаружены. Попробуйте использовать метод индекса совпадений.")
    pause()

def ic(lang,word):
    import IndexOfCoincidence
    import KeyFinder
    word = ''.join(filter(str.isalpha, word))
    possibleKeys = IndexOfCoincidence.analyze(lang,word)
    print("Обнаруженные возможные длины ключа:", *possibleKeys, sep='\n')
    keylen = int(input("Введите длину ключа: "))
    decipherDict = KeyFinder.findPossibleKeys(lang, word, keylen)
    key = KeyFinder.finalProcessing(lang, decipherDict, word, keylen)
    print("Ключ:",key)
    choice = ''
    while not (choice == "y" or choice == "n"):
        choice = input("Расшифровать полученным ключом? (y/n) >")
    if choice == "y":
       vigeneredecrypt(lang,word,key)
    pause()
def langdetection(lang,word):
    import DetectLanguage
    word = ''.join(filter(str.isalpha, word))
    print(DetectLanguage.DetectLanguage(lang,word))
    pause()

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu(word,lang):
    menuChoices = {}
    menuChoices['1'] = "[1] Выбор языка"
    menuChoices['2'] = "[2] Изменение сообщения"
    menuChoices['3'] = "[3] Грубый перебор сообщения словарём"
    menuChoices['4'] = "[4] Частотный анализ сообщения"
    menuChoices['5'] = "[5] Взлом шифра Цезаря"
    menuChoices['6'] = "[6] Криптоанализ с помощью метода Касиски"
    menuChoices['7'] = "[7] Криптоанализ с помощью индекса совпадений"
    menuChoices['8'] = "[8] Определение наличия слов выбранного языка в сообщении"
    menuChoices['9'] = "[9] Расшифровать шифр Виженера известным ключом"
    menuChoices['0'] = "[0] Выход"
    while True:
        cls()
        for i in menuChoices:
            print(menuChoices[i])
        if lang == '':
            print("Язык не установлен")
        else:
            print("Язык:",lang)
        if word == '':
            print("Сообщение отсутствует")
        else:
            if len(word) < 20:
                print("Сообщение:", *word,sep=' ')
            else:
                print("Сообщение:",*word[:20],'...',sep="")
        selection=input("Ваш выбор:")
        if selection =='1':
            lang = picklang()
        elif selection == '2':
            word = pickword()
        elif selection == '3':
            lang = checklang(lang)
            word = checkword(word)
            brute(lang,word)
        elif selection == '4':
            lang = checklang(lang)
            word = checkword(word)
            freqanalysis(lang,word)
        elif selection == '5':
            lang = checklang(lang)
            word = checkword(word)
            hackcaesar(lang,word)
        elif selection == '6':
            lang = checklang(lang)
            word = checkword(word)
            kasiski(lang,word)
        elif selection == '7':
            lang = checklang(lang)
            word = checkword(word)
            ic(lang,word)
        elif selection == '8':
            lang = checklang(lang)
            word = checkword(word)
            langdetection(lang,word)
        elif selection == '9':
            lang = checklang(lang)
            word = checkword(word)
            key = input("Введите ключ")
            vigeneredecrypt(lang,word,key)
        elif selection == '0':
            break
        else:
            print("Неверный пункт меню!")


#Меню
word = ''
lang = ''
menu(word,lang)
