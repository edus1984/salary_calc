# SALARY CALCULATOR BASED ON WORKED HOURS

This repository contains the solution to the problem of payment calculation based on worked hours of an employee in a company. You need to have `Python 3.5` or a higher version installed.

## Installation and use
For running the program, simply clone this repository or copy the files and folders into a local folder, and run this command in a terminal from that folder:

```bash
python calc_salary.py <path/to/schedule> [path/to/payment/table]
```

Where:

* `<path/to/schedule>` *(required)* is the path to the file containing the `name` and `schedule of hours` worked by an employee. This file should contain one text line with the following format:
```
NAME=DDXX:XX-XX:XX,DDYY:YY-YY:YY,ZZ:ZZ-ZZ:ZZ
```
for instance:

*ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00*

Here, every day of the week is represented by its first two letters uppercased. Then, `MO` means *Monday*, `TU` is *Tuesday* and so on. The day is followed by the time interval, and each item is separated by a comma.
* \[path/to/payment/table\] *(optional)* is the path to a file containing the `payment structure` of the company for every day and time span. This parameter is optional, and if is ommitted a default payment table will be used. This file should contain one line per time span, indicating the amount that the company pays its employees for each worked hour in that span. The format of each line of this file is:
```
DD XX:XX XX:XX PP
```
for instance:
```
MO 00:01 09:00 25
```
This example means that for Mondays from 00:01 to 09:00 the company pays U$s for each worked hour.

## Architecture of the solution
The program consists of two classes, namely `Employee` and `PaymentStructure`, into the package `salary`.
* *Employee*: This class provides the basic methods to handle employee information objects, according to the proposed problem. An employee information object should be given a name, and provides two relevant methods for the salary calculation:
  + `set_payment_structure(PaymentStructure)`: This method establishes the payments table to use for the calculation of the salary.
  + `calculate_payment(HoursReport)`: This is the method that performs the calculation of the final payment corresponding to the employee in the related period. It makes use of the payment structure defined in the previous method, for computing the partial amounts of the time spans.
* *PaymentStructure*: The purpose of this class is to have a means to manage the different amounts to pay for different time spans. The methods this class provides are the following:
  + `extract_from_string(StringStructure)`: This method employs a default payment structure, in case there is no path provided for a payment structure file.
  + `extract_from_file(FileStructure)`: Looks for the corresponding path and loads the file for extracting the payment structure from it.
  + `compose_payment_structure(lines)`: Makes up the payment structure from an array of text lines, each one containing a time span with its amount to pay.
  + `partial_amount(day_of_week,time_interval)`: Finds the corresponding time span that includes the worked interval of hours, and calculates the product of the number of hours and the amount per hour in the payment structure.
The file *calc_salary.py* contains the main method that loads the corresponding payment structure and parses the hours report for computing the final amount.
The *draft* folder contains a Jupyter notebook that shows the first version of the solution to the main problem and the first working class structure. This is the very first approach taken to this problem.

## Approach and Methodology
The first step in the development of this solution was the loading and parsing of test files with the required format. For instance, the first iteration went through the processing of an employee schedule sample, as the one provided above for ASTRID. After that, and passing some tests every time a few lines of code were created, the next phase was interpreting and processing the payment structure concepts, understanding it as the table that covers the different hour prices for each time span and week day. The final structure was a dict, containing one entry per day of week, and each entry containing an array per time span for that day. Each time span array consists of the starting and ending time, and the amount to pay for the hours that fall into it.
Finally, following a bottom-up approach, the solution to the problem of automatically computing the amount to pay according to the schedule was written down on its first version. Then, the complete code was better structured in classes with simpler methods each one, and documented accordingly.
The final stage of this process was the development of test cases. This phase could be carried out earlier, but the rush for getting the solution working properly and other issues made it harder. Test cases for the two developed classes were built, including tests for each one of the most relevant methods.

## to-do things:
* Check intervals that belong to more than one slot: The program should separate the hours that belong to one slot and another in a schedule if that was the case, and correctly multiply each number of hours by the corresponding amount.
* Launch notifications of malformed strings: If a string could not be parsed to get payment structures or schedules, the program should tell the user about the issue without rising an exception.

# PROBLEM STATEMENT

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

Monday - Friday
00:01 - 09:00 25 USD
09:01 - 18:00 15 USD
18:01 - 00:00 20 USD

Saturday and Sunday
00:01 - 09:00 30 USD
09:01 - 18:00 20 USD
18:01 - 00:00 25 USD

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

MO: Monday
TU: Tuesday
WE: Wednesday
TH: Thursday
FR: Friday
SA: Saturday
SU: Sunday

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

Output: indicate how much the employee has to be paid

For example:

Case 1:

INPUT

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

OUTPUT:

The amount to pay RENE is: 215 USD

Case 2:

INPUT

ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:

The amount to pay ASTRID is: 85 USD
