package ue01_junit;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        System.out.println(count((" \\\"null\\\" one<img alt=\"<bild \\\" keinwort keinwort\" keinwort>two \"three\"")));
    }

    public static int count(String s) {
        s = s.replaceAll("<[^>]*>", " ");
        s = s.replaceAll("[^a-zA-Z]", " ");
        s = s.trim().replaceAll(" +", " ");
        String[] splitted = s.split(" ");
        System.out.println(Arrays.toString(splitted));
        return splitted.length;
    }
}
