def validWordAbbreviation(word, abbr):

    word = list(word)
    i = 0
    j = 0
    while (j <len(abbr) and i<len(word)):
        if abbr[j].isalpha():
            if word[i]!=abbr[j]:
                #print word[i],abbr[j]
                return False
            else:
                i += 1
                j += 1
        else:
            if abbr[j] == '0':
                    return False
            k = j
            while (j<len(abbr) and abbr[j].isalpha()!=True):
                j += 1
            j -=1
            num = int(abbr[k:j+1])
            i += num
            j += 1
    
    if i == len(word) and j == len(abbr):
        return True
    else:
        return False


print validWordAbbreviation(word, abbr)
