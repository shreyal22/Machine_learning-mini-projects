import random
comp_num=random.randint(1,10)
user_num=int(input('enter a number in range 1-10: '))
if comp_num==user_num:
    print('You won computer lost!!')
else:
    print('Computer won you lost!!')