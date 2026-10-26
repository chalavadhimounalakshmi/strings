##1.convert lowercase string to uppercase string

s = "hero"
result = ""

for ch in s:
    if ch >= 'a' and ch <= 'z':
        result = result + chr(ord(ch) - 32)
    else:
        result = result + ch

print("Uppercase string =", result)

##2.convert uppercase string to lowercase string

s = "HERO"
result = ""

for ch in s:
    if ch >= 'A' and ch <= 'Z':
        result = result + chr(ord(ch) + 32)
    else:
        result = result + ch

print("Lowercase string =", result)

##3.display the sum od digits in given string 

s = "hero123"
total = 0

for ch in s:
    if ch >= '0' and ch <= '9':
        total = total + (ord(ch) - 48)

print("Sum of digits =", total)

##4.count the vowels in the given string

s = "Hello World"
count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count = count + 1

print("Vowel Count =", count)

##5.count the alphabets,digits,and symbols in given string

s = "hero@123"
aCount = 0
dCount = 0
sCount = 0

for ch in s:
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        aCount += 1
    elif '0' <= ch <= '9':
        dCount += 1
    else:
        sCount += 1

print("Alphabet Count =", aCount)
print("Digit Count =", dCount)
print("Symbol Count =", sCount)

##6.remove spaces from string

s = "Hello World Python"
result = ""

for ch in s:
    if ch != " ":
        result = result + ch

print("String without spaces =", result)

