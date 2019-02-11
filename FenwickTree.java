public class FenwickTree {

    private int size;
    public int[] vals;

    public FenwickTree(int initsize) {
        this.size = initsize + 1;
        this.vals = new int[initsize + 1];
    }

    private int LSB(int a) {
        return (a & -a);
    }

    public int rsq(int a) {
        int sum = 0;
        for (; a != 0; a -= LSB(a)) {
            sum += vals[a];
        }
        return sum;
    }

    public int rsq(int a, int b) {
        int sum1 = (a == 1) ? 0 : rsq(a - 1);
        return rsq(b) - sum1;
    }

    public void adjust(int k, int v) {
        for (; k < size; k += LSB(k)) {
            vals[k] += v;
        }
    }
}
