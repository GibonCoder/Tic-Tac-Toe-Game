def transform_column(column: str) -> int:
    """Transforms the column letter to a number.
       Args:
           column (str): The column letter to transform.
       Returns:
           int: Column number."""
    match column.upper():
        case 'A':
            return 0
        case 'B':
            return 1
        case 'C':
            return 2
        case _:
            raise ValueError('Invalid column')
