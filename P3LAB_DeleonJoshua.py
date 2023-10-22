def is_leap_year(user_year):
   is_leap = True
   if (user_year % 4) == 0:
       if (user_year % 100) == 0:
           if (user_year % 400) == 0:
               is_leap = True
           else:
               is_leap = False
       else:
           is_leap = True
   else:
       is_leap = False
   return is_leap
year = int(input())
if is_leap_year(year):
   print(str(year) + ' - leap year')
else:
   print(str(year) + ' - not a leap year')