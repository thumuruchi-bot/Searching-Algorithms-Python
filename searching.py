numbers = [10, 20, 30, 40, 50]
key = 30

for i in range(len(numbers)):
    if numbers[i] == key:
        print("Element Found at Position:", i + 1)
        break
else:
    print("Element Not Found")
