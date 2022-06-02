from salary.Employee import Employee
from salary.PaymentStructure import PaymentStructure
import sys

if __name__ == "__main__":
    if len(sys.argv)<2:
        raise TypeError
    hours_report_file=sys.argv[1]
    #to-do: check incorrect format of text file
    #to-do: make this work for several lines: Compose complete sheet of employees and salaries            

    #Open the file that contains the hours report of the employee
    with open(hours_report_file) as f:
        lines = f.readlines()
    #Raise exception for empty or corrupted file
    if len(lines)!=1:
        raise TypeError

    #Get name of employee and hours report for processing
    [name,hours_report]=lines[0].split('=')
    emp=Employee(name)

    #Generate payment structure from file if there is a parameter indicating such file
    #Otherwise, the program uses a default payment structure
    #to-do: Notify when using default payment structure
    pay_str=PaymentStructure()
    if len(sys.argv)>2:
        pay_str.extract_from_file(sys.argv[2])
    else:
        str_payment_table="MO 00:01 09:00 25;TU 00:01 09:00 25;WE 00:01 09:00 25;TH 00:01 09:00 25;FR 00:01 09:00 25;MO 09:01 18:00 15;TU 09:01 18:00 15;WE 09:01 18:00 15;TH 09:01 18:00 15;FR 09:01 18:00 15;MO 18:01 00:00 20;TU 18:01 00:00 20;WE 18:01 00:00 20;TH 18:01 00:00 20;FR 18:01 00:00 20;SA 00:01 09:00 30;SU 00:01 09:00 30;SA 09:01 18:00 20;SU 09:01 18:00 20;SA 18:01 00:00 25;SU 18:01 00:00 25"
        pay_str.extract_from_string(str_payment_table)

    #Calculate final payment using the built payment structure
    emp.set_payment_structure(pay_str)
    final_payment=emp.calculate_payment(hours_report)
    print('The amount to pay {} is: {} USD'.format(emp.name,final_payment))