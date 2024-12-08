package csv;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Arrays;
import java.util.Objects;

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

        // B5
        CSVReader reader2 = new CSVReader('#', '+', false);
        assert Arrays.equals(reader2.getWords("   one#two#t+hree+"), new String[]{"   one", "two", "three"});
        assert Arrays.equals(reader2.getWords("abc##+def123sdaf+#ghi"), new String[]{"abc", "", "def123sdaf", "ghi"});

        // B6
        try (
                CSVFileReader reader3 = new CSVFileReader("C:\\Users\\fabia\\IdeaProjects\\SEW4_SEM1\\ue03\\src\\csv\\file.csv", ';', '\"', true)) {
            assert Arrays.equals(reader3.next(), new String[]{"", "A", "B", "C", "D", "E", "F", "G", "H"});
            assert Arrays.equals(reader3.next(), new String[]{"A", "", "4", "7", "8", "", "", "", ""});
            assert Arrays.equals(reader3.next(), new String[]{"B", "4", "", "", "", "5", "3", "", ""});
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] args) throws IOException {
        try (
                CSVFileReader reader = new CSVFileReader("C:\\Users\\fabia\\IdeaProjects\\SEW4_SEM1\\ue03\\src\\csv\\file.csv", ';', '\"', true)) {
            String[] firstRow = reader.next();
            for (String[] row : reader) {
                System.out.print(row[0]);
                String s = ":";
                for (int i = 1; i < row.length; i++) {
                    if (!Objects.equals(row[i], "")) {
                        s += " nach " + firstRow[i] + ":" + row[i] + ",";
                    }
                }
                s = s.substring(0, s.length() - 1);
                System.out.println(s);
            }
        }
    }
}
