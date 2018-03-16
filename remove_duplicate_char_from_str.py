NO_OF_CHARS = 256
def toMutable(string):
    List = []
    for i in string:
        List.append(i)
    return List
 
def toString(List):
    return ''.join(List)

def removeDups(string):
    bin_hash = [0] * NO_OF_CHARS
    ip_ind = 0
    res_ind = 0
    temp = ''
    mutableString = toMutable(string)
    while ip_ind != len(mutableString):
        temp = mutableString[ip_ind]
        if bin_hash[ord(temp)] == 0:
            bin_hash[ord(temp)] = 1
            mutableString[res_ind] = mutableString[ip_ind]
            res_ind+=1
        ip_ind+=1
     return toString(mutableString[0:res_ind])
    