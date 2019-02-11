public class UnionFind {

    int[] p;
    int[] rank;
    public UnionFind(int n){
        rank = new int[n];
        p = new int[n];
        for (int i = 0; i < n; i++){
            p[i] = i;
        }
    }

    int findSet(int i){
        return (p[i] == i) ? i : (p[i] = findSet(p[i]));
    }

    boolean isSameSet(int i, int j){
        return findSet(i) == findSet(j);
    }

    void unionSet(int i, int j) {
        if (!isSameSet(i, j)) { // if from different set
            int x = findSet(i), y = findSet(j);
            if (rank[x] > rank[y]){
                p[y] = x; // rank keeps the tree short
            }
            else{
                p[x] = y;
                if (rank[x] == rank[y]) rank[y]++;
            }
        }
    }

    //Main is only for solving unionfind kattis problem
    //Keep commented out if using class for other problems
    public static void main(String[] args){
        Kattio io = new Kattio(System.in, System.out);
        int n = io.getInt();
        int q = io.getInt();
        UnionFind uf = new UnionFind(n);
        for(int i = 0; i < q; i++){
            char comm = io.getWord().charAt(0);
            int v1 = io.getInt();
            int v2 = io.getInt();
            if(comm == '?'){
                io.println(uf.isSameSet(v1,v2) ? "yes" : "no");
            }
            else{
                uf.unionSet(v1,v2);
            }
        }
        io.close();
    }
}
