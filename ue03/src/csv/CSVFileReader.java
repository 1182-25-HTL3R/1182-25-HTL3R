package csv;

import java.io.*;
import java.util.Iterator;
import java.util.NoSuchElementException;

public class CSVFileReader implements Iterable<String[]>, Closeable {
    private CSVReader reader;
    private BufferedReader br;

    public CSVFileReader(String filename, char delimiter, char doublequote, boolean skipinitialwhitespace) throws FileNotFoundException {
        br = new BufferedReader(new FileReader(filename));
        reader = new CSVReader(delimiter, doublequote, skipinitialwhitespace);
    }

    public String[] next() throws IOException {
        String output = br.readLine();
        if (output == null) {   // End-Of-Line ist wenn output gleich null
            return null;
        }
        return reader.getWords(output);
    }

    @Override
    public void close() throws IOException {
        br.close();
    }

    @Override
    public Iterator<String[]> iterator() {
        return new Iterator<String[]>() {
            private String[] nextLine = getNextLine();

            public String[] getNextLine() {
                try {
                    return CSVFileReader.this.next();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }

            @Override
            public boolean hasNext() {
                return nextLine != null;
            }

            @Override
            public String[] next() {
                if (!hasNext()) {
                    throw new NoSuchElementException();
                }

                String[] result = nextLine;
                nextLine = getNextLine();
                return result;
            }
        };
    }
}
