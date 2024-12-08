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
    public static ArrayList<String> words = new ArrayList<>();
    public static String word = "";

    enum State {
        WHITESPACE {
            State handleChar(char ch) {
                if (Character.isWhitespace(ch)) {
                    return WHITESPACE;
                } else if (ch == ',') {
                    words.add(word);
                    word = "";
                    return WHITESPACE;
                } else if (ch == '"') {
                    return INSTRING;
                } else {
                    word += ch;
                    return ZEICHEN;
                }
            }
        },
        ZEICHEN {
            @Override
            State handleChar(char ch) {
                if (ch == ',') {
                    words.add(word);
                    word = "";
                    return WHITESPACE;
                } else if (ch == '"') {
                    return INSTRING;
                } else {
                    word += ch;
                    return ZEICHEN;
                }
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
                    return WHITESPACE;
                } else if (ch == '"') {
                    word += "\"";
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
        State st = State.WHITESPACE;
        for (char ch : s.toCharArray()) {
            st = st.handleChar(ch);
        }

        if (st == State.INSTRING) {
            throw new IllegalArgumentException();
        }

        words.add(word);
        return words.toArray(new String[0]);
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(getWords("\"uno\",dos")));
    }
}
