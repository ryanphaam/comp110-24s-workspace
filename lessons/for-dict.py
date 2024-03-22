"""Practice with dictionaries and for loops."""

in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apples": True}

for key in in_stock:
    # key in "carrots" "beets" "apples"
    # in_stock[key] is values: True False True
    if in_stock[key]:  # in_stock[key] is True
        print(key)

