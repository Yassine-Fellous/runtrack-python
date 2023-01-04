def string():
   cara = "abcdefghijklmnopqrstuvwxyz" * 10
   i = 0
   while i <= len(cara):
      j = 0
      while j <= i:
        print(cara[j], end="")
        j = j + 1
      print()
      i = i + 1
string()