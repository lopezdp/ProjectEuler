t = int(raw_input().strip())

for x in xrange(t):
	sum = 0
	n = int(raw_input().strip())

	n = n - 1

	#Need sum = (n/2) * (a1 + an)  a1 = 1st term in sequence, an = last term in sequence, n = number of terms in sequence
	term3 = n // 3
	term5 = n // 5
	term15 = n // 15
	
	sum = (3 * term3 * (term3 + 1) / 2) + (5 * term5 * (term5 + 1) / 2) - (15 * term15 * (term15 + 1) / 2)

	print sum




