//  // leicht
//  count("") == 0
//  count(" ") == 0
//  count("  ") == 0
//
//  // normal
//  count("one") == 1
//  count(" one") == 1
//  count("one ") == 1
//  count(" one ") == 1
//  count(" one  ") == 1
//  count("  one ") == 1
//  count("  one  ") == 1
//
//  count("one:") == 1
//  count(":one") == 1
//  count(":one:") == 1
//  count(" one  ") == 1
//  count(" one : ") == 1
//  count(": one :") == 1
//  count("ein erster Text") == 3
//  count(" ein  erster   Text      ") == 3
//  count("ein:erster.Text") == 3
//
//  // vielleicht falsch
//  count("a") == 1
//  count(" a") == 1
//  count("a ") == 1
//  count(" a ") == 1
//
//  // mit html
//  count(" one  <html> ") == 1
//  count(" one  < html> ") == 1
//  count(" one  <html > ") == 1
//  count(" one  < html > ") == 1
//  count(" one <html> two<html>three <html> four") == 4
//
//  count(" one <html> two ") == 2
//  count(" one <html>two ") == 2
//  count(" one<html> two ") == 2
//  count(" one<html>two ") == 2
//  count(" one<img alt=\"xxx\" > two") == 2
//  count(" one<img alt=\"xxx yyy\" > two") == 2
//
//  count(" one \"two\" ") == 2
//  count(" one\"two\" ") == 2
//  count(" one \"two\"") == 2
//  count(" one \"two\"three") == 3
//  count(" one \"two\" three") == 3
//
//  // html - trickreich
//  // Achtung: das ist teilweise nicht ganz legales HTML
//  count(" one<html") == 1 // kein >
//
//  count(" one<img alt=\"<bild>\" > two") == 2 // <> innerhalb ""
//  count(" one<img alt=\"bild>\" > two") == 2 // <> innerhalb ""
//  count(" one<img alt=\"<bild>\" keinwort> two") == 2
//  count(" one<img alt=\"<bild>\" src=\"bild.png\" >two") == 2
//  count(" one<img alt=\"<bild\" keinwort>two") == 2
//
//  count(" one<img alt=\"<bild\" keinwort") == 1
//  count(" one<img alt=\"<bild\" keinwort> two") == 2
//  count(" one<img alt=\"<bild keinwort> keinwort") == 1
//  count(" one<img alt=\"<bild keinwort keinwort\">two") == 2
//  count(" one<img alt=\"<bild keinwort< keinwort\">two") == 2
//
//  // ganz ganz fies -- \ entwertet das nächste Zeichen
//  count(" one<img alt=\"<bild \\\" keinwort> keinwort\" keinwort>two") == 2
//  count(" one<img alt=\"<bild \\\" keinwort<keinwort\" keinwort>two") == 2
//  count(" one<img alt=\"<bild \\\" keinwort keinwort\" keinwort>two") == 2
//
//  count(" \\\"null\\\" one<img alt=\"<bild \\\" keinwort keinwort\" keinwort>two \"three\"") == 4
