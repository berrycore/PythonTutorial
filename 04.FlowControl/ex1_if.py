import datetime
now = datetime.datetime.now()

x = 10
zero = 0

if x > 0:
    print("x is larger then zero")

if zero == 0:
    print("zero equals 0")


if now.hour <= 12:
    print("A.M.")

if now.hour > 12:
    print("P.M.")



