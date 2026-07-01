test_case = [[120,130], [198,202],[4848,4848],[1,4848]]

def waveness(num1: int,num2: int)->int:
    if len(str(num1)) == len(str(num2)) <= 1:
        return 0
    ans = 0
    for num in range(num1,num2+1):
        left = 0
        number = str(num)
        for right in range(2,len(number)):
            if number[left] < number[left+1] and number[left+1] > number[right]:
                ans+=1
            elif number[left]> number[left+1] and number[left+1] < number[right]:
                ans+=1
            left+=1

    return ans
for num1,num2 in test_case:
    print(waveness(num1,num2))
