
"""
Add your solution in here
"""
from typing import TypedDict


class Survey(TypedDict):
    """
    The structure of each survey
    a tx_id (unique identifier)
    a name: (also unique)
    """
    tx_id: int
    name: str


def find_fake_surveys(surveys: list[Survey]) -> list[tuple[int]]:
    """
    Given a list of surveys, return a list of tuples that correspond to the
    fake surveys
    """
    result = []
    list_of_values = [i['name'] for i in surveys]
    reversed_values = [i['name'][::-1] for i in surveys]

    for i, v in enumerate(list_of_values):
        if v in reversed_values:
            # Get the index of the value in the reversed list
            j = reversed_values.index(v)
            # Check if it's not matching with itself!
            if i != j:
                # append a tuple of the tx_id values at each index
                result.append((surveys[i]['tx_id'], surveys[j]['tx_id']))
    return result

    # out_list = []
    # for i in range(len(surveys)):
    #     for j in range(i + 1, len(surveys)):
    #         if surveys[i]['name'] == surveys[j]['name'][::-1]:
    #             out_list.append((surveys[i]['tx_id'], surveys[j]['tx_id']))
    # return out_list
