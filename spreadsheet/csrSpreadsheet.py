from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------


class CSRSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        # initializing class
        self.colA = []
        self.valA = []
        self.sumA = []
        self.cols = []

    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        # empty lists to store rows, columns, and values
        rows = []
        cols = []
        value = []
        # appending row, column, and values to their respective lists
        for item in lCells:
            rows.append(item.row)
            cols.append(item.col)
            value.append(item.val)
        # Finding number of columns:
        columns = max(cols)

        # sorting columns according to row placement for ColA
        zipped_rc = zip(rows, cols)
        colA = [x for _, x in sorted(zipped_rc)]

        # sorting values according to row placement for ValA
        zipped_rv = zip(rows, value)
        valA = [x for _, x in sorted(zipped_rv)]

        # creating a list which stores sorted rows and values
        myList = []
        zipped_pairs = zip(rows, value)
        for num in sorted(zipped_pairs):
            myList.append(num)

        # creating a dict to store the sum of each column by value
        sum_dict = {}
        [sum_dict.__setitem__(first, sum_dict.get(first, 0) + second) for first, second in myList]

        # creating a list from the dictionary and storing the second value in the list
        rv_list = list(sum_dict.items())
        m_list = [z[1] for z in rv_list]

        # finding the sum for each consecutive value
        sumVal = [sum(m_list[:i + 1]) for i in range(len(m_list))]
        if 0 not in rows:
            sumVal.insert(0, 0)
        rows.sort()
        rows.insert(0, 0)

        # finding the difference of each value in list
        diff = [rows[i + 1] - rows[i] for i in range(len(rows) - 1)]
        diff.insert(len(diff), 1)
        # creating a list to store the zipped sumVal and diff
        lst = []
        zipped_c = zip(sumVal, diff)
        for num in zipped_c:
            lst.append(num)

            # duplicated sumVal by the number of empty rows to find sumA
        sumA = []
        for element in lst:
            if element[1] > 1:
                sumA.extend([element[0]] * element[1])
            else:
                sumA.append(element[0])
        sumA.insert(0, 0)

        # modifying the empty lists
        self.colA = colA
        self.valA = valA
        self.sumA = sumA
        self.cols = columns

    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # appending row
        try:
            # finding the last element in sumA list and duplicates it, else returns false
            lastElement = self.sumA[-1]
            self.sumA.append(lastElement)
            return True
        except NameError:
            return False

    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        try:
            # tracks the column numbers and adds two, one for 0, and one for extra column
            self.cols = self.cols + 2
            return True
        except NameError:
            return False

    def insertRow(self, rowIndex: int) -> bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        # if rowIndex greater than zero, insert value using the rowIndex
        if rowIndex > 0:
            value = self.sumA[rowIndex]
            self.sumA.insert(rowIndex, value)
            return True
        # if rowIndex equals zero, insert value at the start of SumA list
        elif rowIndex == 0:
            self.sumA.insert(rowIndex, 0)
            return True
        # if rowIndex equals zero, insert value at the start of SumA list
        elif rowIndex == -1:
            last_element = self.sumA[-1]
            self.sumA.append(last_element)
            return True
        else:
            return False

    def insertCol(self, colIndex: int) -> bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """
        for i in range(self.cols):  # making sure that the colIndex is in the spreadsheet
            if i == colIndex:
                continue
        # adds one to the column numbers if column numbers after inserted column
        if colIndex >= 0:
            for i in range(len(self.colA)):
                if self.colA[i] >= colIndex:
                    self.colA[i] = self.colA[i] + 1
            self.cols = self.cols + 1
            return True
        elif colIndex == -1:
            self.cols = self.cols + 1  # tracking col numbers
            return True
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
        column_length = self.cols - 1  # minus one for zero

        row_length = len(self.sumA)

        if colIndex > column_length or rowIndex > row_length - 1:
            return False
        else:
            myList = []
            indices = []
            result = []

            # finds and appends row indexes which are have values
            for r_inx, row in enumerate(self.sumA):
                if row not in myList and row != 0:
                    myList.append(row)
                    if row in myList:
                        indices.append(r_inx - 1)

            # if indexes are not equal the index must be duplicated by row
            if len(indices) < len(self.valA):
                result = []
                start = 0
                for i in indices:
                    target = myList[i]  # find the target value
                    count = 0  # initializing a counter for num of elements

                    # # check if current element in valA is <= to target value and if so, subtracts element from target
                    for j in range(start, len(self.valA)):
                        if self.valA[j] <= target:
                            target -= self.valA[j]
                            count += 1
                            if target == 0:
                                start = j + 1
                                break
                    if target == 0 and count > 0:  # final check to ensure target has been met by elements
                        result.extend([i] * count)
                    else:  # append current index to the result list
                        for k in range(count):  # appending index
                            result.append(i)

                zipped_pairs = zip(indices, self.colA, self.valA)
                for elements in zipped_pairs:
                    # if element equals value append indices to list
                    if elements[2] == value:
                        result.append(elements[:2])

                # changing the indice values to the result values
                indices = result

                zipped_pairs = zip(self.colA, indices)
            else:
                zipped_pairs = zip(self.colA, indices)

            lst = []
            for element in zipped_pairs:  # appending the column and row values to lst
                lst.append(element)

            new_tuple = (colIndex, rowIndex)

            # if column and row index not in lst append it
            if new_tuple not in lst:
                lst.append(new_tuple)
            lst.sort(key=lambda x: x[1], reverse=False)  # sort list according to row index

            # taking just the first value (column index) to create colA, then replaces self.colA
            new_colA = [z[0] for z in lst]
            self.colA = new_colA

            # finding valA indices
            valA_indices = []
            for r_inx, row in enumerate(self.valA):
                valA_indices.append(r_inx)
            zipped_valA_indices = zip(valA_indices, indices)

            # appending row and value indexes together
            vala = []
            for element in zipped_valA_indices:
                vala.append(element)
            zipped_rv = zip(self.valA, self.colA, indices)

            # appending values columns and rows to values list
            values = []
            for element in zipped_rv:
                values.append(element)
            # modifying existing value to new value
            for index, elements in enumerate(values):
                if values[index][1] == colIndex and values[index][2] == rowIndex:
                    for element in vala:
                        if element[1] == rowIndex and element[0] == colIndex:
                            self.valA[element[0]] = value  # replacing existing value with new value
                else:
                    pass

            # checking if length of colA and valA are the same
            if len(self.colA) > len(self.valA):
                vala_tuple = (value, colIndex, rowIndex)

                # if new tuple is not in values, append it
                if vala_tuple not in values:
                    values.append(vala_tuple)
                    values.sort(key=lambda x: x[2], reverse=False)

                    # creating the new_valA list with first element in values
                    new_valA = [z[0] for z in values]
                    self.valA = new_valA
            else:
                pass

            # finding if there are duplicate rows
            if len(indices) != len(set(indices)):
                num_rows = len(set(result))

                # Initialize a list to store the sums for each row
                sumVal = [0] * num_rows

                # Loop over the result list and add up the values in valA
                cumulative_sum = 0
                for i, r in enumerate(result):
                    sumVal[r] += self.valA[i] + cumulative_sum
                    if i < len(result) - 1 and result[i] != result[i + 1]:
                        cumulative_sum = sumVal[r]
                    else:
                        cumulative_sum = 0
            else:
                sumVal = [sum(self.valA[:i + 1]) for i in range(len(self.valA))]  # finding the sum for each value
                sumVal.insert(0, 0)

            # creating index list
            inx = [x[2] for x in values]
            inx.insert(0, 0)

            # finding the difference between each value in the list
            diff = [inx[i + 1] - inx[i] for i in range(len(inx) - 1)]
            diff.insert(len(diff), 1)

            # creating a list to store the zipped sumVal and diff
            lst = []
            if len(sumVal) > len(diff):
                difference = len(inx) - len(diff)
                diff.append(difference + 1)
            zipped_c = zip(sumVal, diff)
            for num in zipped_c:
                lst.append(num)

            # list to find sumA
            sumA = []
            for element in lst:
                if element[1] > 1:  # if difference between rows > 1 duplicate elements by the difference
                    sumA.extend([element[0]] * element[1])
                else:
                    sumA.append(element[0])
            self.sumA = sumA  # changing the elements in sumA to the new values
            self.sumA.insert(0, 0)
            return True

    def rowNum(self) -> int:
        """
        @return Number of rows the spreadsheet has.
        """
        length = len(self.sumA)  # finding the length of sumA
        return length - 1  # minus one for the zero

    def colNum(self) -> int:
        """
        @return Number of column the spreadsheet has.
        """
        return self.cols  # returning number of columns

    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """
        # empty lists to store row indexes, row values, and final index list
        indices = []
        myList = []
        index_list = []

        # finds index for rows which have values
        for r_inx, row in enumerate(self.sumA):
            if row not in myList and row != 0:
                myList.append(row)
                if row in myList:
                    indices.append(r_inx - 1)  # minus one for the zero

        # if indexes are not equal the index must be duplicated by row
        if len(indices) < len(self.valA):
            result = []
            start = 0  # starting index
            for i in indices:
                target = myList[i]  # find the target value
                count = 0  # initializing a counter for num of elements
                for j in range(start,
                               len(self.valA)):  # iterate through element in valA starting from current start index
                    if self.valA[j] <= target:  # check if current element in valA is <= to target value
                        target -= self.valA[j]  # if so subtract current element from target
                        count += 1
                        if target == 0:  # if target is zero, update start index and exit the loop
                            start = j + 1
                            break
                if target == 0 and count > 0:  # final check to ensure target has been met by elements
                    result.extend([i] * count)
                else:
                    for k in range(count):
                        result.append(i)
            zipped_pairs = zip(indices, self.colA, self.valA)

            for elements in zipped_pairs:
                if elements[2] == value:  # if element equals value append indices to list
                    index_list.append(elements[:2])
            return index_list
        else:
            zipped_pairs = zip(indices, self.colA, self.valA)  # zipping rows, columns, and values together
            for elements in zipped_pairs:
                if elements[2] == value:  # if element equals value append indices to list
                    index_list.append(elements[:2])
            return index_list

    def entries(self) -> [Cell]:
        """
        return a list of cells that have values (i.e., all non None cells).
        """
        indexes = []
        lst = []
        final_list = []

        # finds index for rows which have values
        for r_inx, row in enumerate(self.sumA):
            if row not in lst and row != 0:
                lst.append(row)
                if row in lst:
                    indexes.append(r_inx - 1)

        # if indexes are not equal the index must be duplicated by row
        if len(indexes) < len(self.valA):
            result = []
            start = 0
            for i in indexes:
                target = lst[i]  # find the target value
                count = 0
                for j in range(start,
                               len(self.valA)):  # iterate through element in valA starting from current start index
                    if self.valA[j] <= target:  # check if current element in valA is <= to target value
                        target -= self.valA[j]  # if so subtract current element from target
                        count += 1
                        if target == 0:  # if target is zero, update start index and exit the loop
                            start = j + 1
                            break
                if target == 0 and count > 0:  # final check to ensure target has been met by elements
                    result.extend([i] * count)
                else:  # append current index to the result list
                    for k in range(count):
                        result.append(i)

            # zipping row index, column index, and value together and appending it to final list
            zipped_pairs = zip(result, self.colA, self.valA)
            for elements in zipped_pairs:
                final_list.append(elements)
        else:
            # zipping row index, column index, and value together and appending it to final list
            zipped_pairs = zip(indexes, self.colA, self.valA)
            for elements in zipped_pairs:
                final_list.append(elements)
        return final_list