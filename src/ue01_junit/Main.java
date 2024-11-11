package ue01_junit;

public class Main {
    /**
     * Methode zum Zählen der Worte
     * @param s Input-String
     * @return Anzahl der Worte
     */
    public static int count(String s) {
        s = s.replaceAll("<((\".*\")|([^>\"]*))*>", " ");
        s = s.replaceAll("<.*", " ");
        s = s.replaceAll("[^a-zA-Z]", " ");
        s = s.trim().replaceAll(" +", " ");
        if (s.isEmpty()) return 0;
        return s.split(" ").length;
    }
}