def find(s):
    for i in range(1, len(s)):
        if s[i] in s[0:i]:
            if s[0:i] == s[i:2*i]:
                if len(s) % len(s[0:i]) == 0:
                    times = int(len(s) / len(s[0:i]))
                    if s == s[0:i] * times:
                        return len(s[0:i])

    return len(s)


if __name__ == "__main__":
  print(find("aaa")) # 1
  print(find("abcd")) # 4
  print(find("abcabcabcabc")) # 3
  print(find("aybabtuaybabtu")) # 7
  print(find("abcabca")) # 7
  print(find("mmzxzj")) #6