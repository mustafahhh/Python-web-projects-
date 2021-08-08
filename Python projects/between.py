from datetime import date,datetime

    

def diff_month(d1, d2):
    return abs((d1.year - d2.year) * 12 + d1.month - d2.month)
while True:
    y = input("YEAR: ")
    m = input("MONTH: ")
    d = input("DAY: ")
    print("-----------2----------")
    y2 = input("YEAR: ")
    m2 = input("MONTH: ")
    d2 = input("DAY: ")
    birth = date(int(y), int(m), int(d))
    birth2 = date(int(y2), int(m2), int(d2))
    print(f'days:{abs(birth-birth2)},months:{diff_month(birth,birth2)},year:{abs(birth.year-birth2.year)}')
