import java.util.Scanner;
public class Area{
    public static void main(String args[]){
        double r;
        Scanner sc= new Scanner(System.in);
        r=sc.nextDouble();
        double res = 3.14*r*r;
        System.out.printf("%.2f",res);
    }
}