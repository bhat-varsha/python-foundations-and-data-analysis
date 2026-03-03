#to find the sum of squares upto infinity
#infinity is not possible to perform
n=int(input("enter the number upto  u want sums:  "))
sum_of_seq=0 # for starting wll take 0
for i in range(1,n+1):
    sum_of_seq=sum_of_seq+i**i
    print(f'each step in loop the sum of square is {sum_of_seq}')
print(f'the sum of square is {sum_of_seq}')

count=int(input("upto which number?   "))
total_sum=0
for number in range(1,count+1):
    total_sum=total_sum+number**number
print(f'the sum is {sum}')


