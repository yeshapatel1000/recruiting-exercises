Files in the folder:

1. warehouse.py
2. test.txt

warehouse.PY

The file takes input from the test.txt file. The input data is converted to JSON and processed to get the results. The output is matched against the output mentioned in the test.txt file. For correct output, TESTCASE PASSED message is written to th eoutput file. Otherwise TESTCASE FAILED message is wriiten to the output file.

All the logs are maintained in the logs folder. The logs are named as the timestamp of the runtime of the file.

test.txt

All the test cases are written in the file. 
1. First line in the file is the input
2. Second line is the required or the expected output.

Each test case along with input and output are separated by a "-------" line.

To add test cases, user needs to add input and expected output.

HOW TO RUN

Go in "recruiting-exercises-master\inventory-allocator\src" directory
To run the tests, use command python3 warehouse.py



