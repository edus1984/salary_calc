class Employee:
    #Constructor with name assignment
    def __init__(self,name):
        self.name=name
    
    #Payment structure contains the amount to pay each hour and day
    def set_payment_structure(self,payment_structure):
        self.payment_structure=payment_structure
    
    #Compute the total amount to pay employee given schedule
    #Example of schedule: 'MO 10:00-12:00,TH 09:00-11:00'
    def calculate_payment(self,str_hours_report):
        final_payment=0
        #Separate items of hours and days using comma
        items=str_hours_report.split(',')
        #to-do: test and notify malformed string
        for item in items:
            day_of_week=item[0:2]
            time_interval=item[2:]
            #Final amount for item: num_hours*pay_per_hour
            final_payment+=self.payment_structure.partial_amount(day_of_week,time_interval)
        return final_payment