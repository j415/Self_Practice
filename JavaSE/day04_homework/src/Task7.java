public class Task7 {
    public static void main(String[] args) {
        /*函数重载
            个数不一样 数据类型不一样  顺序不同
         */
        double sum1 = add(4.0, 6);
        System.out.println("sum1 = " + sum1);
        double sum2 = add(3.2, 2, 1);
        System.out.println("sum2 = " + sum2);
        double sum3 = add(4.7, 6.0);
        System.out.println("sum3 = " + sum3);
        double sum4 = add(4, 6.2);
        System.out.println("sum4 = " + sum4);

    }

    // 原型
    public static double add(double a, int b) {
        return a + b;
    }

    // 个数不一样
    public static double add(double a, int b, int c) {
        return a + b + c;
    }

    // 数据类型不一样
    public static double add(double a, double b) {
        return a + b;
    }

    // 顺序不同
    public static double add(int a, double b) {
        return a + b;
    }

}
