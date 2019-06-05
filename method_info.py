import re

from arg_info import ArgInfo
from parse_regex import METHOD_LINE


class MethodInfo:
    _METHOD_LINE_PATTERN = re.compile(METHOD_LINE)

    def __init__(self, name: str, return_type: str, access_modifier: str, is_class_method: bool, arg_list: []):
        self.name = name
        self.return_type = return_type
        self.access_modifier = access_modifier
        self.is_class_method = is_class_method
        self.arg_list = arg_list

    @staticmethod
    def _str_to_this(line: str):
        match = MethodInfo._METHOD_LINE_PATTERN.match(line)

        name = match.group(5)
        return_type = match.group(4)
        access_modifier = match.group(1)
        is_static = True if match.group(2) else False
        arg_list = ArgInfo.multi_str_to_list(match.group(6))

        return MethodInfo(name, return_type, access_modifier, is_static, arg_list)

    @staticmethod
    def code_to_list(code: str):
        method_line_list = MethodInfo._code_extra_method_line(code)
        return list(map(MethodInfo._str_to_this, method_line_list))

    @staticmethod
    def _code_extra_method_line(code: str) -> []:
        code_list = code.split('\n')
        return list(filter(MethodInfo._METHOD_LINE_PATTERN.match, code_list))
