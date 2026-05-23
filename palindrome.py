def upper(s):
    res = ""
    for ch in s:
        asci = ord(ch)
        if asci >= 65 and asci <= 90:
            res = res + ch
        else:
            res = res + chr(asci-32)
    return res

s = "A man a plan a canal Panama"
print(s)
s1 = s.lower()
print(s1)


if s==s:
    print("True")
elif s!=s:
    print("False")

