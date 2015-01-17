# Paste your code into this box 
s ='soobobla'
#s = 'vbobbbobbobboboowobobozxoboobbobbowbbobbbobobboob'
count = 0
for i in range(len(s)):
    if s.find('bob',i,i+len('bob')) != -1:
        count += 1

print 'Number of times %s occurs is: %d' %(s,count)
