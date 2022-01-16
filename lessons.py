def is_cat_here(*args):
    if "cat" in args:
        return True
    return False

def is_item_here(item,*args):
    if item in args:
        return True
    return False

