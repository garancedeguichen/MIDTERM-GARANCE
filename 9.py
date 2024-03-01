def days_since_birthday():
    """
    Asks the user for their birthday and calculates how many days have passed since that date,
    excluding the days in the birth year and the current year.
    """
    # On what day-month-year was the user born?
    birthday = input("Please enter your birthday in the format 'DD-MM-YYYY': ")

    # Split the birthday string into day, month, and year
    day, month, year = map(int, birthday.split('-'))

    # Current year
    current_year = 2024

    # Calculate the total number of days between the birth year and the current year, excluding both. I substracted 2 since the day the user was born isn't suppose to count and today's day neither.
    total_days = (current_year - year - 2) * 365

    # Subtract the days in the birth month and birth year: in my case, after the 20-08-2004, how many days were left in 2004 after my birth.
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days -= day
    total_days -= sum(days_in_month[month - 1:])

    # Adjust for leap year if the birth month is February and it's a leap year
    if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        total_days -= 1

    print("Days since your birthday, excluding the days in your birth year and the current year, are:", total_days)

days_since_birthday()