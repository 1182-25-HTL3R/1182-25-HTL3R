/**
 * @author Fabian Ha
 * class: 4CN
 * date: 05.12.2024
 * program: CSVReader
 */

package csv;

import java.util.ArrayList;
import java.util.Arrays;

public class CSVReader {
    private ArrayList<String> words;
    private String word;
    private char delimiter;
    private char doublequote;
    private boolean skipinitialspace;

    public CSVReader(char delimiter, char doublequote, boolean skipinitialspace) {
        this.delimiter = delimiter;
        this.doublequote = doublequote;
        this.skipinitialspace = skipinitialspace;
        this.words = new ArrayList<>();
        this.word = "";
    }

    enum State {
        WHITESPACE {
            State handleChar(char ch, CSVReader reader) {
                if (reader.skipinitialspace && Character.isWhitespace(ch)) {
                    return WHITESPACE;
                } else {
                    return State.ZEICHEN.handleChar(ch, reader);
                }
            }
        },
        ZEICHEN {
            @Override
            State handleChar(char ch, CSVReader reader) {
                if (ch == reader.delimiter) {
                    reader.words.add(reader.word);
                    reader.word = "";
                    return WHITESPACE;
                } else if (ch == reader.doublequote) {
                    return INSTRING;
                } else {
                    reader.word += ch;
                    return ZEICHEN;
                }
            }
        },
        INSTRING {
            State handleChar(char ch, CSVReader reader) {
                if (ch == reader.doublequote) {
                    return AFTERSTRING;
                }

                reader.word += ch;
                return INSTRING;
            }
        },
        AFTERSTRING {
            State handleChar(char ch, CSVReader reader) {
                if (ch == reader.delimiter) {
                    reader.words.add(reader.word);
                    reader.word = "";
                    return WHITESPACE;
                } else if (ch == reader.doublequote) {
                    reader.word += reader.doublequote;
                    return INSTRING;
                }

                throw new IllegalArgumentException();
            }
        };

        abstract State handleChar(char ch, CSVReader reader);
    }

    public String[] getWords(String s) {
        word = "";
        words = new ArrayList<>();
        State st = State.WHITESPACE;
        for (char ch : s.toCharArray()) {
            st = st.handleChar(ch, this);
        }

        if (st == State.INSTRING) {
            throw new IllegalArgumentException();
        }

        words.add(word);
        return words.toArray(new String[0]);
    }

    public static void main(String[] args) {
        CSVReader reader = new CSVReader(',', '"', false);
        System.out.println(Arrays.toString(reader.getWords("\"uno\",dos")));
    }
}
