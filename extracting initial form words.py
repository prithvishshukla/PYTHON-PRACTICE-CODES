
def get_initials(full_name):
    names = full_name.split()
    initials = "".join([name[0].upper() for name in names])
    return initials

name = "John Doe"
print(get_initials(name))
