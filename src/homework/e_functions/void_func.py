def display_payroll_check(gross_pay, fica, federal_tax, net_pay):
    print("                  Gross Pay:      ", end="")
    print("%.2f" % gross_pay)
    print("                  FICA:           ", end="")
    print("%.2f" % fica)
    print("                  Federal Tax:    ", end="")
    print("%.2f" % federal_tax)
    print("                  Net Pay:        ", end="")
    print("%.2f" % net_pay)