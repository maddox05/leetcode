class Solution {
    public int romanToInt(String s) {
        String[] romans = s.split("",0);
        int[] real_nums = new int[romans.length];
        for (int i = 0; i < romans.length; i++) {
            switch (romans[i]) {
                case "I" -> real_nums[i] = 1;
                case "V" -> real_nums[i] = 5;
                case "X" -> real_nums[i] = 10;
                case "L" -> real_nums[i] = 50;
                case "C" -> real_nums[i] = 100;
                case "D" -> real_nums[i] = 500;
                case "M" -> real_nums[i] = 1000;
                default -> System.out.println("err" + romans[i]);
            }

        }
        int final_number = 0;
        for (int j = 0; j < real_nums.length; j++) {
            if (j == real_nums.length-1){

                final_number = final_number + real_nums[j];

            }
            else if (real_nums[j] < real_nums[j+1]){
                final_number = final_number + (real_nums[j+1] - real_nums[j]);
                j=j+1;
            } else if(real_nums[j] > real_nums[j+1]){
                final_number = final_number + (real_nums[j]);
            }
            else if (real_nums[j] == (real_nums[j + 1])){
                final_number = final_number + (real_nums[j] + real_nums[j+1]);
                j=j+1;
            }



        }
        return final_number;
    }
}
