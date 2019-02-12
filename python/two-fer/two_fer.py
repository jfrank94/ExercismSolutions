def two_fer(name=None):
    return "One for you, one for me." if name is None else "One for {}, one for me.".format(name)
