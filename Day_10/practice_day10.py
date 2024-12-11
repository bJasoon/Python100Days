
#==========================================================
# Docstrings
def format_name(fname, lname):
    """Take a first and last name and format it to 
    return the title case of the version of the name"""
    return f"{fname.title()} {lname.title()}"

print(format_name("JASON", "bAlETe"))

