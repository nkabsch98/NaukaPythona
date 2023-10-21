#solution for https://leetcode.com/problems/add-two-numbers/ with normal lists
def addTwoNumbers(l1, l2):
    list1 = l1
    print(list1)
    list2 = l2
    answer = []
    rest = 0
    if len(l2) > len(l1):
        list1 = l2
        list2 = l1
    short_lenght = len(list2)
    for position, number in enumerate(list1):
        if position < short_lenght:
            answer.append((number+list2[position]+rest)%10)
            rest = (number+list2[position]+rest) // 10
        else:
            answer.append((number+rest)%10)
            rest = (number+rest) // 10
        if position == len(list1)-1 and rest != 0:
            answer.append(rest)
    return(answer)
        


print(addTwoNumbers([2,4,3],[5,6,4]))
print(addTwoNumbers([0],[0]))
print(addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))