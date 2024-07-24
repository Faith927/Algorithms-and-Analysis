from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell


# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class Node:
    def __init__(self, cell=None):
        self.cell = cell
        self.next = None  # reference to the next node in the same column
        self.prev = None  # reference to the previous node in the same column
        self.down = None  # reference to the node below in the same row
        self.up = None  # reference to the node above in the same row

class LinkedListSpreadsheet(BaseSpreadsheet):

    def __init__(self, num_rows=0, num_cols=0, defaultValue=None):
        # TO BE IMPLEMENTED
        self.head = Node(None)
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.data = {}
        self.defaultValue = defaultValue
        self.spreadsheet = [[defaultValue for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        self.cells = [[Cell(None) for _ in range(self.num_cols)] for _ in range(self.num_rows)]

    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        self.num_rows = max(cell.row for cell in lCells) + 1  # max row number
        self.num_cols = max(cell.col for cell in lCells) + 1  # max column number

        if not lCells:
            return False

        self.head.cell = Cell(-1, -1, None)

        curr_row = self.head  # initialising head reference for column header node
        prev_node = None

        # Create the first row and column headers
        for i in range(self.num_cols):
            new_node = Node(Cell(0, i, None))
            curr_row.next = new_node  # previous node (current head) points to the next new node in the same column
            new_node.prev = curr_row  # new node's previous pointer points back to previous node
            curr_row = new_node  # current pointer is now on the new node

        curr_col = self.head  # initialising head reference for row header node

        for i in range(self.num_rows):
            new_node = Node(Cell(i, 0, None))
            curr_col.down = new_node  # previous node (current head) points down to the new node in the same row
            new_node.up = curr_col  # new node's previous pointer points back up to reference previous node
            curr_col = new_node

        # Add the remaining cells
        for cell in lCells:
            #row, col, val = cell
            # Traverse to the correct row
            curr_row = self.head  # start at the beginning of the row
            while curr_row.down and curr_row.down.cell.row < cell.row:  # while row nodes are less than max row number, current pointer will keep going down list
                curr_row = curr_row.down  # until it finds the last node

            # If the row doesn't exist, create it
            if curr_row.down is None or curr_row.down.cell.row > cell.row:  # while row nodes are none or less than max row number
                new_row = Node(Cell(cell.row, -1, None))
                curr_row.down = new_row  # current node points down to the new row node in the same row
                new_row.up = curr_row  # new row node's previous pointer points back up to reference previous node
                curr_row = new_row
                # Create new nodes for this row in the first column
                for i in range(self.num_cols):
                    new_node = Node(Cell(cell.row, i, None))
                    curr_row.next = new_node
                    new_node.prev = curr_row
                    curr_row = new_node
            else:
                curr_row = curr_row.down

            # Traverse to the correct column
            while curr_row.next and curr_row.next.cell.col < cell.col:
                curr_row = curr_row.next

            # If a node already exists in this column, update its value
            if curr_row.next and curr_row.next.cell.col == cell.col:
                curr_row.next.cell.val = cell.val

            # Otherwise, create a new node
            else:
                new_node = Node(cell)
                new_node.prev = curr_row
                new_node.next = curr_row.next
                curr_row.next = new_node

        return True

    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """
        if self.num_cols == 0:
            return False

        curr_row = self.head

        # Traverse to the last row
        while curr_row.down:
            curr_row = curr_row.down

        # Append new row
        new_row = Node(Cell(curr_row.cell.row + 1, -1, None))
        curr_row.down = new_row
        new_row.up = curr_row
        self.num_rows += 1

        # Add empty cells to the new row
        curr_col = new_row
        for i in range(self.num_cols):
            new_cell = Cell(curr_row.cell.row + 1, i + 1, None)
            new_node = Node(new_cell)

            curr_col.next = new_node
            new_node.prev = curr_col
            curr_col = curr_col.next

        return True

    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        if not self.head.down:
            # Spreadsheet is empty
            return False

        curr = self.head.down
        while curr:
            # Traverse to the last node in the row
            while curr.next:
                curr = curr.next

            # Create new node at end of row
            new_node = Node(Cell(curr.cell.row, curr.cell.col + 1, None))
            curr.next = new_node
            new_node.prev = curr

            curr = curr.down

        self.num_cols += 1

        return True

    def insertRow(self, rowIndex: int) -> bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        if rowIndex < 0 or rowIndex > self.num_rows:
            return False

        curr_row = self.head
        # Traverse to the correct row
        while curr_row.down and curr_row.down.cell.row < rowIndex + 1:
            curr_row = curr_row.down

        # If the row doesn't exist, create it
        if curr_row.down is None or curr_row.down.cell.row > rowIndex + 1:
            new_row = Node(Cell(rowIndex + 1, -1, None))
            curr_row.down = new_row
            new_row.up = curr_row
            curr_row = new_row
            # Create new nodes for this row in the first column
            for i in range(self.num_cols):
                new_node = Node(Cell(rowIndex + 1, i, None))
                curr_row.next = new_node
                new_node.prev = curr_row
                curr_row = new_node
        else:
            curr_row = curr_row.down

        # Shift the row index of all the affected cells down by 1
        curr_row = curr_row.down
        while curr_row:
            curr_row.cell.row += 1
            curr_node = curr_row
            while curr_node:
                curr_node.cell.row += 1
                curr_node = curr_node.next
            curr_row = curr_row.down

        self.num_rows += 1
        return True

    def insertCol(self, colIndex: int) -> bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """
        # Check if colIndex is valid
        if colIndex < 0 or colIndex > self.colNum():
            return False

        curr_col = self.head

        # Traverse to the column to the left of the insert position
        while curr_col.next and curr_col.next.cell.col < colIndex:
            curr_col = curr_col.next

        # Create a new column node
        new_col = Node(Cell(-1, colIndex, None))

        # Insert new column node after curr_col
        new_col.next = curr_col.next
        curr_col.next = new_col

        # Update links between rows and columns
        curr_row = self.head
        while curr_row:
            if curr_row.next and curr_row.next.cell.col == colIndex:
                # Insert new node in this row to the right of the existing node
                new_node = Node(Cell(curr_row.cell.row, colIndex, None))
                new_node.next = curr_row.next
                curr_row.next.prev = new_node
                curr_row.next = new_node
                new_node.prev = curr_row
                new_node.up = new_col
                new_col.down = new_node
                new_col = new_col.down
            curr_row = curr_row.down

        # Update self.num_cols
        self.num_cols += 1
        return True

    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """
        curr_row = self.head.down
        while curr_row and curr_row.cell.row < rowIndex:
            curr_row = curr_row.down

        if not curr_row or curr_row.cell.row != rowIndex:
            return False

        curr_col = curr_row.next
        while curr_col and curr_col.cell.col < colIndex:
            curr_col = curr_col.next

        if not curr_col or curr_col.cell.col != colIndex:
            return False

        curr_col.cell.val = value
        return True

    def rowNum(self) -> int:
        """
        @return Number of rows the spreadsheet has.
        """
        return self.num_rows

    def colNum(self) -> int:
        """
        @return Number of column the spreadsheet has.
        """
        return self.num_cols

    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """
        result = []
        for cell in self.entries():
            if cell.val == value:
                result.append((cell.row, cell.col))
        return result

    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """
        cell_list = []
        curr_row = self.head.down
        while curr_row:
            curr_col = curr_row.next
            while curr_col:
                if curr_col.cell.val is not None:
                    cell_list.append(curr_col.cell)
                curr_col = curr_col.next
            curr_row = curr_row.down
        return cell_list

    def findNode(self, row: int, col: int) -> [Node]:
        """
        Helper function that returns the Node at the specified (row, col) position.
        Returns None if the Node is not found.
        """
        curr = self.head

        while curr is not None:
            if curr.cell.row == row and curr.cell.col == col:
                return curr
            elif curr.cell.row > row:
                return None
            elif curr.next is None:
                return None
            else:
                curr = curr.next
        return None
