class Solution {
    public int getSum(int a, int b) {

        int res = 0;
        int c = 0;
        for(int i = 0; i < 32; i++){
            int[] calList = myCal(c, (a & 1), (b & 1));
            c = calList[0];
            int s = calList[1];
            calList = null;
            res = res | (s << i);
            a = a >> 1;
            b = b >> 1;
        }
        return res;

    }

    int[] myCal(int c, int x, int y){
        int s = c ^ (x ^ y);
        c = (x & y) | (c & (x ^ y));
        // int s = c ^ (x ^ y) ORDER MATTRES
        int[] res = {c, s};
        return res;
    }

}
