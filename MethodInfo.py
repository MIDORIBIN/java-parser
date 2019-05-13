import re

from ArgInfo import ArgInfo


class MethodInfo:
    # (public|private|protected)( +static)?(?: +(.*))? +(\w+) *\((.*)\)
    _ACCESS = r' *(public|private|protected)'
    _STATIC = r'( +static)?'
    _NAME = r' +(\w+) *'
    _ARG = r'\((.*)\)'
    _OTHER = r'(?: +(.*))?'
    _RE_PATTERN = re.compile(_ACCESS + _STATIC + _OTHER + _NAME + _ARG)

    def __init__(self, name: str, return_type: str, access_modifier: str, is_class_method: bool, arg_list: []):
        self.name = name
        self.return_type = return_type
        self.access_modifier = access_modifier
        self.is_class_method = is_class_method
        self.arg_list = arg_list

    @staticmethod
    def _str_to_this(line: str):
        match = MethodInfo._RE_PATTERN.match(line)

        name = match.group(4)
        return_type = match.group(3)
        access_modifier = match.group(1)
        is_static = True if match.group(2) else False
        arg_list = ArgInfo.multi_str_to_list(match.group(5))

        return MethodInfo(name, return_type, access_modifier, is_static, arg_list)

    @staticmethod
    def code_to_list(code: str):
        method_line_list = MethodInfo._code_extra_method_line(code)
        return list(map(MethodInfo._str_to_this, method_line_list))

    @staticmethod
    def _code_extra_method_line(code: str) -> []:
        code_list = code.split('\n')
        return list(filter(MethodInfo._RE_PATTERN.match, code_list))