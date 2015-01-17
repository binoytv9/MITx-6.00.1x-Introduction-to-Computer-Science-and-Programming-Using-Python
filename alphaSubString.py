i = 1
sub = s[0]
new = []

while i < len(s):
	if s[i-1] <= s[i]:
		sub += s[i]
	else:
		new.append(sub)
		sub = ''
		sub += s[i]
	i += 1
new.append(sub)
new.sort(key = lambda x: len(x),reverse = True)

print 'Longest substring in alphabetical order is: ',new[0]
