# pypy printer

'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # TBC

    #print(word.count("th", 0, len(word)))
    print(len(word))
    if len(word) < 2:
        return 0
    elif word[0:2] != "th":
        return count_th(word[1:])
    elif word[0:2] == "th":
        print("1")
        return count_th(word[1:])


count_th('thsthsmiththythy thy pop')
