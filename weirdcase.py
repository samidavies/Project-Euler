def to_weird_case(string):
    copy = "" 
    counter = 0
    for i in range(len(string)):
        if string[i] == " ":
            copy += " "
            counter = 0
        elif counter % 2 == 1:
            copy += string[i].lower()
            print(string[i],counter)
            counter += 1            
        elif counter % 2 == 0:
            copy+= string[i].upper()
            print(string[i],counter)     
            counter += 1
    return copy

def convert_to_kg(n,s):
    if s == "G":
        return n / 1000.0
    if s == "T":
        return n * 1000.0
    if s == "KG":
        return n


def find_key(dic,value):
    arr = []
    for k in dic:
        if dic.get(k) == value:
            print(k)
            arr.append(k)
    return arr

def extract_suffix(s):
    if s[-2] == 'K':
        return int(s[0:-2]) , 'KG'
    return int(s[0:-1]), s[-1] 


print(find_key({"200G":0.2,"300G":0.3,"150G":0.15,"100KG":100},0.15))

def arrange(arr):
    weights = {}
    units = []
    srtd = []
    for item in arr:
        num, suffix = extract_suffix(item)
        print(num,suffix)
        if item in weights:
            weights[item].append("multiple")
        else:
            weights[item] = []
            weights[item].append(convert_to_kg(num,suffix))
    new_arr = weights.values()
    new_arr.sort()
    print(new_arr)
    for v in new_arr:
        keys = find_key(weights, v)
        print(weights,v)
        print(keys)
        for k in keys:
            srtd.append( k)
    return srtd

           

print(arrange(["200G","300G","200G","150G","100KG"]))
