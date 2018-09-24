def shitty_bubblesort(ilist):
		for i in range(0, len(ilist) - 1):
				for j in range(0, len(ilist) - 2):
						if ilist[j] > ilist[j+1]:
								ilist[j+1], ilist[j] = ilist[j], ilist[j+1]

def bubble_sort(alist):
		for i in range(len(alist)):
				for j in range(len(alist)-1):
						if alist[j] > alist[i]:
								alist[j],alist[i]=alist[i],alist[j]


def insertion_sort(alist):
		for i in range(1, len(alist)):
				current_value = alist[i]
				position      = i
				while position > 0 and alist[position-1] > current_value:
						alist[position] = alist[position-1]
						position = position - 1
				alist[position] = current_value










if __name__ == '__main__':
		print("Pre-Professor-Urban's BubbleSort:")
		alist = [1, 56, 4, 11, 0, 19, 11, 55, 72, 5, 10, 15, 1, 11, 100, 3]
		print(alist)
		print("Post-Professor-Urban's BubbleSort:")
		bubblesort(alist)
		print(alist)
		print("\n")

		print("Pre-My-BubbleSort:")
		ilist = [1, 56, 4, 11, 0, 19, 11, 55, 72, 5, 10, 15, 1, 11, 100, 3]
		print(ilist)
		print("Post-My-BubbleSort:")
		bubble_sort(ilist)
		print(ilist)
		print("\n")

		print("Pre-InsertionSort:")
		slist = [1, 56, 4, 11, 0, 19, 11, 55, 72, 5, 10, 15, 1, 11, 100, 3]
		print(slist)
		print("Post-InsertionSort:")
		insertion_sort(slist)
		print(slist)
		print("\n")
