from collections import Counter
import os

os.system('cls')

values = [1, 4, 6, 4, 8]  #lista

most_common_numbers = Counter(values)

most_common = most_common_numbers.most_common(1)[0]

print("mest vanlig:", most_common[0])
print("hur många av den mest vanliga:", most_common[1])


most_common_letters = Counter("abcbadfbcb").most_common(3)
print(most_common_letters)
