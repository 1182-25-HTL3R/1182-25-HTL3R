/**
 * @author Fabian Ha
 * class: 4CN
 * date: 11.11.2024
 * program: WordCount
 */

package wordcount;

public class WordCount {
    enum State {
        NOWORD {
            @Override
            State handleChar(char c, WordCount context) {
                if (Character.isLetter(c)) {
                    context.counter++;
                    return INWORD;
                } else {
                    return this;
                }
            }
        },
        INWORD {
            @Override
            State handleChar(char c, WordCount context) {
                if (! Character.isLetter(c)) {
                    return NOWORD;
                } else {
                    return this;
                }
            }
        };

        abstract State handleChar(char c, WordCount context);
    }

    int counter;

    /**
     * Funktion zum Zählen der Worte
     * @param text Text, dessen Wörter gezählt werden
     * @return Anzahl der Wörter
     */
    public int count(String text) {
        State state = State.NOWORD;
        counter = 0;
        for (char c : text.toCharArray()) {
            state = state.handleChar(c, this);
        }
        return counter;
    }
}
