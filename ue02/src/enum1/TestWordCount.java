package enum1;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class TestWordCount {
    @org.junit.jupiter.api.Test
    public void testCount() throws IOException {
        WordCount wc = new WordCount();
        wc.count(String.valueOf(Files.readAllLines(Path.of("C:\\Users\\fabia\\IdeaProjects\\SEW4_SEM1\\ue02\\src\\enum1\\crsto12.html"))));
        assert wc.counter == 482515; // Mitschüler gefragt nach der Anzahl
    }
}
