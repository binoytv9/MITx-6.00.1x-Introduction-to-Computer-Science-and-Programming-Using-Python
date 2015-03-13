a = 'asdfghjklrtyuivcxz'
l = len(a)
subStrList = [ a[i:j] for i in range(l) for j in range(i+1,l+1) if a[i:j] == ''.join(sorted(a[i:j])) ]

subStrList.sort(key=lambda x: len(x), reverse=True)

print 'Longest substring in alphabetical order is: ',subStrList[0]
