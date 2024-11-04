import java.util.Scanner;
public class Donation{
    public static void main(String args[]){
        Scanner sc= new Scanner(System.in);
        int x,y;
        x=sc.nextInt();
        y=sc.nextInt();
        if(y>x){
            System.out.println(y-x);
        }
    }
}