/**
 * @author Fabian Ha
 * class: 4CN
 * date: 11.11.2024
 * program: WordCount
 */

package enum1;

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
                return null;
            }
        };

        abstract State handleChar(char c, WordCount context);
    }

    int counter;

    public int count(String text) {
        State state = State.NOWORD;
        counter = 0;
        for (char c : text.toCharArray()) {
            state = state.handleChar(c, this);
        }
        return counter;
    }
}
