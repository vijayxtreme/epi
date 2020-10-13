num1 = [1,2,3]
num2 = [-4,5,6]
def multiply(num1, num2):
    #Check both signs of each row -- if both numbers are neg, pos
    sign = -1 if (num1[0]<0) ^ (num2[0]<0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    #Make an array of 0s using num1 * num2 length
    result = [0]*(len(num1) + len(num2))

    # Go thru both num arrays and multiply the nums
    # store the result at i+j+1 in the result array
    # if the result of i+j is an int, e.g 1, put that in front
    # mod the remainder of i+j+1 (e.g. 15) and set it to 5
    # Loop until all i+j combinations are done and place 
    # appropriately in new result array
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i+j+1] += num1[i] * num2[j]
            result[i+j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10
            print(result[i+j+1])

    # Remove any zeroes that came from int div, we don't need them
    # return 0 if all 0s --> we multiplied by 0.
    result = result[next((i for i, x in enumerate(result) if x!=0), len(result)):] or [0]
    # final result should just be basic mult
    return [sign * result[0]] + result[1:]

print(multiply(num1, num2))