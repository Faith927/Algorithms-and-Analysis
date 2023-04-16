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
        self.colA = []
        self.valA = []
        self.sumA = []
        self.cols = []
        self.row = []
        self.num = []
        self.rows = []

    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """

        # TO BE IMPLEMENTED
        rows = []
        cols = []
        value = []
        for item in lCells:
            rows.append(item.row)
            cols.append(item.col)
            value.append(item.val)
        # finding the number of columns in the spreadsheet
        columns = max(cols) + 1  # adding one for 0

        # finding number of rows
        columns_rows = len(rows)/columns
        # print(columns_rows)
        num_row = max(rows) + 1 # adding one for 0
        # ColA
        zipped_rc = zip(rows, cols)  # zipping the rows and cols lists together
        zipped = list(zipped_rc)
        res = sorted(zipped, key=lambda x: x[0])
        # printing result
        # print("final list - ", res)
        colA = []
        for element in res:
            colA.append(element[1])
        # print("length", len(colA))
        # print(colA)
        # colA = [x for _, x in sorted(zipped_rc)]  # sorting columns according to row placement
        # ValA
        zipped_rv = zip(rows, value)  # zipping rows and values together
        # Converting to list
        zipped = list(zipped_rv)
        res = sorted(zipped, key=lambda x: x[0])
        # printing result
        # print("final list - ", res)
        valA = []
        for element in res:
            valA.append(element[1])
        # print(valA)
        # for x in zipped_rv:
        #     print(x)
        # # valA = [x for _, x in sorted(zipped_rv)]  # sorting the values according to the row placement
        # print(valA)
        # SumA
        myList = []  # creating a list to store the tuples of row and values
        zipped_pairs = zip(rows, value)  # zipping rows and values together
        for num in sorted(zipped_pairs):  # appending the sorted tuples to myList
            myList.append(num)
        sum_dict = {}  # creating a dict to store the sum of each column by value
        [sum_dict.__setitem__(first, sum_dict.get(first, 0) + second) for first, second in myList]
        rv_list = list(sum_dict.items())  # creating a list from the dictionary
        m_list = [z[1] for z in rv_list]  # taking only the second values from the list
        sumVal = [sum(m_list[:i + 1]) for i in range(len(m_list))]  # finding the sum for each value
        sumVal.insert(0, 0)
        rows.sort()  # sorting rows
        rows.insert(0, 0)  # appending 0 to the start of the list
        diff = [rows[i + 1] - rows[i] for i in range(len(rows) - 1)]  # finding the difference of each value in list
        diff.insert(len(diff), 1)  # appending one for the last element in the list
        lst = []  # creating a list to store the zipped sumVal and diff
        zipped_c = zip(sumVal, diff)  # zipping the lists sumVal and diff
        for num in zipped_c:
            lst.append(num)  # appending the tuples to lst
        sumA = []  # list to find sumA
        for element in lst:
            if element[1] > 1:  # if difference between rows > 1 duplicate elements by the difference
                sumA.extend([element[0]] * element[1])
            else:
                sumA.append(element[0])  # else just append value
        sumA.insert(0,0)  # cumulative sum up to row 0
        self.colA = colA
        self.valA = valA
        self.sumA = sumA
        self.cols = columns
        # self.cols = cols
        self.num = int(columns_rows)
        self.rows = rows
        # print(self.valA)


    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        try:
            lastElement = self.sumA[-1]  # finding the last element in sumA list
            self.sumA.append(lastElement)  # duplicating the last element in the sumA list
            # self.row += 1
            return True
        except NameError:
            return False


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # TO BE IMPLEMENTED
        try:
            self.cols += 1 # adds one to track column numbers
            # n = max(self.cols)
            # self.cols.append(n)
            return True
        except NameError:
            return False


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        value = self.sumA[rowIndex]  # finding the value of row according to rowIndex
        if rowIndex > 0:  # if rowIndex greater than zero, insert value using the rowIndex
            self.sumA.insert(rowIndex, value)  # inserting value at rowIndex
            # self.row += 1
            return True
        elif rowIndex == 0:  # if rowIndex equals zero, insert value at the start of SumA list
            self.sumA.insert(0, 0)
            # self.row += 1
            return True
        elif rowIndex == -1:
            self.sumA.append(value)  # appending value at end of sumA list
            return True
        else:
            return False


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """

        if 0 < colIndex < self.cols:  # making sure colIndex is a positive integer and in column list
            for i in range(len(self.colA)):
                if self.colA[i] >= colIndex:   # finds if column number is larger than colIndex
                    self.colA[i] = self.colA[i] + 1  # if larger, adds one to the column number
            self.cols += 1
            # for i in range(len(self.cols)):
            #     if self.cols[i] >= colIndex:
            #         self.cols[i] = self.col[i] + 1
            # n = self.colA[colIndex]
            # n = max(self.cols)
            # self.cols.append(n)
            return True
        elif colIndex == 0:
            self.cols += 1  # add another column to self.cols
            return True
        elif colIndex == -1:
            self.cols += 1  # add another column to self.cols
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
        if colIndex >= self.cols or rowIndex > len(self.sumA) - 1:  # check if column and row index exist
            return False
        else:
            myList = []
            indices = []
            # print("indices before", self.sumA)
            # print("before", self.colA)

            for r_inx, row in enumerate(self.sumA):  # finding the row indexes and values for each row
                # print(r_inx, row)
                if row not in myList and row != 0:
                    # print("row", row)
                    myList.append(row)
                    if row in myList:
                        indices.append(r_inx - 1)

            # n = self.row
            # print(n)
            # new = [item -1 for item in indices for i in range(n)]

            # print(new)
            # zipped_pairs = zip(self.colA, new)
            zipped_pairs = zip(self.colA, indices)

            # print(len(new))

            # print("indices", indices)
            lst = []
            for element in zipped_pairs:
                lst.append(element)
            # print("lst", lst)
            # print(self.valA)

            # if updating existing cell update column

            new_tuple = (colIndex, rowIndex)

            if new_tuple not in lst:
                lst.append(new_tuple)
                # print("lst", lst)

            lst.sort(key=lambda x: x[1], reverse=False)
            # print("sorted", lst)

            new_colA = [z[0] for z in lst]

            self.colA = new_colA

            # print("after", self.colA)

            # finding valA indcies
            valA_indices = []
            # print("valA before", self.valA)

            for r_inx, row in enumerate(self.valA):  # finding the row indexes and values for each row
                valA_indices.append(r_inx)

            zipped_valA_indices = zip(valA_indices, indices)
            # zipped_valA_indices = zip(valA_indices, new)


            vala = []

            for element in zipped_valA_indices:
                vala.append(element)
            # print("indices", vala)

            # update value or inserting value in volA:

            zipped_rv = zip(self.valA, self.colA, indices)
            # zipped_rv = zip(self.valA, self.colA, new)


            values = []
            for element in zipped_rv:
                values.append(element)
            # print(values, "values")
            # print(len(values))

            # updates a cells value if the row and column index are found

            for index, elements in enumerate(values):
                #         print("elements", values[index][1])
                if values[index][1] == colIndex and values[index][2] == rowIndex:

                    for element in vala:
                        if element[1] == rowIndex:
                            self.valA[element[0]] = value

                else:
                    pass

            if len(self.colA) > len(self.valA):
                vala_tuple = (value, colIndex, rowIndex)

                if vala_tuple not in values:
                    values.append(vala_tuple)
                    #                 print("values", values)

                    values.sort(key=lambda x: x[2], reverse=False)
                    #                 print("sorted", values)
                    # print("values", values)
                    new_valA = [z[0] for z in values]
                    self.valA = new_valA
            else:
                pass

            #     new = zip(indices, csr[1])

            # print(indices)

            # #     for index, row in enumerate(csr[2]):
            # #         print(row)
            # print("valA after", self.valA)
            sumVal = [sum(self.valA[:i + 1]) for i in range(len(self.valA))]  # finding the sum for each value
            # print("sumA before", self.sumA)

            sumVal.insert(0, 0)
            # print("sumVal", sumVal)
            #     sumVal.insert(0, 0)
            inx = [x[2] for x in values]
            inx.insert(0, 0)  # appending 0 to the start of the list
            # print("indices", indices)
            diff = [inx[i + 1] - inx[i] for i in range(len(inx) - 1)]  # finding the difference between each value in the list
            diff.insert(len(diff), 1)  # appending one for the last element in the
            # print("diff", diff)
            lst = []  # creating a list to store the zipped sumVal and diff
            if len(sumVal) > len(diff):
                # print(True)
                difference = len(inx) - len(diff)
                # print(difference)
                diff.append(difference + 1)
            zipped_c = zip(sumVal, diff)  # zipping the lists sumVal and diff
            for num in zipped_c:
                lst.append(num)  # appending the tupes to lst
            # print("lst", lst)
            # print("diff", diff)
            sumA = []  # list to find sumA
            for element in lst:
                if element[1] > 1:  # if difference between rows > 1 duplicate elements by the difference
                    sumA.extend([element[0]] * element[1])
                else:
                    sumA.append(element[0])  # else just append value
            #     sumA.insert(0,0)  # cumulative sum up to row 0
            self.sumA = sumA
            # self.sumA.insert(0,0)
            self.sumA.insert(0, 0)
            # print("sumA after", self.sumA)
            return True

    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        length = len(self.sumA)  # finding the length of sumA
        return length - 1  # minus one for the zero
        # return self.row

    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        return self.cols

    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        indices = []
        row_value = []
        index_list = []
        # print("value", row_value)
        for r_inx, row in enumerate(self.sumA):  # finding the row indexes and values for each row
            if row not in row_value and row != 0:
                # print(True)
                row_value.append(row)
                if row in row_value:
                    # print(r_inx)
                    indices.append(r_inx -1)  # minus one for 0
        # for r_inx, row in enumerate (self.valA):
        # print(len(indices))
        n = self.num
        # print(n)
        new = [item - 1 for item in indices for i in range(n)]

        # print(len(self.colA))
        print(len(self.colA), len(self.valA), len(new))
        zipped_pairs = zip(self.rows, self.colA, self.valA)  # zipping rows, columns, and values together
        for elements in zipped_pairs:
            # print(elements)
            if elements[2] == value:  # if row value equals value append row and column indexes to list
                # print(elements)
                index_list.append(elements[:2])
        return index_list



    def entries(self) -> [Cell]:
        """
        return a list of cells that have values (i.e., all non None cells).
        """
        indexes = []
        row_values = []
        final_list = []

        for r_inx, row in enumerate(self.sumA):
            if row not in row_values and row != 0:
                row_values.append(row)
                if row in row_values:
                    indexes.append(r_inx - 1)
        n = self.num
        # print(n)
        new = [item - 1 for item in indexes for i in range(n)]

        # zipped_pairs = zip(new, self.colA, self.valA)
        zipped_pairs = zip(self.rows, self.colA, self.valA)

        for elements in zipped_pairs:
            final_list.append(elements)
        # print(self.valA)
        return final_list
