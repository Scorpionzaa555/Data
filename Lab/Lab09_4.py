def insertionSort(list, last):
    current = 1
    compare = 0
    while (current <= last):
        hold = list[current]
        walker = current - 1
        compare += 1
        while (walker >= 0 and cards_list(list[walker]) > cards_list(hold)):
            list[walker+1] = list[walker]
            walker -= 1
            compare += 1
        list[walker+1] = hold
        current += 1
        if walker < 0:
            compare -= 1
        print(list)
    print(compare)

def cards_list(list):
    nums = {"2" :1, "3" :2, "4" :3, "5" :4, "6" :5, "7" :6, "8" :7, "9" :8,
            "10" :9, "J" :10, "Q" :11, "K" :12, "A" :13}
    signs = {"♣" :1, "♦" :2, "♥" :3, "♠" :4}

    lists = (nums[list[:-1]], signs[list[-1]])
    return lists

# insertionSort([23, 78, 45, 8, 32, 56], 5)
insertionSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)