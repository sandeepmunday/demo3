def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)
print(add_tags('i', 'Sandeep'))
print(add_tags('b', 'Singh'))
