import java.util.Scanner;

public class supercomputer {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        FenwickTree ft = new FenwickTree(sc.nextInt());
        int n = sc.nextInt();
        sc.nextLine();
        for (int ii = 0; ii < n; ii++){
            String[] comm = sc.nextLine().split(" ");
            if(comm[0].equals("F")){
                int i = Integer.parseInt(comm[1]);
                if(ft.rsq(i,i) == 1){
                    ft.adjust(i,-1);
                }
                else{
                    ft.adjust(i,1);
                }
            }
            else{
                int l = Integer.parseInt(comm[1]);
                int r = Integer.parseInt(comm[2]);
                System.out.println(ft.rsq(l,r));
            }
        }
    }
}
