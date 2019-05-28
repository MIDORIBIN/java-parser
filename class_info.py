import json
import re

from method_info import MethodInfo
from variableinfo import VariableInfo
from parse_regex import CLASS_NAME_LINE, ACCESS_MODIFIER_LINE


class ClassInfo:
    def __init__(self, code: str):
        self.class_name = ClassInfo.extra_class_name(code)
        self.class_type = ClassInfo.extra_class_type(code)
        self.variable_info_list = VariableInfo.code_to_list(code)
        self.method_info_list = MethodInfo.code_to_list(code)

    @staticmethod
    def is_access_modifier_line(line: str) -> bool:
        return True if re.match(ACCESS_MODIFIER_LINE, line) else False

    @staticmethod
    def filter_access_modifier(code) -> []:
        code_list = code.split('\n')
        return list(filter(ClassInfo.is_access_modifier_line, code_list))

    @staticmethod
    def extra_class_name(code: str) -> str:
        code_list = code.split('\n')
        pattern = re.compile(CLASS_NAME_LINE)
        class_name_line = list(filter(pattern.match, code_list))[0]
        return pattern.match(class_name_line).group(2)

    @staticmethod
    def extra_class_type(code: str) -> str:
        code_list = code.split('\n')
        pattern = re.compile(CLASS_NAME_LINE)
        class_name_line = list(filter(pattern.match, code_list))[0]
        return pattern.match(class_name_line).group(1)


def main():
    interface_sample = '''
public interface SampleInterface {
    public String normal();
    public void arg(String name);
    public void args(String name, int age);
}
    '''
    class_sample = """
public class TestClass {
    private String name;
    private String id = "idid";
    public static int age;

    public TestClass(String name) {
        this.name = name;
    }
    public String normalMethod(){
        return "Engineer";
    }
    public static MyClass classMethod(MyClass myClass) {
        return myClass;
    }
    private void multiArgMethod(String id, String age) {
    }
}"""

    print(json.dumps(ClassInfo(interface_sample), default=(lambda o: o.__dict__), indent=4))
    print('==========================================================================================')
    print(json.dumps(ClassInfo(class_sample), default=(lambda o: o.__dict__), indent=4))


if __name__ == '__main__':
    main()
