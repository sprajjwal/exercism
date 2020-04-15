def two_fer(name = None):
    if type(name) != str and name != None:
        return None
    return f"One for {name}, one for me." if name else "One for you, one for me."
