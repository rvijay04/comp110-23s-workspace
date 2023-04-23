from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read csv file and return as a list of dicts wit header keys."""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close
    return result


def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header"""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str,str]]) -> dict[str,list[str]]:
    """Reformats data so that it's a dictionary with column headers."""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table
    first_row: dict[str,str] = table[0]
    for key in first_row:
        #for each key, make a dictionary entry eith all column values
        result[key] = column_values(table, key)
    return result


def head(top_few: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new column with only the first few rows of data for each column."""
    new_dict: dict[str, list[str]] = {}
    for column in top_few:
        new_dict[column] = []
        for i in range(N):
            if i < len(top_few[column]):
                new_dict[column].append(top_few[column][i])
    return new_dict


def select(a: dict[str, list[str]], b: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of original columns."""
    new_dict: dict[str, list[str]] = {}
    for elem in b:
        new_dict[elem] = a[elem]
    return new_dict


def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combining two column-based tables combined."""
    new_dict: dict[str, list[str]] = {}
    for elem in a:
        new_dict[elem] = a[elem]
    for key in b:
        if key in new_dict:
            new_dict[key] += b[key]
        else:
            new_dict[key] = b[key]
    return new_dict


def count(a: list[str]) -> dict[str, int]:
    """Count the number of times a value appearied in the input list."""
    new_dict: dict[str, int] = {}
    for elem in a:
        if elem in new_dict:
            new_dict[elem] += 1
        else:
            new_dict[elem] = 1
    return new_dict