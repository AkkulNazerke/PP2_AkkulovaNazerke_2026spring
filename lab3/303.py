s = input()

d = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3",
    "FOU": "4", "FIV": "5", "SIX": "6",
    "SEV": "7", "EIG": "8", "NIN": "9"
}

r = {v: k for k, v in d.items()}

for i in range(len(s)):
    if s[i] in "+-*":
        op = s[i]
        left = s[:i]
        right = s[i+1:]
        break

a = ""
for i in range(0, len(left), 3):
    a += d[left[i:i+3]]
a = int(a)

b = ""
for i in range(0, len(right), 3):
    b += d[right[i:i+3]]
b = int(b)

if op == "+":
    res = a + b
elif op == "-":
    res = a - b
else:
    res = a * b

if res == 0:
    print("ZER")
else:
    ans = ""
    for x in str(res):
        ans += r[x]
    print(ans)
