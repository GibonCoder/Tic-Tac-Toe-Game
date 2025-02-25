from transform_column import transform_column as trans_col


def parse_input(input_string: str) -> list:
    """Parse input string into a list of integers.
       Args:
           input_string (str): The input to parse.
       Returns:
           list: The parsed input."""
    listed_input = list(input_string)
    try:
        float(listed_input[1])
    except ValueError:
        return [-1, -1]
    else:
        parsed_input = [int(trans_col(listed_input[0])), int(listed_input[1])-1]
        return parsed_input
