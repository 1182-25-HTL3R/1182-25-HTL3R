package csv;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class TestCSVReader {
    @Test
    public void testGetWords() {
        CSVReader reader = new CSVReader(',', '"', true);
        // B1
        assert Arrays.equals(reader.getWords("one,two,three"), new String[]{"one", "two", "three"});
        assert Arrays.equals(reader.getWords("abc,,def123+#+sdaf,ghi"), new String[]{"abc", "", "def123+#+sdaf", "ghi"});

        // B2
        assert Arrays.equals(reader.getWords("\"uno\",dos,\"tres, cuatro\",cin\"co\""), new String[]{"uno", "dos", "tres, cuatro", "cinco"});
        IllegalArgumentException excp = Assertions.assertThrows(IllegalArgumentException.class, () -> {
            reader.getWords("\"hall\"o");
        });

        excp = Assertions.assertThrows(IllegalArgumentException.class, () -> {
            reader.getWords("\"hallo");
        });

        // B3
        assert Arrays.equals(reader.getWords("\"ein,s\",\"zw\"\"ei\",drei"), new String[]{"ein,s", "zw\"ei", "drei"});
        assert Arrays.equals(reader.getWords("\"\"\"ein,s\"\"\""), new String[]{"\"ein,s\""});

        // B4
        assert Arrays.equals(reader.getWords("    \"ab,cd\""), new String[]{"ab,cd"});
        assert Arrays.equals(reader.getWords("    \"ab,cd\",     efg"), new String[]{"ab,cd", "efg"});

        CSVReader reader2 = new CSVReader('#', '+', false);
        assert Arrays.equals(reader2.getWords("   one#two#t+hree+"), new String[]{"   one", "two", "three"});
        assert Arrays.equals(reader2.getWords("abc##+def123sdaf+#ghi"), new String[]{"abc", "", "def123sdaf", "ghi"});
    }
}
