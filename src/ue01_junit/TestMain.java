package ue01_junit;

import static ue01_junit.Main.count;

public class TestMain {
    @org.junit.jupiter.api.Test
    public void testCount() {
        assert count("") == 0;
        // leicht
        assert count("") == 0;
        assert count(" ") == 0;
        assert count("  ") == 0;

        // normal
        assert count("one") == 1;
        assert count(" one") == 1;
        assert count("one ") == 1;
        assert count(" one ") == 1;
        assert count(" one  ") == 1;
        assert count("  one ") == 1;
        assert count("  one  ") == 1;

        assert count("one:") == 1;
        assert count(":one") == 1;
        assert count(":one:") == 1;
        assert count(" one  ") == 1;
        assert count(" one : ") == 1;
        assert count(": one :") == 1;
        assert count("ein erster Text") == 3;
        assert count(" ein  erster   Text      ") == 3;
        assert count("ein:erster.Text") == 3;

        // vielleicht falsch
        assert count("a") == 1;
        assert count(" a") == 1;
        assert count("a ") == 1;
        assert count(" a ") == 1;

        // mit html
        assert count(" one  <html> ") == 1;
        assert count(" one  < html> ") == 1;
        assert count(" one  <html > ") == 1;
        assert count(" one  < html > ") == 1;
        assert count(" one <html> two<html>three <html> four") == 4;

        assert count(" one <html> two ") == 2;
        assert count(" one <html>two ") == 2;
        assert count(" one<html> two ") == 2;
        assert count(" one<html>two ") == 2;
        assert count(" one<img alt=\"xxx\" > two") == 2;
        assert count(" one<img alt=\"xxx yyy\" > two") == 2;

        assert count(" one \"two\" ") == 2;
        assert count(" one\"two\" ") == 2;
        assert count(" one \"two\"") == 2;
        assert count(" one \"two\" three") == 3;
        assert count(" one \"two\"three") == 3;

        // html - trickreich
        // Achtung: das ist teilweise nicht ganz legales HTML
        assert count(" one<html") == 1; // kein >

        assert count(" one<img alt=\"<bild>\" > two") == 2; // <> innerhalb ""
        assert count(" one<img alt=\"bild>\" > two") == 2; // <> innerhalb ""
        assert count(" one<img alt=\"<bild>\" keinwort> two") == 2;
        assert count(" one<img alt=\"<bild>\" src=\"bild.png\" >two") == 2;
        assert count(" one<img alt=\"<bild\" keinwort>two") == 2;

        assert count(" one<img alt=\"<bild\" keinwort") == 1;
        assert count(" one<img alt=\"<bild\" keinwort> two") == 2;
        assert count(" one<img alt=\"<bild keinwort> keinwort") == 1;
        assert count(" one<img alt=\"<bild keinwort keinwort\">two") == 2;
        assert count(" one<img alt=\"<bild keinwort< keinwort\">two") == 2;

        // ganz ganz fies -- \ entwertet das nächste Zeichen
        assert count(" one<img alt=\"<bild \\\" keinwort> keinwort\" keinwort>two") == 2;
        assert count(" one<img alt=\"<bild \\\" keinwort<keinwort\" keinwort>two") == 2;
        assert count(" one<img alt=\"<bild \\\" keinwort keinwort\" keinwort>two") == 2;

        assert count(" \\\"null\\\" one<img alt=\"<bild \\\" keinwort keinwort\" keinwort>two \"three\"") == 4;
    }
}
