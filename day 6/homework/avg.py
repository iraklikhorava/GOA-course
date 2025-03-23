#4)მოხმარებელს შემოატანინეთ რიცხვები ანუ num,num1,num2...და ასე შემდეგ და საბოლოოდ გამოითვალეთ მაგ რიცხების საშუალო არითმეტიკული
#მაგალითად 2, 2, 2 = 2 + 2 + 2 = 6 / 3 = 2 ანუ რიცხვების ჯამი გავყოთ რაოდენობაზე(მინიმუმ 3 რიცხვის ცვლადი გქონდეთ შექმნილი
num1 = int(input("Put any number: "))
num2 = int(input("Put any number: "))
num3 = int(input("Put any number: "))
num4 = int(input("Put any number: "))

numbers = [num1, num2, num3, num4]

# საშუალო არითმეტიკული გამოვთვალოთ
average = sum(numbers) / len(numbers)
print(f"შეყვანილი რიცხვების არითმეტიკული: {average}")