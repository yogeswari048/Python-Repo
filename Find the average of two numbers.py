import java.util.Scanner;
public class Avg{
    public static void main(String args[]){
        double a,b;
        Scanner sc=new Scanner(System.in);
        a=sc.nextDouble();
        b=sc.nextDouble();
        double d = (a+b)/2;
        System.out.printf("%.4f",d);
    }
}