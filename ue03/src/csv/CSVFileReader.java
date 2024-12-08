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

    /**
     * gibt die Wörter der nächsten Zeile aus
     * @return Wörter der nächsten Zeile als String Array von CSVReader
     * @throws IOException Wenn das File nicht existiert
     */
    public String[] next() throws IOException {
        String output = br.readLine();
        if (output == null) {   // End-Of-Line ist wenn output gleich null
            return null;
        }
        return reader.getWords(output);
    }

    /**
     * um den Reader zu schließen z.B. in einem try-catch-Block
     * @throws IOException Wenn das File nicht existiert
     */
    @Override
    public void close() throws IOException {
        br.close();
    }

    /**
     * Damit man über den CSVFileReader iterieren kann
     * @return Iterator Objekt
     */
    @Override
    public Iterator<String[]> iterator() {
        return new Iterator<String[]>() {
            private String[] nextLine = getNextLine();

            /**
             * Methode, die die Wörter der nächsten Zeile zurückgibt
             * @return Wörter der nächsten Zeile
             */
            public String[] getNextLine() {
                try {
                    return CSVFileReader.this.next();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }

            /**
             * überprüft, ob es eine nächste Zeile gibt
             * @return true -> gibt eine nächste Zeile, false -> keine nächste Zeile
             */
            @Override
            public boolean hasNext() {
                return nextLine != null;
            }

            /**
             * Methode, die die Wörter der nächsten Zeile zurückgibt
             * @return Wörter der nächsten Zeile
             */
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
