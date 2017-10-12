from timeit import default_timer as timer
import random

def findMindex(ar, j):
	min = ar[j]
	index = j
	for i, item in enumerate(ar, j):
		if (item < min):
			min, index = item, i
	return index

def selectionSort(ar):
	for i in range(len(ar)):
		j = findMindex(ar, i)
		ar[i], ar[j] = ar[j], ar[i]
	return ar

def bubbleSort(ar):
	for i in range(len(ar)):
		for j in range(len(ar)):
			if (ar[j] > ar[i]):
				ar[i], ar[j] = ar[j], ar[i]
	return ar

def quickSort(ar):
	greaterThan = []
	equalTo = []
	lessThan = []

	if len(ar) > 1:
		pivot = ar[round(len(ar)/2)]
		for item in ar:
			if item > pivot:
				greaterThan.append(item)
			elif item == pivot:
				equalTo.append(item)
			else:
				lessThan.append(item)
		return quickSort(lessThan) + equalTo + quickSort(greaterThan)
	else:
		return ar

if __name__ == '__main__':
	ar = []
	for i in range(1000):
		ar.append(random.randint(-500,500))

	start = timer()
	bubbleSort(ar)
	end = timer()
	print(end-start)

	start = timer()
	selectionSort(ar)
	end = timer()
	print(end-start)

	start = timer()
	quickSort(ar)
	end = timer()
	print(end-start)
