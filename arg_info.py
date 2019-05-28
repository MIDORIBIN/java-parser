import re


class ArgInfo:
    def __init__(self, type_name: str, name: str):
        self.type_name = type_name
        self.name = name

    @staticmethod
    def _str_to_this(ele: str):
        return ArgInfo(*ele.split(' '))

    @staticmethod
    def multi_str_to_list(line: str):
        # 引数なしの場合
        if not line:
            return []
        str_arg_list = re.split(r', *', line)
        return list(map(ArgInfo._str_to_this, str_arg_list))
