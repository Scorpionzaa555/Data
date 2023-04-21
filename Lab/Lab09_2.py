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
#####################
def selectionSort(list, last):
    current = 0
    compare = 0
    while current < last:
        smallest = current
        walker = current+1
        while walker <= last:
            if cards_list(list[walker]) <= cards_list(list[smallest]):
                smallest = walker
            walker += 1
            compare += 1
        list[current], list[smallest] = list[smallest], list[current]
        current += 1
        print(list)
    print("Comparison times: " , compare)
####################
def bubbleSort(list, last):
    current = 0
    compare = 0
    sort = False
    while (current <= last) and (sort == False):
        walker = last
        sort = True
        while walker > current:
            if cards_list(list[walker]) < cards_list(list[walker-1]):
                sort = False
                list[walker], list[walker-1] = list[walker-1], list[walker]
            walker -=1
            compare += 1
        current += 1
        print(list)
    print("Comparison times: " , compare)
#####################
def cards_list(list):
    nums = {"2" :1, "3" :2, "4" :3, "5" :4, "6" :5, "7" :6, "8" :7, "9" :8,
            "10" :9, "J" :10, "Q" :11, "K" :12, "A" :13}
    signs = {"♣" :1, "♦" :2, "♥" :3, "♠" :4}

    lists = (nums[list[:-1]], signs[list[-1]])
    return lists

insertionSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
selectionSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
bubbleSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
