from pymarkdownlint.options import IntOption


class Rule(object):
    options_spec = []
    id = []
    name = []

    def __init__(self, opts={}):
        self.options = {}
        for op_spec in self.options_spec:
            self.options[op_spec.name] = op_spec
            actual_option = opts.get(op_spec.name)
            if actual_option:
                self.options[op_spec.name].set(actual_option)

    def validate(self, markdown):
        lines = markdown.split("\n")
        i = 1
        for line in lines:
            self.validate_line(line, i)
            i += 1

    def validate_line(self, line):
        pass


class RuleError(BaseException):
    pass


class MaxLineLengthRule(Rule):
    name = "Max line length"
    id = "R1"
    options_spec = [IntOption('line-length', 80, "Max line length")]

    def validate_line(self, line, index):
        max_length = self.options['line-length'].value
        if len(line) > max_length:
            raise RuleError("Line {0} exceeds max length ({1}>{2})".format(index, len(line), max_length))
