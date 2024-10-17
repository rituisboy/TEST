from collections import Counter

# tests = int(input())

# for _ in range(tests):
#     s = input()
#     print(s)


s = input()

if(len(set(s))==1 and len(s)!=1):
    print()

if len(s) % 2 == 0:
    s1 = s[: (len(s) // 2 + 1)]

    s2 = s[len(s) // 2 - 1 :]
    s3 = s[: (len(s) // 2 + 2)]

    s4 = s[len(s) // 2 - 2 :]

    # print(s1, s2)

    if len(s1) == len(s) or len(s3)==len(s):
        print("NO")
    else:

        if s1 == s2 or s3 == s4:
            print("YES")
            print(s1 if s1 == s2 else s3)
        else:
            print("NO")
else:
    s1 = s[: (len(s) // 2) + 1]

    s2 = s[len(s) // 2 :]

    if len(s1) == len(s):
        print("NO")
    else:
        if s1 == s2:
            print("YES")
            print(s1)
        else:
            print("NO")
