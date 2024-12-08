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
                } else {
                    word += ch;
                }

                return this;
            }
        };

        abstract State handleChar(char ch);
    }

    public static String[] getWords(String s) {
        word = "";
        words = new ArrayList<>();
        State ZEICHEN = State.ZEICHEN;
        for (char ch : s.toCharArray()) {
            ZEICHEN = ZEICHEN.handleChar(ch);
        }
        words.add(word);
        return words.toArray(new String[0]);
    }
}
