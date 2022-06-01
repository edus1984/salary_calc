# SALARY CALCULATOR BASED ON WORKED HOURS

This repository contains the solution to the problem of payment calculation based on worked hours of an employee in a company. You need to have `Python 3.5` or a higher version installed.

## Installation and use
For running the program, simply clone this repository or copy the files and folders into a local folder, and run this command in a terminal from that folder:

```bash
python calc_salary.py <path/to/schedule> \[path/to/payment/table\]
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








* [Triple E - Effective Ensembling of Embeddings and Language Models for NER of Historical German](http://ceur-ws.org/Vol-2696/paper_173.pdf)

We are heavily working on better models for historic texts, so please star or watch this repository!

# Triple E - Effective Ensembling of Embeddings and Language Models for NER of Historical German

In this section we give a brief overview of how to reproduce the results from our paper.

As we heavily use Flair and Transformers for our experiments, you should find the relevant scripts in the
`experiments/clef-hipe-2020` folder:

* `word-embeddings`: includes scripts for the experiments with different word embeddings
* `flair-embeddings`: includes scripts for the experiments with different Flair embeddings
* `stacked`: combines word, Flair and Transformer-based embeddings

# Historic Language Models (Multilingual and monolingual)

For the upcoming [CLEF-HIPE 2022](https://hipe-eval.github.io/HIPE-2022/tasks) we provide several
multilingual and monolingual Historic Language Models. Please refer to the documentation [here](hlms.md).

# Changelog

* 22.03.2022: Initial version for our HIPE-2022 submission [here](experiments/clef-hipe-2022/README.md).
* 06.12.2021: Release of smaller multilingual Historic Language Models (ranging from 2-8 layers) - more information [here](hlms.md).
* 18.11.2021: Release of first multilingual and monolingual Historic Language Models - more information [here](hlms.md).
* 04.11.2021: We will take part in the upcoming [CLEF-HIPE 2022](https://hipe-eval.github.io/HIPE-2022/tasks) Shared Task.
              We plan to release new language models before the start of the official shared task very soon.
* 30.10.2021: Manually sentence-segmented Development and Test data for English was added.
* 30.11.2020: Initial version of this repository.

# Citation

You can use the following BibTeX entry for citation:

```bibtex
@inproceedings{DBLP:conf/clef/SchweterM20,
  author    = {Stefan Schweter and
               Luisa M{\"{a}}rz},
  editor    = {Linda Cappellato and
               Carsten Eickhoff and
               Nicola Ferro and
               Aur{\'{e}}lie N{\'{e}}v{\'{e}}ol},
  title     = {Triple {E} - Effective Ensembling of Embeddings and Language Models
               for {NER} of Historical German},
  booktitle = {Working Notes of {CLEF} 2020 - Conference and Labs of the Evaluation
               Forum, Thessaloniki, Greece, September 22-25, 2020},
  series    = {{CEUR} Workshop Proceedings},
  volume    = {2696},
  publisher = {CEUR-WS.org},
  year      = {2020},
  url       = {http://ceur-ws.org/Vol-2696/paper\_173.pdf},
  timestamp = {Tue, 27 Oct 2020 17:12:48 +0100},
  biburl    = {https://dblp.org/rec/conf/clef/SchweterM20.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```



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