import random

def unix_time_to_human_readable(seconds):
    # https://www.geeksforgeeks.org/convert-unix-timestamp-to-dd-mm-yyyy-hhmmss-format/
    # Unix time is in seconds and
    # Human Readable Format:
    # DATE:MONTH:YEAR:HOUR:MINUTES:SECONDS,
    # Start of unix time:01 Jan 1970, 00:00:00

    # Function to convert unix time to
    # Human readable format:

    # Save the time in Human
    # readable format
    ans = ""

    # Number of days in month
    # in normal year
    days_of_month = [31, 28, 31, 30, 31, 30,
                   31, 31, 30, 31, 30, 31]

    (curr_year, days_till_now, extra_time,
     extra_days, index, date, month, hours,
     minutes, seconds_myp, flag) = (0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0)

    # Calculate total days unix time T
    days_till_now = seconds // (24 * 60 * 60)
    extra_time = seconds % (24 * 60 * 60)
    curr_year = 1970

    # Calculating current year
    while days_till_now >= 365:
        if curr_year % 400 == 0 or (curr_year % 4 == 0 and curr_year % 100 != 0):
            if days_till_now < 366:
                break
            days_till_now -= 366

        else:
            days_till_now -= 365

        curr_year += 1

    # Updating extra days because it
    # will give days till previous day
    # and we have included current day
    extra_days = days_till_now + 1

    if (curr_year % 400 == 0 or
        (curr_year % 4 == 0 and
            curr_year % 100 != 0)):
        flag = 1

    # Calculating MONTH and DATE
    month = 0
    index = 0

    if flag == 1:
        while True:

            if index == 1:
                if extra_days - 29 < 0:
                    break

                month += 1
                extra_days -= 29

            else:
                if extra_days - days_of_month[index] < 0:
                    break

                month += 1
                extra_days -= days_of_month[index]

            index += 1

    else:
        while True:
            if extra_days - days_of_month[index] < 0:
                break

            month += 1
            extra_days -= days_of_month[index]
            index += 1

    # Current Month
    if extra_days > 0:
        month += 1
        date = extra_days

    else:
        if month == 2 and flag == 1:
            date = 29
        else:
            date = days_of_month[month - 1]

    # Calculating HH:MM:YYYY
    hours = extra_time // 3600
    minutes = (extra_time % 3600) // 60
    seconds_myp = (extra_time % 3600) % 60

    # Print time in format
    # DD:MM:YYYY:HH:MM:SS
    ans += str(date)
    ans += "/"
    ans += str(month)
    ans += "/"
    ans += str(curr_year)
    ans += " "
    ans += str(hours)
    ans += ":"
    ans += str(minutes)
    ans += ":"
    ans += str(seconds_myp)

    # Return the time
    return ans


# Find minimum in a list
def myp_min(myp_list):
    minim = myp_list[0]
    for i in range(len(myp_list)):
        if minim > myp_list[i]:
            minim = myp_list[i]
    return minim


# Driver code
if __name__ == "__main__":

    # Given unix time
    T = 1595497956

    # Function call to convert unix
    # time to human read able
    answe = unix_time_to_human_readable(T)

    # list of random number of random numbers
    myp_list_act = []
    for i in range(random.randint(5, 20)):
        myp_list_act.append(random.randint(-100, 100))

    print(" part1:", answe, '\n', "part2:")
    print("Исходный список: " + str(myp_list_act) + "\n")

    print("Если массив не отсортирован")
    print("Минимальное число, сложность = O(n): " + str(myp_min(myp_list_act)) + "\n")

    print("Если массив отсортирован")
    myp_list_act = sorted(myp_list_act)
    print(myp_list_act)
    print("Минимальное число, сложность = O(1): " + str(myp_list_act[0]) + "\n")
