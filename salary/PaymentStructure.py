class PaymentStructure:
    #The complete payment structure can be in a string separate by semi-colon
    def extract_from_string(self,str_payment_structure):
        self.compose_payment_structure(str_payment_structure.split(';'))
    
    #Allow the payment structure to arise in a file
    def extract_from_file(self,filePaymentStructure):
        #to-do: check incorrect format of text file
        with open(filePaymentStructure) as f:
            lines = f.readlines()
        self.compose_payment_structure(lines)
        
    #From file or string, payment structure should be an array of text lines
    #Expected format of each line: 'MO 00:01 09:00 25' (day_of_week, start, end, amount_in_dollars)
    def compose_payment_structure(self,lines):
        self.payment_structure=dict()
        for line in lines:
            #Extract and convert values in each line
            [day,str_start_time,str_end_time,str_price]=line.strip().split(' ')
            start_time=int(str_start_time.split(':')[0])
            end_time=int(str_end_time.split(':')[0])
            price=int(str_price)
            #Update the structure of the day of week:
            #Add time intervals with amounts
            if not day in self.payment_structure:
                self.payment_structure[day]=[]
            self.payment_structure[day].append([start_time,end_time,price])
        
    #Returns the amount in dollars for a day_of_week and time interval
    #Format of day_of_week: 'MO' or 'TU' or 'WE'...
    #Format of time_interval: '09:00-11:00' (start_time-end_time)
    def partial_amount(self,day_of_week,time_interval):
        [str_start_time,str_end_time]=time_interval.split('-')
        #to-do: check if end is greater than start
        #to-do: check minutes into hours (what if half an hour? or a couple of minutes?)
        start_time=int(str_start_time.split(':')[0])
        end_time=int(str_end_time.split(':')[0])
        #Check if there exists an interval containing the time span
        for time_span in self.payment_structure[day_of_week]:
            span_start=time_span[0]
            span_end=time_span[1]
            #In case we have a span like 18:00-00:00 or 21:00-04:00
            #add 24 to the end_time
            if (span_end<span_start):
                span_end+=24
            if start_time>=span_start and start_time<span_end:
                #to-do: check intervals that belong to more than one slot
                hours=end_time-start_time
                payment_per_hour=time_span[2]
                return hours*payment_per_hour