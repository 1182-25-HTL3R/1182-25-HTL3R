package csv;

import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class TestCSVReader {
    @Test
    public void testGetWords() {
        assert Arrays.equals(CSVReader.getWords("one,two,three"), new String[]{"one", "two", "three"});
        assert Arrays.equals(CSVReader.getWords("abc,,def123+#+sdaf,ghi"), new String[]{"abc", "", "def123+#+sdaf", "ghi"});
    }
}
