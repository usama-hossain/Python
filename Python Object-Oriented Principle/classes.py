

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


# If no optional formatter is supplied, a DefaultFormatter is created.
# DefaultFormatter is a local function class that is not accessible anywhere else.
def format_string(string, formatter=None):
    class DefaultFormatter:
        def format(self, string):
            return str(string).title()

    if not formatter:
        formatter = DefaultFormatter()

    return formatter.format(string)
