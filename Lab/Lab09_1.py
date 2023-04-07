def insertionSort(list, last):
    compare = 0
    current = 1

    while(current <= last):
        hold = list[current]
        walker = current - 1
        compare += 1

        while(walker >= 0 and hold < list[walker]):
            # move walker element right one element
            list[walker + 1] = list[walker]
            walker -= 1
            compare += 1

        # move hold to walker + 1
        list[walker + 1] = hold
        current += 1
        if(walker < 0):
            compare -= 1
        print(list)
    print("Comparison times:", compare)

insertionSort([23, 78, 45, 8, 32, 56], 5)
