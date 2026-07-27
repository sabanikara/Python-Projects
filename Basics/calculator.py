print('ماشین حساب ساده')
print('عملیات‌های مجاز: +  -  *  /')
print('برای خروج بنویس: exit')

while True:
    # گرفتن عملیات
    operation = input('عملیات را وارد کن (+ - * / یا exit): ')

    # اگر خواست خارج بشه
    if operatin == 'exit':
        print('خداحافظ!')
        break

    # گرفتن دو عدد
    num1 = float(input('عدد اول: '))
    num2 = float(input('عدد دوم: '))

    # محاسبه با if-elif-else
    if operation == '+':
        result = num1 + num2
        print('نتیجه:', result)

    elif operation == '-':
        result = num1 - num2
        print('نتیجه:', result)

    elif operation == '*':
        result = num1 * num2
        print('نتیجه:', result)

    elif operation == '/':
        if num2 == 0:
            print('خطا! تقسیم بر صفر ممکن نیست')
        else:
            result = num1 / num2
            print('نتیجه:', result)

    else:
        print('عملیات نامعتبر! فقط + - * / رو وارد کن')