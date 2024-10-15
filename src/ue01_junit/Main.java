package ue01_junit;

public class Main {
    public static void main(String[] args) {
        System.out.println(count(("")));
    }

    public static int count(String s) {
        s = s.replaceAll("<[^>]*>", " ");
        s = s.replaceAll("[^a-zA-Z]", " ");
        s = s.trim().replaceAll(" +", " ");

        if (s.isEmpty()) return 0;

        return s.split(" ").length;
    }
}
