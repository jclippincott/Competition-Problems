

class fenwick {

    public static void main (String[] args){
//        int[] f = {2,4,5,5,6,6,6,7,7,8,9};
//        fenwick ft = new fenwick(10);
//
//        for(int i = 0; i < 11; i++){
//            ft.add(f[i],1);
//        }

        Kattio io = new Kattio(System.in, System.out);
        int n = io.getInt();
        FenwickTree ft = new FenwickTree(n);
        int q = io.getInt();
        for (int i = 0; i < q; i++){
            char comm = io.getWord().charAt(0);
            int v1 = io.getInt();
            if(comm == '+'){
                int v2 = io.getInt();
                ft.adjust(v1+1,v2);
            }
            else{
                if(v1 == 0){
                    io.println("0");
                }
                else{
                    io.println(ft.rsq(v1));
                }
            }
        }
        io.close();
    }
}