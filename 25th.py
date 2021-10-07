text='''this is a paragraph which is written just for the purpose of providing content to let the average word length be calculated'''
lst=text.split()
s=0
c=0
for i in lst:
	   s=s+len(i)
	   c=c+1
avg=s/c
print (f"The average length of word is: { avg}")

