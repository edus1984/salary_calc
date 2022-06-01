class Employee:
    def __init__(self,name):
        self.name=name
    
    def set_payment_structure(self,payment_structure):
        self.payment_structure=payment_structure
    
    def calculate_payment(self,str_hours_report):
        final_payment=0
        items=str_hours_report.split(',')
        #to-do: test malformed string
        for item in items:
            day_of_week=item[0:2]
            time_interval=item[2:]
            final_payment+=self.payment_structure.partial_amount(day_of_week,time_interval)
        return final_payment