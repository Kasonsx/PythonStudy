def quicksort(seq):
	if seq == []:
		return []
	else:
		refer = seq[0]
		less = quicksort([x for x in seq[1:] if x < refer])
		greater = quicksort([x for x in seq[1:] if x >= refer])
		return less+[refer]+greater

if __name__ == '__main__':
	seq = [5,6,78,9,0,-1,2,3,-65,12]
	print(quicksort(seq))

