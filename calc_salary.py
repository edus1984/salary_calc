from salary.Employee import Employee
from salary.PaymentStructure import PaymentStructure
import sys

if __name__ == "__main__":
    if len(sys.argv)<2:
        raise TypeError
    hours_report_file=sys.argv[1]
    #to-do: check incorrect format of text file
    #to-do: make this work for several lines: Compose complete sheet of employees and salaries            
    with open(hours_report_file) as f:
        lines = f.readlines()
    if len(lines)!=1:
        raise TypeError
    [name,hours_report]=lines[0].split('=')
    emp=Employee(name)

    pay_str=PaymentStructure()
    if len(sys.argv)>2:
        pay_str.extract_from_file(sys.argv[2])
    else:
        str_payment_table="MO 00:01 09:00 25;TU 00:01 09:00 25;WE 00:01 09:00 25;TH 00:01 09:00 25;FR 00:01 09:00 25;MO 09:01 18:00 15;TU 09:01 18:00 15;WE 09:01 18:00 15;TH 09:01 18:00 15;FR 09:01 18:00 15;MO 18:01 00:00 20;TU 18:01 00:00 20;WE 18:01 00:00 20;TH 18:01 00:00 20;FR 18:01 00:00 20;SA 00:01 09:00 30;SU 00:01 09:00 30;SA 09:01 18:00 20;SU 09:01 18:00 20;SA 18:01 00:00 25;SU 18:01 00:00 25"
        pay_str.extract_from_string(str_payment_table)
    emp.set_payment_structure(pay_str)
    final_payment=emp.calculate_payment(hours_report)
    print('The amount to pay {} is: {} USD'.format(emp.name,final_payment))