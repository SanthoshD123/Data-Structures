import java.util.*;

public class Main {
    public static void main(String[] args) {
        String str = "{()}";
        System.out.print(isBalanced(str));
    }

    public static boolean isBalanced(String str) {
        Stack<Character> s = new Stack<>();

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (c == '(' || c == '{') {
                s.push(c);
            } else {
                if (s.isEmpty()) {
                    return false;
                } else if (!matching(s.peek(), c)) {
                    return false;
                } else {
                    s.pop();
                }
            }
        }
        
        return s.isEmpty();
    }

    public static boolean matching(char a, char b) {
        return ((a == '(' && b == ')') || (a == '{' && b == '}'));
    }
}
