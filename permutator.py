global count
count = 0
def permute_recursive (till_now, left):
	global count
	if left == "":
		print till_now
	else:
		for i in range (len(left)-1):
			done = till_now + left[i]
			remaining = left[0:i] + left[i+1]
			print "Recursion count: %r" %count
			print "Done: %s" %done
			print "Remaining: %s" %remaining
			permute_recursive (done, remaining)
		print
	count += 1	
			
def permute (s):
	permute_recursive ("", s)
	
def subsets_recursive (till_now, left):
	if left == "":
		print till_now
	else:
		subsets_recursive(till_now+left[0], left[1:len(left)])
		subsets_recursive(till_now, left[1:len(left)])
		
def subsets (s):
	subsets_recursive ("", s)
