from collections import Counter

number_of_shoes = input()
list_of_shoes = Counter(input().split())
number_of_customers = int(input())
profit = 0

while number_of_customers > 0:
    x = input().split()
    if list_of_shoes[x[0]] > 0:
        list_of_shoes[x[0]] -= 1
        x[1] = int(x[1])
        profit += x[1]
    number_of_customers -= 1

print(profit)