#This is sum_pairs where the target is 5 we want to add the elements which get as 5 and want to make in separate list

arr = [1,2,3,4,5]
target = 5
result = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):

        if arr[i] + arr[j] == target:

            first = arr[i]
            second = arr[j]

            if first > second:
                temp = first
                first = second
                second = temp

            duplicate = False

            for pair in result:
                if pair[0] == first and pair[1] == second:
                    duplicate = True
                    break

            if duplicate == False:
                result.append([first, second])

print("Pairs:", result)