class Sorting(object):
    def __init__(self, lst):
        self.lst = lst

    def bubble_sort(self, lst):
        n = len(lst)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
        print(lst)

    def selection_sort(self, lst):
        length = len(lst)

        for i in range(length - 1):
            minIndex = i

            for j in range(i + 1, length):
                if lst[j] < lst[minIndex]:
                    minIndex = j

            lst[i], lst[minIndex] = lst[minIndex], lst[i]
        print(lst)


if __name__ == '__main__':
    c = Sorting([13, 12, 18, 1222, 1, 5, 0])
    c.selection_sort(c.lst)
    c.bubble_sort(c.lst)