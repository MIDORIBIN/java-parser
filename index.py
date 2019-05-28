import json
import base64

from class_info import ClassInfo
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
def catch_all(path):
    return "You visited the %s page" % (path)


@app.route('/sample')
def sample():
    class_sample = """public class TestClass {
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
    interface_sample = '''
        public interface SampleInterface {
            public String normal();
            public void arg(String name);
            public void args(String name, int age);
        }
    '''
    class_info_list = [ClassInfo(class_sample)]
    body_json = json.loads(json.dumps(class_info_list, default=(lambda o: o.__dict__)))

    return jsonify(body_json)


@app.route('/analyze', methods=["GET", "POST"])
def analyze():
    data = request.data.decode('utf-8')
    data = json.loads(data)

    class_info_list = list(map(base64_to_class_info, data['code_list']))
    body_json = json.loads(json.dumps(class_info_list, default=(lambda o: o.__dict__)))

    return jsonify(body_json)


def base64_to_code(base64_code: str) -> str:
    return base64.b64decode(base64_code).decode('utf-8')


def base64_to_class_info(base64_code: str) -> ClassInfo:
    code = base64_to_code(base64_code)
    return ClassInfo(code)


if __name__ == '__main__':
    app.run()
