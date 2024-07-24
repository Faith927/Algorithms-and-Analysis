# Algorithms and Analysis
Implement and test a spreadsheet using different data structures

## Objectives:
Evaluate and contrast the performance of different data structures/and or algorithms with respect to different usage scenarios and input data

## Background:
Spreadsheets are an essential application, for anyone needing to record and share tabular data. While
not the most exciting of applications, they are the workhorse of data analysis and professional services
and provide an ideal application setting for studying data structures and their efficiencies. 

### Array-Based Spreadsheet
In the array-based spreadsheet implementation, we use the Python list (a data structure) as the
basis to implement common operations for a spreadsheet. A spreadsheet is a 2D structure of cells,
and each cell can hold different data types, e.g., general, number etc. We will
concentrate on cells only holding floats. Hence to implement a spreadsheet, we will need to implement
a 2D array.

The 2D array is indexed by the tuple (row,column) in the spreadsheet. An example is if we use
numbers to index rows, and letters for columns, we might have (10,8) to specify the cell of the 11th
row, 9th column (we assume indices start at 0). 

### Doubly Linked-List-Based Spreadsheet
A linked list is a list of nodes linked together by references. In a doubly
linked list, each node consists of a data item, e.g., a string or a number, a reference that holds the
memory location of the next node in the list (the reference in the last node is set to None) and a
memory reference to the previous node in the list (the reference to the first node is set to None). Each
linked list has a head, which is the reference holding memory location of the first node in the list and
a tail reference. Once we know the head or tail of the list, we can access all nodes sequentially by
going from one node to the next using references until reaching the last node.

In the linked-list-based implementation of a spreadsheet, we use an unsorted doubly linked list.
As we need to implement a 2D structure, this needs to be a linked list of linked list. You can use the
implementation of the linked list in the workshop as a reference for your implementation. Each node
stores as data the cell contents (a float), a reference to the next node and a reference to the previous
node.

### CSR (Compressed Sparse Row) based Spreadsheet
CSR (Compressed Sparse Row) is an array based representaion used to store spreadsheets using less
space. It consists of three arrays, ColA, SumA and ValA.
Consider a spreadsheet consisting of r rows, c columns and N ZV number of cells with values in
them.

• ColA is of length N ZV and for each row, denotes which columns of cells with values in them.

• ValA is of length N ZV and for each row, denotes the values of each cell that has values in them.
ColA and ValA should have the same lengths.

• SumA is of length r + 1 and stores the cumulative sum up to the ith row. E.g., sumA[0] is the
cumulative sum up to 0th row (it should always equal 0), sumA[1] is the cumulative sum up to
the 1st row.

As an example, consider we have the following spreadsheet:

![image](https://github.com/user-attachments/assets/701a4607-825a-4104-b74e-cc96cf5c4879)

Then we would have the following arrays:

• ColA = [2, 1, 0, 2], as in row 0, column 2 has a value, for row 1, column 1, and for row 2, columns
0 and 2.

• V alA = [3, 4, 6, −2], these are the values that correspond to each cell that has a value. Note it
corresponds with the ColA array.

• SumA = [0, 3, 7, 11], as the cumulative sum up to row 0 (not including row 0) is 0, up to row 1
is 3, up to row 2 is 7 (3+4) and up to row 3, or the whole spreadsheet, is 11 (7 + 6 - 2).

From these three arrays, we are able to reconstruct the 2D spreadsheet. For example, we know
from SumA[1] that row 0 has a total of 3. We then know from ValA[0] that row 0 only contains a value
of 3, which is located in column 2 (from ColA[0]). The location of the other values in the spreadhseet
can be inferred from the three arrays.

# File Explanation:
 * spreadsheetFilebased.py  - Code that reads in operation commands from file then executes
those on the specified data structure.
* spreadsheet/cell.py - Class representing a cell in the spreadsheet
* spreadsheet/baseSpreadsheet.py - The base class for the spreadsheet implementation
* spreadsheet/arraySpreadsheet.py - Code that implements an array-based spreadsheet
* spreadsheet/linkedlistSpreadsheet.py - Code that implements an array-based spreadsheet
* spreadsheet/csrSpreadsheet.py - Code that implements a trie-based spreadsheet

# How to run:
* Clone or download repository
* Open your command window and navigate to the directory
* python spreadsheetFilebased.py csr sampleData.txt sampleCommands.in sample.out
* use python3 for Linux or python for windows
* You can change or add different txt files to test data structure quality

# Contributors 
Faith Ha & Elissa Van

# Notes:
This project was taken from RMIT's algorithm and analysis assignment 1


