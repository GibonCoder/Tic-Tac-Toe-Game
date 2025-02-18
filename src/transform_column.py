def transform_column(column):
    match column:
        case 'A':
            return 0
        case 'B':
            return 1
        case 'C':
            return 2
        case _:
            raise ValueError('Invalid column')
