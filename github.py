def mostFrequentLetter(s):
	s=s.lower()
	s=s.replace(" ","")
	count=0
	frequent=""
	for i in range(1, len(s)):
		if s.count(s[i])>=count:
			count=s.count(s[i])
			frequent=s[i]
	return frequent

print(mostFrequentLetter("We will attack at dawn"))
assert(mostFrequentLetter("hii")=="i")
assert(mostFrequentLetter("wow")=="w")