def tagger(tag):
    def inner(s):
        return "<" + tag + ">" + s + "</" + tag + ">"
    return inner