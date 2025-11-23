FICA_RATE = 765
FEDERAL_RATE = 800

def get_gross_pay(hours, rate):
    if hours > 40:
        overtime_hours = hours - 40
        gross_pay = (40 * rate) + (overtime_hours * rate * 3 // 2)
    else:
        gross_pay = hours * rate
    return gross_pay


def get_fica_tax(gross_pay):
    return gross_pay * FICA_RATE // 10000


def get_federal_tax(gross_pay):
    return gross_pay * FEDERAL_RATE // 10000