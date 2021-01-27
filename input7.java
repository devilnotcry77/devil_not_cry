import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Введите число: ");
        int n = in.nextInt();
        int i, j;
        for (i=1; j<=n; j++)
        {
            for (j=1; j<=n; j++)
            {
                if (i==j)
                   System.out.print(i+"");
                else
                   System.out.print("0");
            }
            System.out.println("");
        }
    }
}