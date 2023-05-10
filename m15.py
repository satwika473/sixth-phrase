numbers = input("Enter comma-separated numbers: ").split(",")
squared_odds = [int(num)**2 for num in numbers if int(num) % 2 != 0]
print(",".join(str(num) for num in squared_odds))
