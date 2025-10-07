def flatten_menu(node):
    """
    Return a flat list of item names from a nested menu.
    Node has "type": "category" or "item".
    """
    if not isinstance(node, dict):
        return []

    node_type = node.get("type")
    
    # Base case: it's an item with a name
    if node_type == "item":
        name = node.get("name")
        return [name] if isinstance(name, str) else []

    # Recursive case: it's a category
    elif node_type == "category":
        children = node.get("children", [])
        result = []
        for child in children:
            result.extend(flatten_menu(child))
        return result

    # Ignore unknown types
    return []
