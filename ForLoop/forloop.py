start_number = input("please enter your start number")
end_number = input("please enter you end number")
decrement_val = input("Enter by what value you want to decrement")
if int(decrement_val) < 0 and int(start_number) != int(end_number):
    if int(start_number) > 0 and int(start_number) > int(end_number):
        for i in range(int(start_number), int(end_number), int(decrement_val)):
            print(i)
    elif int(start_number) < 0 and int(start_number) > int(end_number):
        for i in range(int(start_number), int(end_number), int(decrement_val)):
            print(i)
    else:
        print("Either end value is grater than start value for positive input ")
else:
    print("Cannot Decrement with positive value or cannot decrement from 0 to 0")
