import json
import re

from MethodInfo import MethodInfo
from VariableInfo import VariableInfo


class ClassInfo:
    _RE_PATTERN = re.compile(r'public class (\w+)')

    def __init__(self, code: str):
        self.class_name = ClassInfo.extra_class_name(code)
        self.variable_info_list = VariableInfo.code_to_list(code)
        self.method_info_list = MethodInfo.code_to_list(code)

    @staticmethod
    def is_access_modifier_line(line: str) -> bool:
        pattern = '( *public.*)|( *private.*)|( *protected.*)'
        return True if re.match(pattern, line) else False

    @staticmethod
    def filter_access_modifier(code) -> []:
        code_list = code.split('\n')
        return list(filter(ClassInfo.is_access_modifier_line, code_list))

    @staticmethod
    def extra_class_name(code: str) -> str:
        code_list = code.split('\n')
        class_name_line = list(filter(ClassInfo._RE_PATTERN.match, code_list))[0]
        return ClassInfo._RE_PATTERN.match(class_name_line).group(1)


def main():
    code = """public class TestClass {
        // メンバ変数
        private String name;
        public static int age;

        // 引数ありのコンストラクタ
        public TestClass(String name) {
            this.name = name;
        }

        // メソッド
        public String TestMethod(){
            return "Engineer";
        }
    }"""
    # a = MethodInfo.str_to_this('        public TestClass(String name) {')
    # print(vars(a))
    a = ClassInfo(code)
    print(json.dumps(a, default=(lambda o: o.__dict__)))


if __name__ == '__main__':
    main()
