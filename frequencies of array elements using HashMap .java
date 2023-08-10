import java.util.*;

public class Main
{
    public static void main(String[] args) {
        int[] arr = {10, 20, 20, 30, 40, 50, 40};
        countFreq(arr);
    }

    public static void countFreq(int arr[]) {
        HashMap<Integer, Integer> h = new HashMap<>();
        for (int x : arr) {
            h.put(x, h.getOrDefault(x, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> e : h.entrySet()) {
            System.out.println(e.getKey() + " " + e.getValue());
        }
    }
}
