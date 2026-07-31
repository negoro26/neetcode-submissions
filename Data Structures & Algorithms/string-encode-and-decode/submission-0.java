class Solution {

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();

        for (String s : strs) {
            res.append(s.length()).append("#").append(s);
        }
        
        return res.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();

        int i = 0;

        while (i < str.length()) {
            int j = str.indexOf('#', i);

            int length = Integer.valueOf(str.substring(i, j));

            int start = j + 1;
            int end = start + length;

            res.add(str.substring(start, end));

            i = end;
        }

        return res;
    }
}
