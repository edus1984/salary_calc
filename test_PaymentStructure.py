import unittest
from salary.PaymentStructure import PaymentStructure
from salary.Employee import Employee


class TestPaymentStructure(unittest.TestCase):
    
	def test_partial_amount(self):
		#Test 1: Specific case of partial amount
		pay_str=PaymentStructure()
		str_payment_table="MO 00:01 09:00 25;TU 00:01 09:00 25;WE 00:01 09:00 25;TH 00:01 09:00 25;FR 00:01 09:00 25;MO 09:01 18:00 15;TU 09:01 18:00 15;WE 09:01 18:00 15;TH 09:01 18:00 15;FR 09:01 18:00 15;MO 18:01 00:00 20;TU 18:01 00:00 20;WE 18:01 00:00 20;TH 18:01 00:00 20;FR 18:01 00:00 20;SA 00:01 09:00 30;SU 00:01 09:00 30;SA 09:01 18:00 20;SU 09:01 18:00 20;SA 18:01 00:00 25;SU 18:01 00:00 25"
		pay_str.extract_from_string(str_payment_table)
		self.assertEqual(pay_str.partial_amount('TU','09:00-14:00'),75)
		print('FIRST TEST CASE OK')
		#Test 2: Specific case of calculus
		self.assertEqual(pay_str.partial_amount('SU','18:00-21:00'),75)
		print('SECOND TEST CASE OK')
		#Test 3: Malformed string of payment structure
		str_payment_table2="MO00:01 09:00 25;TU 00:01 09:00 25;WE 00:01 09:00 25;TH 00:01 09:00 25;FR 00:01 09:00 25;MO 09:01 18:00 15;TU 09:01 18:00 15;WE 09:01 18:00 15;TH 09:01 18:00 15;FR 09:01 18:00 15;MO 18:01 00:00 20;TU 18:01 00:00 20;WE 18:01 00:00 20;TH 18:01 00:00 20;FR 18:01 00:00 20;SA 00:01 09:00 30;SU 00:01 09:00 30;SA 09:01 18:00 20;SU 09:01 18:00 20;SA 18:01 00:00 25;SU 18:01 00:00 25"
		self.assertRaises(ValueError, pay_str.extract_from_string,str_payment_table2)
		print('THIRD TEST CASE OK')

if __name__ == "__main__":
    unittest.main()