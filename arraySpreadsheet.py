from spreadsheet.cell import Cell
from spreadsheet.baseSpreadsheet import BaseSpreadsheet
import numpy as np
import sys
import time

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class ArraySpreadsheet(BaseSpreadsheet):

    def __init__(self):
        # TO BE IMPLEMENTED
        pass

    def buildSpreadsheet(self, lCells: [Cell]):
    # def buildSpreadsheet(self):

        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        print(lCells)

        # TO BE IMPLEMENTED
        return self

    array = [[11, 12, 5, 2, 9, 10, 11], [-6.7, 6, 10], [10, 8, 12, 5], [12, 5, 8, 1]]
    spreadsheet = buildSpreadsheet(array, Cell)
    # print(spreadsheet)
    # spreadsheet.append([])
    # print(spreadsheet)

    def appendRow(self)->bool:
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # TO BE IMPLEMENTED
        print(self)
        # x = self.append([])
        # print(x)
        # # len(x)
        # if len(x) > len(self):
        #     print(True)
        # else:
        #     print(False)

        try:
            print(True)
            return self.append([])
        except:
            print(False)

        # # REPLACE WITH APPROPRIATE RETURN VALUE
        # return True
    row = appendRow(spreadsheet)
    # print(spreadsheet)


    def appendCol(self)->bool:
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # TO BE IMPLEMENTED
        try:
            print(True)
            return self[0].append(None)
        except:
            print(False)

        # REPLACE WITH APPROPRIATE RETURN VALUE
        # return new_col
    col = appendCol(spreadsheet)
    # print(spreadsheet)

    def insertRow(self, rowIndex: int) -> bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        if rowIndex <= len(self) and rowIndex >= 0:
            print(True)
            return self.insert(rowIndex -1, [])
        else:
            print(False)

        # TO BE IMPLEMENTED
        # try:
        #     print(True)
        #     return self.insert(rowIndex, [])
        # except:
        #     print(False)

        # # REPLACE WITH APPROPRIATE RETURN VALUE
        # return True

    e_row = insertRow(spreadsheet, 2)
    # print(spreadsheet)

    def insertCol(self, colIndex: int) -> bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """
        if colIndex <= len(self) and colIndex >= 0:
            print(True)
            return self[0].insert(colIndex -1, None)
        else:
            print(False)


    insert_col = insertCol(spreadsheet, 3)
    # print(spreadsheet)

    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        # TO BE IMPLEMENTED
        try:
            update_val = self[rowIndex][colIndex] = value
            print(True)


        except:
            print(False)

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return self
    print(spreadsheet)

    try:
        col_ind = int(input("What is the column index? "))
        row_ind = int(input("What is the row index? "))
        new_value = float(input("what would you like to replace it with? "))
        update_val = update(spreadsheet, row_ind, col_ind, new_value)
        print(spreadsheet)
    except:
        print("wrong value inputted, please input only integers")




    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        return len(self)

    print("Number of rows for the spreadsheet: ", rowNum(spreadsheet))


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """

        list_len = [len(i) for i in self]
        return max(list_len)

    print("Number of columns for the spreadsheet: ", colNum(spreadsheet))



    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        # TO BE IMPLEMENTED
        from collections import defaultdict
        elements = defaultdict(list)
        for row_index in range(len(self)):
            for col_index in range(len(self[row_index])):
                elements[self[row_index][col_index]].append([row_index, col_index])

        multiples = [elements[i] for i in elements if len(elements[i]) > 1 and i == value]
        print(multiples)

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return

    find(spreadsheet, 12)






    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """

        # TO BE IMPLEMENTED
        pass

        # TO BE IMPLEMENTED
        return []


    # function update
    # col_ind= int(input("What is the column index? "))
    # row_ind = int(input("What is the row index? "))
    # new_value = float(input("what would you like to replace it with? "))
    #
    # update_val = update(insert_col, row_ind, col_ind, new_value)