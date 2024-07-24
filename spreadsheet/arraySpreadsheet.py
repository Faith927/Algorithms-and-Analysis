from spreadsheet.cell import Cell
from spreadsheet.baseSpreadsheet import BaseSpreadsheet
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
        self.table = []  # initializing the class

    def buildSpreadsheet(self, lCells: [Cell]):

        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        # finding the max number of rows and columns
        max_row = max([item.row for item in lCells])
        max_col = max([item.col for item in lCells])

        # creating a 2D array with None as the values
        table = [[None] * (max_col + 1) for _ in range(max_row + 1)]

        # adding values into the 2D array if the index and column number match up
        for item in lCells:
            table[item.row][item.col] = item.val
        self.table = table  # initializing the table



    def appendRow(self)->bool:
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        try:
            # appends an empty row to the bottom of the spreadsheet
            max_len = len(self.table[0])
            self.table.append([None] * max_len)
            return True
        except NameError:
            # if table cannot be found, returns False
            return False


    def appendCol(self)->bool:
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        try:
            # appends None to the end of each individual list
            for elements in self.table:
                elements.append(None)
            return True
        except:
            return False

    def insertRow(self, rowIndex: int) -> bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        # makes sure rowIndex is valid and appends a list with the length of the biggest row
        if 0 <= rowIndex <= len(self.table):
            max_len = len(self.table[0])
            self.table.insert(rowIndex, [None] * max_len)
            return True
        # appends row to the end of each list
        elif rowIndex == -1:
            max_len = len(self.table[0])
            self.table.insert(-1, [None] * max_len)
        else:
            return False


    def insertCol(self, colIndex: int) -> bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """
        # inserts None in the colIndex position for each list
        num = []
        for item in self.table:
            num.append(len(item))
        n = max(num)
        if n >= colIndex >= 0:  # making sure the colIndex is a valid number
            for element in self.table:
                element.insert(colIndex, None)
            return True
        elif colIndex == -1:          # inserts None at the end of each list
            for element in self.table:
                element.insert(-1, None)
        else:
            return False


    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        # uses the rowIndex and colIndex to find and replace the value
        try:
            self.table[rowIndex][colIndex] = value
            return True
        except:
            return False

    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        return len(self.table)  # returning the number of lists in the 2D array

    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        list_len = [len(i) for i in self.table]  # finding the length of the elements in the 2D array
        return max(list_len)  # returning the max number found

    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """
        val_list = []
        # enumerating through the 2D array to find the row index and the row values
        for r_inx, row in enumerate(self.table):
            for c_inx, col in enumerate(row):
                if col == value:
                    print(r_inx, c_inx)
                    val_list.append((r_inx, c_inx))  # appending row index and column index to val_list
        return val_list

    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """
        values = []
        # appends row and column index if value found
        for r_inx, row in enumerate(self.table):
            for c_inx, col in enumerate(row):
                if col != None:
                    values.append((r_inx, c_inx, col))  # appending row and column index to values
        return values