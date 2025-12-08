'''
any number that is repeating like 1010, 11 are invalid 
so the task is to get the count of all the number which has repeating sequence 

thoughts:"

digits repeated twice so any number with even number of digits are possibiliy our search , also 
'''
def total(start,end):
    count = 0
    sum = 0
    for i in range(start,end+1):
        num = str(i)
        l = len(num)
        if l&1 == 1:
            continue
        if num[:l//2] == num[l//2:]:
            sum+=int(num)
            count+=1
    return count,sum
'''
string = "
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"

    '''
string="78847-119454,636-933,7143759788-7143793713,9960235-10043487,44480-68595,23468-43311,89-123,785189-1014654,3829443354-3829647366,647009-692765,2-20,30-42,120909-197026,5477469-5677783,9191900808-9191943802,1045643-1169377,46347154-46441299,2349460-2379599,719196-779497,483556-641804,265244-450847,210541-230207,195-275,75702340-75883143,58-84,2152-3237,3367-5895,1552-2029,9575-13844,6048-8966,419388311-419470147,936-1409,9292901468-9292987321"

list_s = string.rstrip().lstrip().split(',')
totally = 0
total_sum = 0
for s in list_s:
    count,sum =total(int(s.split('-')[0]),int(s.split('-')[-1]))
    totally+=count
    total_sum+=sum
print(totally,total_sum)

