import re


class VariableInfo:
    _ACCESS = r' *(public|private|protected)'
    _STATIC = r'( +static)?'
    _WARD = r' +(\w+)'
    _RE_PATTERN = re.compile(_ACCESS + _STATIC + _WARD + _WARD + r'(.*);')

    def __init__(self, access_modifier: str, is_class_variable: bool, variable_type: str, name: str):
        self.access_modifier = access_modifier
        self.is_class_variable = is_class_variable
        self.variable_type = variable_type
        self.name = name

    @staticmethod
    def str_to_this(line: str):
        match = VariableInfo._RE_PATTERN.match(line)
        access_modifier = match.group(1)
        is_class = True if match.group(2) else False
        variable_type = match.group(3)
        name = match.group(4)

        return VariableInfo(access_modifier, is_class, variable_type, name)

    @staticmethod
    def code_to_list(code: str):
        method_line_list = VariableInfo.code_extra_variable_line(code)
        return list(map(VariableInfo.str_to_this, method_line_list))

    @staticmethod
    def code_extra_variable_line(code: str) -> []:
        code_list = code.split('\n')
        return list(filter(VariableInfo._RE_PATTERN.match, code_list))