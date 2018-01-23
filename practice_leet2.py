def substrin(s):
    arr = []
    MaxLen = 0
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            arr.append(s[i:j])
    for sub in arr:
        subSet = set(sub)
        l = list(subSet)
        if len(sub) == len(l) and len(sub) > MaxLen:
            MaxLen = len(sub)
    return MaxLen

# print(substrin("khoixbmjvvfuvwcvyjllymocshinmicwsqhptvaprhlmdnjewwpvidxcmfpyqtxkl"))


def reverse(x):
    s = str(abs(x))
    new = ""
    for elem in s:
        new  = elem + new
    if str(x)[0] == "-":
        new = "-" + new
        return new


nums = set(["0","1","2","3","4","5","6","7","8","9"])

def myAtoi(str):
    str = str.strip(" ", "")
    print str
    if str == "":
        return 0
    for i in str:
        if i not in nums:
            print i
            return 0
    return int(str)


def convert(s, numRows):
    new = ""
    diag = 2 * numRows - 2
    for k in range((len(s))):
        if k % diag == 0:
            new += s[k]
    for j in range(1,numRows-1):
        for k in range(len(s)):
            if k % diag == j:
                new += s[k]
                print s[k]
            if k % diag == diag-j:
                new += s[k]
                print("here")
    for k in range((len(s))):
        if k % diag == numRows-1:
            new += s[k]
    return new

#print(convert("paypalishiring", 4))

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    prefix = strs[0]
    for elem in strs:
        n = min(len(prefix),len(elem))
        if n == 1:
            if prefix[0] != elem[0]:
                return ""
        for i in range(n):
            print prefix,elem, i 
            if prefix == "":
                break
            if prefix[i] != elem[i]:
                prefix = prefix[:i]
                break
        if len(prefix) >len(elem):
            prefix = elem
    return prefix

#print(longestCommonPrefix(["aabaa", "aab" ]))


chain = {
        "antelope": ["grass"],
        "big-fish": ["little-fish"],
        "bug": ["leaves"],
        "bear": ["big-fish", "bug", "chicken", "cow", "leaves", "sheep"],
        "chicken": ["bug"],
        "cow": ["grass"],
        "fox": ["chicken", "sheep"],
        "giraffe": ["leaves"],
        "lion": ["antelope", "cow"],
        "panda": ["leaves"],
        "sheep": ["grass"],
        "grass": []
        }

def who_eats_who1(zoo):
    arr = zoo.split(",")
    fin = [zoo]
    #outside = {}
    #for k in range(len(zoo)):
     #   animal = zoo[k]
      #  if animal not in chain:
       #     zoo.pop(animal)
        #    outside[animal] = k
    if len(arr) == 1 or len(arr) == 0:
        return fin
    print fin
    change = True
    i = 0
    while len(arr) > 1 and i < len(arr):
        l = len(arr)
        print l,i
           # if arr[i] not in chain:
            #    print fin, arr,'c', i 
            #    continue
        if arr[0] in chain and arr[1] in chain[arr[0]]:
            fin.append(arr[0] + " eats " + arr[1])
            arr.pop(1)
            print fin, arr, 'a'
            i = 0
            continue
        if arr[1] in chain and arr[0] in chain[arr[1]]:
            fin.append(arr[1] + " eats " + arr[0])
            arr.pop(0)
            i = 0
            print fin, arr, 'b'
            continue
        if arr[0] not in chain or arr[1] not in chain:
            i = 2
        if i>0:
            if arr[i] not in chain:
                i += 1
                if i == l:
                    break
                continue
            if arr[i-1] in chain[arr[i]]:
                fin.append(arr[i] + " eats " + arr[i-1] )
                arr.pop(i-1)
                i = 0
               # import pdb; pdb.set_trace()
                continue
            if i == len(arr)-1:
                break
        if i < len(arr)-1:
            if arr[i] not in chain:
                i += 1
                if i == l:
                    break
                continue
            if arr[i+1] in chain[arr[i]]:
                fin.append(arr[i] + " eats " + arr[i+1] )
                arr.pop(i+1)
                i = 0
                continue
            else:
                i += 1
                if i == l:
                    break
                continue
    fin.append( ",".join(x for x in arr))
    return fin

#print(who_eats_who1("grass,fox,bug,chicken,grass,sheep,horse"))


#takes index
def eat_left(i,zoo):
    if i == 0:
        return None
    left = zoo[i-1]
    current = zoo[i]
    if left in chain.get(current, []):
        zoo.pop(i-1)
        return "{} eats {}".format(current, left)


def eat_right(i,zoo):
    if i >= len(zoo)-1:
        return None
    right = zoo[i+1]
    current = zoo[i]
    if right in chain.get(current, []):
        zoo.pop(i+1)
        return "{} eats {}".format(current, right)


#takes array (current zoo state) and returns a string of one thing that happens and mutates the zoo status or nothing
def one_chain(zoo):
    l = len(zoo)
    for i in range(l):
       s = eat_left(i,zoo) or eat_right(i,zoo)
       if s:
           return s
    return None


def who_eats_who(animals):
        zoo = animals.split(",")
        result = [animals]
        while True:
            s = one_chain(zoo)
            if s:
                result.append(s)
            else:
                break
        result.append(",".join(zoo))
        return result

print(who_eats_who("grass,fox,bug,chicken,grass,sheep,horse"))


    

