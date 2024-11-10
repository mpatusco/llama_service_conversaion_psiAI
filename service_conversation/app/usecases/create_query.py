from typing import List

def create_query(fields: List[str]) -> dict:
    """Generate a MongoDB query to fetch specific fields.

    Args:
        fields (List[str]): List of field names to include in the query.

    Returns:
        dict: MongoDB query for the specified fields.
    """
    return {"_id": field for field in fields}
