public class Task2 {
    public static void main(String[] args) {
        /*  用while循环完成如下案例

          求和
          假设有一张足够大的纸，厚度为1毫米，珠穆朗玛峰高度为8848米，
          求纸张至少折叠几次可以超过珠穆朗玛峰的高度
         */
        int x = 1;
        int sum = 1;
        while (sum < 8848000) {
            sum = sum * 2;
            x++;
        }
        System.out.println("纸张至少折叠" + x + "次");
        System.out.println("折叠的纸张共" + sum + "层");


    }
}
