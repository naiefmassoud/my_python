#!/usr/bin/env python3

# Cost per hour, day, and month
cost = 0.51
cost_day = cost * 60
cost_month = cost_day * 30

# How much does it cost to operate 20 servers a day
cost_day_twenty = cost_day * 20

# How much does it cost to operate 20 servers a month
cost_month_twenty = cost_month * 20

# How many days can I operate one server with $918
cost_price = 918 / cost_day
price_day  = int(cost_price)

print('Based on an hourly cost of: $' + str(cost))
print('Server cost on the cloud per day is: ${:.2f}'.format(cost_day)) # Display this one with 2 floating points
print('Server cost on the cloud per month is: $' + str(cost_month))
print('Operating 20 servers per day: $' + str(cost_day_twenty))
print('Operating 20 servers per month: $' + str(cost_month_twenty))
print('How many days for $918? ' + str(price_day) + ' days.')
