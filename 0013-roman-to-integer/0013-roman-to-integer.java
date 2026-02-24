import java.util.HashMap;

class Solution {
    public int romanToInt(String s) {
        int p1 = 0;
        int p2 = 1;
        int ans = 0;
        HashMap<Character,Integer> hashMap = new HashMap<>();
        hashMap.put('I',1); 
        hashMap.put('V',5); 
        hashMap.put('X',10); 
        hashMap.put('L',50); 
        hashMap.put('C',100); 
        hashMap.put('D',500); 
        hashMap.put('M',1000);
        while(p1 <= s.length() -2){
            if(s.charAt(p1) == 'I' && (s.charAt(p2) == 'V' || s.charAt(p2) == 'X')){
                if(s.charAt(p2) == 'V' ){
                    ans += 4;
                    p1 = p2 + 1;
                    p2 += 2;
                }else{
                    ans += 9;
                    p1 = p2 + 1;
                    p2 += 2;
                }
            } else if(s.charAt(p1) == 'X' && (s.charAt(p2) == 'L' || s.charAt(p2) == 'C')){
                if(s.charAt(p2) == 'L' ){
                    ans += 40;
                    p1 = p2 + 1;
                    p2 += 2;
                }else{
                    ans += 90;
                    p1 = p2 +1 ;
                    p2 += 2;
                }
            } else if(s.charAt(p1) == 'C' && (s.charAt(p2) == 'D' || s.charAt(p2) == 'M')){
                if(s.charAt(p2) == 'D' ){
                    ans += 400;
                    p1 = p2 + 1;
                    p2 += 2;
                }else{
                    ans += 900;
                    p1 = p2 +1 ;
                    p2 += 2;
                }
            } else{
                ans += hashMap.get(s.charAt(p1));
                p1 = p2;
                p2 += 1;
            }
            
            
        } 
        if(p1 == s.length()-1){
            ans += hashMap.get(s.charAt(p1));
        }

        //ans += hashMap.get(s.charAt(p1));
        System.out.println(ans);
        return ans;
    }
}