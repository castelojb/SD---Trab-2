import json

# version of program
version = '1.0'


def parse_json(json_: dict) -> dict:
    """
    function that, given a json, performs a parser and applies the function responsible for computing the calculation
    Args:
        json_: a json in the following format
                {
                'val1': number,
                'val2': number,
                'op': string like +,-,* and / operations
                }

    Returns:
        dict: a dictionary containing the response of the operations it follows in the following format
        {
        'version': program version,
        'response': number or "undefined" in case of errors
        }
    """

    # get first valor
    val1 = json_.get('val1')

    # get second valor
    val2 = json_.get('val2')

    # get operator
    op = json_.get('op')

    # making default response
    out = {
        'version': version,
        'response': 'undefined'
    }

    # check if the 3 valors are passed
    if val1 and val2 and op:

        # make computation
        try:
            response = make_operation(
                float(val1),
                float(val2),
                op
            )

            # add response
            out['response'] = response

        except Exception as e:
            out['error'] = e

    # add error
    else:
        out['error'] = 'missing parameter'

    return out


def make_operation(val1: float, val2: float, op: str) -> float:
    """
    given two values and an operator, this function computes the desired operation, if the operator is
    not valid, returns an error
    Args:
        val1: firts valor of expression
        val2: second valor of expression
        op: operator of expression

    Returns:
        float: result of operation "val1 op val2" like 10 + 11 expression
    """

    # make operation check
    if op == '+':
        out = val1 + val2
    elif op == '-':
        out = val1 - val2
    elif op == '*':
        out = val1 * val2
    elif op == '/':
        out = val1 / val2
    else:
        # raise if operator unrecognized
        raise Exception("Unrecognized operator")

    return out


def make_json(val1: float, val2: float, op: str) -> dict:
    """
    facilitate the construction of a json to send to the server
    Args:
        val1: firts valor of expression
        val2: second valor of expression
        op: operator of expression

    Returns:
        dict: json in the following format
        {
        'val1': val1,
        'val2': val2,
        'op': op
        }
    """

    return {
        'val1': val1,
        'val2': val2,
        'op': op
    }


def json_to_bytes(json_: dict) -> bytes:
    """
    perform the transformation of a json into bytes
    Args:
        json_: a json object

    Returns:
        bytes: bytes representing the json
    """

    return str.encode(json.dumps(json_))


def bytes_to_json(bytes_: bytes) -> dict:
    """
    performs the transformation from bytes to json
    Args:
        bytes_: bytes representing the json

    Returns:
        dict: json obtained from bytes

    """

    return json.loads(bytes_)
