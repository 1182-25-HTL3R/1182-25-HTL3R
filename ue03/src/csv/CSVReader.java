/**
 * @author Fabian Ha
 * class: 4CN
 * date: 05.12.2024
 * program: CSVReader
 */

package csv;

import java.util.ArrayList;

public class CSVReader {
    public static ArrayList<String> words = new ArrayList<>();
    public static String word = "";

    enum State {
        ZEICHEN {
            @Override
            State handleChar(char ch) {
                if (ch == ',') {
                    words.add(word);
                    word = "";
                } if (ch == '"') {
                    return INSTRING;
                }else {
                    word += ch;
                }

                return this;
            }
        },
        INSTRING {
            State handleChar(char ch) {
                if (ch == '"') {
                    return AFTERSTRING;
                }

                word += ch;
                return INSTRING;
            }
        },
        AFTERSTRING {
            State handleChar(char ch) {
                if (ch == ',') {
                    words.add(word);
                    word = "";
                    return ZEICHEN;
                } else if (ch == '"') {
                    return INSTRING;
                }

                throw new IllegalArgumentException();
            }
        };

        abstract State handleChar(char ch);
    }

    public static String[] getWords(String s) {
        word = "";
        words = new ArrayList<>();
        State st = State.ZEICHEN;
        for (char ch : s.toCharArray()) {
            st = st.handleChar(ch);
        }

        if (st == State.INSTRING) {
            throw new IllegalArgumentException();
        }

        words.add(word);
        return words.toArray(new String[0]);
    }
}
