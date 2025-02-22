/**
 * @author Fabian Ha
 * class: 4CN
 * date: 24.11.2024
 * program: WordCount
 */
package secondtry;

public class WordCount {
    private enum State {
        NOWORD {
            @Override
            State handleChar(char c) {
                if (Character.isLetter(c)) {
                    counter++;
                    return INWORD;
                } else if (c == '<') {
                    return TAG;
                } else {
                    return this;
                }
            }
        },
        INWORD {
            @Override
            State handleChar(char c) {
                if (c == '<') {
                    return TAG;
                }
                if (!Character.isLetter(c)) {
                    return NOWORD;
                }
                return this;
            }
        },
        TAG {
            @Override
            State handleChar(char c) {
                if (c == '"') {
                    return ALTTEXT;
                } else if (c == '>') {
                    return NOWORD;
                } else {
                    return this;
                }
            }
        },
        ALTTEXT {
            @Override
            State handleChar(char c) {
                if (c == '\\') {
                    return BACKSLASH_ALTTEXT;
                }

                if (c == '\"') {
                    return TAG;
                } else {
                    return this;
                }
            }
        },
        BACKSLASH_ALTTEXT {
            @Override
            State handleChar(char c) {
                return ALTTEXT;
            }
        };

        abstract State handleChar(char c);
    }

    /**
     * Globaler Zähler für die Anzahl der Wörter.
     */
    public static int counter = 0;

    /**
     * Zählt die Anzahl der Wörter im String text.
     * @param text String von welchem die Anzahl der Wörter ermittelt wird
     * @return Anzahl der Wörter
     */
    public static int count(String text) {
        State state = State.NOWORD;
        counter = 0;
        for (char c : text.toCharArray()) {
            state = state.handleChar(c);
        }
        return counter;
    }
}
