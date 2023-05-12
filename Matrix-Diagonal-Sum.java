class Solution {
    int final_num = 0;
    int middle_num;
    //middle cant be counted so check if its middle and dont count it by saving the middle var
    public int diagonalSum(int[][] mat) {
        int where_middle_num =(mat.length-(mat.length/2))-1;
        for (int i=0; i<= mat.length-1; i++){

                final_num = final_num + mat[i][i];
        }

        for (int j=0; j< mat.length; j++){
            if (j != where_middle_num & mat.length%2!=0){
                final_num = final_num + mat[j][mat.length-j-1];
            }
            else if(mat.length%2==0){
                final_num = final_num + mat[j][mat.length-j-1];
            }
        }
        return final_num;
    }
}
