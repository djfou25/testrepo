sum=0
count=0
while True:
    try:
        num=input('Enter a number: ')
        if num!='done':
            inum=int(num)
            sum=sum+inum
            count=count+1
        else:
            print(sum,count,sum/count)
            break
    except:
        print('Invalid input')
