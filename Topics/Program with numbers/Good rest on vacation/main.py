duration = int(input())
daily_food = int(input()) * duration
flights = int(input()) * 2 
hotel = int(input()) * (duration - 1)
print(daily_food + flights + hotel)
