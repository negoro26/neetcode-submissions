class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> word1Counts = new HashMap<>();
        HashMap<Character, Integer> word2Counts = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            word1Counts.put(s.charAt(i), word1Counts.getOrDefault(s.charAt(i), 0) + 1);
            word2Counts.put(t.charAt(i), word2Counts.getOrDefault(t.charAt(i), 0) + 1);
        }

        return word1Counts.equals(word2Counts);
    }
}