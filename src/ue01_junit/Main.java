package ue01_junit;

import java.util.Arrays;

public class Main {
    public static int count(String s) {
        s = s.replaceAll("<((\".*\")|([^>\"]*))*>", " ");
        s = s.replaceAll("<.*", " ");
        s = s.replaceAll("[^a-zA-Z]", " ");
        s = s.trim().replaceAll(" +", " ");

        if (s.isEmpty()) return 0;
        return s.split(" ").length;
    }
}
