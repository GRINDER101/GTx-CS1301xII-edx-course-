# Write a function called what_season. what_season should
# have two parameters: the first a string representing
# a month, and the second an integer representing a day.
#
# what_season should return "Spring" if the date is in
# Spring, "Summer" if it's in Summer, "Fall" if it's in
# Fall, and "Winter" if it's in Winter.
#
# For this problem, we define those seasons as follows:
#
# - Spring starts March 20.
# - Summer starts June 21.
# - Fall starts September 22.
# - Winter starts December 21.
#
# So, March 20 to June 20 would be Spring; June 21 to
# September 21 would be Summer; September 22 to December
# 20 would be Fall; and December 21 to March 19 would be
# Winter.


# Add your code here!
def what_season(a_month, a_day):
    if (a_month == "March" and a_day >= 20) or (a_month == "April" and a_day >= 1) or (a_month == "May" and a_day >= 1) or (a_month == "June" and a_day <= 20):
        return "Spring"
    elif (a_month == "June" and a_day >= 21) or (a_month == "July" and a_day >= 1) or (a_month == "August" and a_day >= 1) or (a_month == "September" and a_day <= 21):
        return "Summer"
    elif (a_month == "September" and a_day >= 22) or (a_month == "October" and a_day >= 1) or (a_month == "November" and a_day >= 1) or (a_month == "December" and a_day <= 21):
        return "Fall"
    else:
        return "Winter"


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print Winter, Spring, Summer, and Fall in that order.
print(what_season("December", 25))
print(what_season("June", 15))
print(what_season("June", 23))
print(what_season("September", 27))
