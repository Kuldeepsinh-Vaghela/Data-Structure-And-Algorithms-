class Solution {
    public int[] plusOne(int[] digits) {
        int p1 = digits.length -1;
        while(digits[p1] == 9){
            digits[p1] = 0;
            p1 -= 1;
            if(p1 == -1){
                break;
            }
        }
        if(p1 == -1){
                int[] newArr = new int[digits.length + 1];
                newArr[0] = 1;
                return newArr;
        }else{
            
            digits[p1] += 1;
                
                
            }
            
        
        //digits[p1] += 1;
        //System.out.println(digits);
        return digits;
        
    }
}

