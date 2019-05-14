import json

from ClassInfo import ClassInfo
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config.update({'DEBUG': True})


@app.route('/', defaults={'path': ''})
def catch_all(path):
    return "You visited the %s page" % (path)


@app.route('/sample')
def sample():
    code = """public class TestClass {
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
    class_info_list = [ClassInfo(code)]
    body_json = json.loads(json.dumps(class_info_list, default=(lambda o: o.__dict__)))

    return jsonify(body_json)


@app.route('/analyze', methods=["GET", "POST"])
def analyze():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    code = str(data['key'])

    class_info = ClassInfo(code)
    body_json = json.loads(json.dumps(class_info, default=(lambda o: o.__dict__)))

    return jsonify(body_json)


if __name__ == '__main__':
    app.run()
