# -*- coding: utf-8 -*-

for num in range(1, 101):
    string = ''

    # ここから記述

    if(num%3 != 0 and num%5 != 0):
        string = str(num)
    else:
        #3の倍数かつ5の倍数の時、以下の二つのif文はともに実行される
        if(num%3 == 0):
            string += 'Fizz'
        if(num%5 == 0):
            string += 'Buzz'
    # ここまで記述

    print(string)

