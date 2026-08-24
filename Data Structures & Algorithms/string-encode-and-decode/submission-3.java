class Solution {

    public String encode(List<String> strs) {

        StringBuilder sb = new StringBuilder();
        for (String str : strs) {
            int length = str.length();

            sb.append(length);
            sb.append("#");
            sb.append(str);
        }

        return sb.toString();
    }

    public List<String> decode(String str) {

        List<String> ret = new ArrayList<>();

        int i = 0;
        while (i < str.length()) {
            int j = i;

            while (str.charAt(j) != '#') {
                j++;
            }

            int length = Integer.parseInt(str.substring(i, j));

            ret.add(str.substring(j + 1, j + length + 1));

            i = j + length + 1;
        }

        return ret;
    }
}
