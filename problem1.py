# Implement a group_by_owners function that:
#
# ·   Accepts a dictionary containing the file owner name for each file name.
#
# ·   Returns a dictionary containing a list of file names for each owner name, in any order.
#
# For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
# the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

from collections import defaultdict


def group_by_owners(data):
    """
    :param data: input dictionary with file_name as key and owner_name as value
    :return: return dictionary containing a list of file names for each owner name, in any order.
    """
    owners_grp = defaultdict(list)
    for file, owner in data.items():
        owners_grp[owner].append(file)
    return dict(owners_grp)


# if __name__ == '__main__':
#     print(group_by_owners({'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}))
