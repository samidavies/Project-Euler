import itertools



def twoSum(nums, target):
    total = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            total = nums[i] + nums[j]
            if total == target:
                return [i,j]

def addNums(l1, l2):
    arr = []
    q = 0
    while len(l1) > 0:
        n = l1[-1] + l2[-1]
        if q > 0:
            q, r = divmod(n + 1, 10)
        else:
            q, r = divmod(n, 10)
        arr.append(r)
        l1.pop()
        l2.pop()
        print( q, r)
    print(arr)

def rev(l1):
    if l1 == None:
        return l1
    front = l1
    back = l1.next
    rev(back)



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        x = l1.val + l2.val
        l1, l2 = l1.next, l2.next
        if x > 9:
            carry = 1
            x -= 10
        else:
            carry = 0
        head = ListNode(x)
        prev = head
        while l1 != None or l2 != None:
            x = get(l1) + get(l2) + carry
            if x > 9:
                carry = 1
                x -= 10
            else:
                carry = 0
            new = ListNode(x)
            prev.next = new
            prev = new
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            prev.next = ListNode(1)


roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

def RomToInt(n):
    total = 0
    for i in range(len(n)-1):
        if roman[n[i]] < roman[n[i+1]]:
            total -= roman[n[i]]
        else:
            total += roman[n[i]]
    total += roman[n[-1]]
    return total

backrom = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
    }

def IntToRom(n):
    rom = ''
    s = str(n)
    l = len(s)-1
    while l >= 0:
        current = int(s[0]) * 10 ** l
        print current 
        if current in backrom:
            rom += backrom[current]
        if current not in backrom and int(s[0]) < 4:
            for i in range(int(s[0])):
                rom += backrom[10 ** l]
        if int(s[0]) == 4 or int(s[0]) == 9:
            rom += backrom[10 ** l]
            rom += backrom[(int(s[0])+1) * 10 ** l]
        if 5 < int(s[0]) < 9:
            rom += backrom[5 * 10 ** l]
            for i in range(5, int(s[0])):
                    rom += backrom[10 ** l]
        s = s[1:]
        l -= 1
    return rom











