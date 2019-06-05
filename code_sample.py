class_sample = '''
public class TestClass {
    private String name;
    private String id = "idid";
    private List<String> list = new ArrayList<>();
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
    private List<String> returnList(String id, String age) {
    }
}
'''

interface_sample = '''
public interface SampleInterface {
    public String normal();
    public void arg(String name);
    public void args(String name, int age);
    public List<String> returnList();
}
'''