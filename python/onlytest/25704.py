coupon = int(input(""))
price = int(input(""))

if 5 <= coupon and coupon <= 9:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    if price-500 <= 0:
        print(0)
    else:
        print(price-500)

elif 10 <= coupon and coupon <= 14:
    if int(price*0.9) > price-500:    
        if price-500 <= 0:
            print(0)
        else:
            print(price-500)
    else:
        print(int(price*0.9))

elif 15 <= coupon and coupon <= 19:
    if int(price*0.9) > price-2000:
        if price-2000 <= 0:
            print(0)
        else:
            print(price-2000)
    else:
        print(int(price*0.9))

elif 20 <= coupon:
    if int(price*0.75) > price-2000:    
        if price-2000 <= 0:
            print(0)
        else:
            print(price-2000)
    else:
        print(int(price*0.75))
else:
    print(price)