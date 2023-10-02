class Solution {
    public int lengthOfLastWord(String s) {
        String newS=s.trim();
        int j=newS.lastIndexOf(" ");
        int l=newS.length();
        int result=l-j-1;
        return result;
    }
}