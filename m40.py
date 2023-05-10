t = (1,2,3,4,5,6,7,8,9,10)
n = len(t)
first_half = t[:n//2]
last_half = t[n//2:]

print("First half:", " ".join(map(str, first_half)))
print("Last half:", " ".join(map(str, last_half)))
