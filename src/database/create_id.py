import uuid


def create_id(prefix: str) -> str:
    """
    Create a unique ID for a database entry.

    :param prefix: Prefix of database entry.
    :return: Randomized ID.
    """
    return str(prefix + "_" + uuid.uuid4().__str__().strip("-").upper())
