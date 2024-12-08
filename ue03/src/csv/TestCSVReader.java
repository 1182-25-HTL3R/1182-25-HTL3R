package csv;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class TestCSVReader {
    @Test
    public void testGetWords() {
        // B1
        assert Arrays.equals(CSVReader.getWords("one,two,three"), new String[]{"one", "two", "three"});
        assert Arrays.equals(CSVReader.getWords("abc,,def123+#+sdaf,ghi"), new String[]{"abc", "", "def123+#+sdaf", "ghi"});

        // B2
        assert Arrays.equals(CSVReader.getWords("\"uno\",dos,\"tres, cuatro\",cin\"co\""), new String[]{"uno", "dos", "tres, cuatro", "cinco"});
        IllegalArgumentException excp = Assertions.assertThrows(IllegalArgumentException.class, () -> {
            CSVReader.getWords("\"hall\"o");
        });

        excp = Assertions.assertThrows(IllegalArgumentException.class, () -> {
            CSVReader.getWords("\"hallo");
        });

        // B3
        assert Arrays.equals(CSVReader.getWords("\"ein,s\",\"zw\"\"ei\",drei"), new String[]{"ein,s", "zw\"ei", "drei"});
        assert Arrays.equals(CSVReader.getWords("\"\"\"ein,s\"\"\""), new String[]{"\"ein,s\""});

    }
}
