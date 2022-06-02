import unittest
from salary.Employee import Employee
from salary.PaymentStructure import PaymentStructure

class TestEmployee(unittest.TestCase):
    
	def test_calculate_payment(self):
		#Test 1: Specific case of calculus
		pay_str=PaymentStructure()
		str_payment_table="MO 00:01 09:00 25;TU 00:01 09:00 25;WE 00:01 09:00 25;TH 00:01 09:00 25;FR 00:01 09:00 25;MO 09:01 18:00 15;TU 09:01 18:00 15;WE 09:01 18:00 15;TH 09:01 18:00 15;FR 09:01 18:00 15;MO 18:01 00:00 20;TU 18:01 00:00 20;WE 18:01 00:00 20;TH 18:01 00:00 20;FR 18:01 00:00 20;SA 00:01 09:00 30;SU 00:01 09:00 30;SA 09:01 18:00 20;SU 09:01 18:00 20;SA 18:01 00:00 25;SU 18:01 00:00 25"
		pay_str.extract_from_string(str_payment_table)
		emp=Employee('RENE')
		emp.set_payment_structure(pay_str)
		hours_report='MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'
		self.assertEqual(emp.calculate_payment(hours_report),215)
		print('FIRST TEST CASE OK')
		#Test 2: Specific case of calculus
		emp2=Employee('ASTRID')
		emp2.set_payment_structure(pay_str)
		hours_report2='MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'
		self.assertEqual(emp2.calculate_payment(hours_report2), 85)
		print('SECOND TEST CASE OK')
		#Test 3: Malformed string of schedule
		emp3=Employee('DARTH VADER')
		emp3.set_payment_structure(pay_str)
		hours_report3='evening-morning,afternoon-night'
		self.assertRaises(ValueError, emp2.calculate_payment,hours_report3)
		print('THIRD TEST CASE OK')

if __name__ == "__main__":
    unittest.main()