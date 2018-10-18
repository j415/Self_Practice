public class Task6 {
    public static void main(String[] args) {
        /* 函数的练习：
                A:求两个数据之和
                B:判断两个数据是否相等
                C:获取两个数中较大的值
                D:打印m行n列的星形矩形
                E:打印nn乘法表
         */
        double sum1 = add(3.5,6.3);
        System.out.println("两个数据之和为="+sum1);
        boolean boo = isEquals(3.5,5);
        System.out.println("两个数据是否相等:"+boo);
        double sum2 = getMax(5,9.9);
        System.out.println("两个数中较大的为:"+sum2);
        star(6,8);
        Mul_table(6);

    }

    // A:求两个数据之和
    public static double add(double a, double b) {
        return a + b;
    }

    // B:判断两个数据是否相等
    public static boolean isEquals(double a, double b) {
        return a == b;
    }

    // C:获取两个数中较大的值
    public static double getMax(double a, double b) {
        return a > b ? a : b;
    }

    // D:打印m行n列的星形矩形
    public static void star(int a, int b) {
        for (int i = 1; i <= a; i++) {
            for (int j = 1; j <= b; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
    // E:打印nn乘法表
    public static void Mul_table(int a) {
        for (int i = 1; i <= a; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(j +"*"+i+"="+(i*j)+"\t");
            }
            System.out.println();
        }
    }
}
