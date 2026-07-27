import random
secret = random. randint (1,100)
tries=0
print('عدد انتخاب شده را حدس بزن')
while True:
    guess = int(input('حدس تو'))
    tries = tries + 1
    if guess < secret:
        print ('بزرگتر حدس بزن')
    elif guess > secret:
        print ('کوچکتر حدس بزن')
    else:
        print (' آفرین درست حدس زدی')
        print ( 'تعداد تلاش هات' , tries)
        break