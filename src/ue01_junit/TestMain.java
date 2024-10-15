package ue01_junit;

import static ue01_junit.Main.count;

public class TestMain {
    @org.junit.jupiter.api.Test
    public void testCount() {
        assert count("") == 0;
    }
}
