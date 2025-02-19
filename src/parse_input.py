from transform_column import transform_column as trans_col


def parse_input(input_string: str) -> list:
    """Parse input string into a list of integers.
       Args:
           input_string (str): The input to parse.
       Returns:
           list: The parsed input."""
    sliced_input = input_string.split()
    parsed_input = []
    parsed_input[0] = trans_col(sliced_input[0])
    parsed_input[1] = int(sliced_input[1])

    return parsed_input
