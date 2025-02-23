# Generated from main/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u01f6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\7\65\u0159\n\65\f\65\16\65\u015c\13\65\3\66")
        buf.write("\3\66\3\66\7\66\u0161\n\66\f\66\16\66\u0164\13\66\5\66")
        buf.write("\u0166\n\66\3\67\3\67\3\67\6\67\u016b\n\67\r\67\16\67")
        buf.write("\u016c\38\38\38\68\u0172\n8\r8\168\u0173\39\39\39\69\u0179")
        buf.write("\n9\r9\169\u017a\3:\3:\3:\5:\u0180\n:\3;\3;\3<\3<\6<\u0186")
        buf.write("\n<\r<\16<\u0187\5<\u018a\n<\3=\3=\7=\u018e\n=\f=\16=")
        buf.write("\u0191\13=\3>\3>\5>\u0195\n>\3>\3>\3?\3?\7?\u019b\n?\f")
        buf.write("?\16?\u019e\13?\3?\3?\3@\3@\5@\u01a4\n@\3A\3A\3A\3A\5")
        buf.write("A\u01aa\nA\3B\3B\3B\3C\3C\5C\u01b1\nC\3D\3D\3E\5E\u01b6")
        buf.write("\nE\3E\3E\3E\3F\6F\u01bc\nF\rF\16F\u01bd\3F\3F\3G\3G\3")
        buf.write("G\3G\7G\u01c6\nG\fG\16G\u01c9\13G\3G\3G\3H\3H\3H\3H\3")
        buf.write("H\7H\u01d2\nH\fH\16H\u01d5\13H\3H\3H\3H\3H\3H\3I\3I\3")
        buf.write("I\3J\3J\7J\u01e1\nJ\fJ\16J\u01e4\13J\3J\3J\3J\5J\u01e9")
        buf.write("\nJ\3J\3J\3K\3K\7K\u01ef\nK\fK\16K\u01f2\13K\3K\3K\3K")
        buf.write("\3\u01d3\2L\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:s;u\2w\2y\2{\2}<\177\2\u0081\2\u0083\2\u0085")
        buf.write("=\u0087>\u0089?\u008b@\u008dA\u008fB\u0091C\u0093D\u0095")
        buf.write("E\3\2\23\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2")
        buf.write("DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2")
        buf.write("GGgg\4\2--//\5\2\f\f$$^^\7\2$$^^ppttvv\5\2\13\13\16\17")
        buf.write("\"\"\3\2\f\f\3\3\f\f\2\u0205\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\3\u0097\3\2\2\2\5\u009a")
        buf.write("\3\2\2\2\7\u009f\3\2\2\2\t\u00a3\3\2\2\2\13\u00aa\3\2")
        buf.write("\2\2\r\u00af\3\2\2\2\17\u00b4\3\2\2\2\21\u00bb\3\2\2\2")
        buf.write("\23\u00c5\3\2\2\2\25\u00cc\3\2\2\2\27\u00d0\3\2\2\2\31")
        buf.write("\u00d6\3\2\2\2\33\u00de\3\2\2\2\35\u00e4\3\2\2\2\37\u00e8")
        buf.write("\3\2\2\2!\u00f1\3\2\2\2#\u00f7\3\2\2\2%\u00fd\3\2\2\2")
        buf.write("\'\u0101\3\2\2\2)\u0106\3\2\2\2+\u010c\3\2\2\2-\u010e")
        buf.write("\3\2\2\2/\u0110\3\2\2\2\61\u0112\3\2\2\2\63\u0114\3\2")
        buf.write("\2\2\65\u0116\3\2\2\2\67\u0119\3\2\2\29\u011c\3\2\2\2")
        buf.write(";\u011e\3\2\2\2=\u0121\3\2\2\2?\u0123\3\2\2\2A\u0126\3")
        buf.write("\2\2\2C\u0129\3\2\2\2E\u012c\3\2\2\2G\u012e\3\2\2\2I\u0130")
        buf.write("\3\2\2\2K\u0133\3\2\2\2M\u0136\3\2\2\2O\u0139\3\2\2\2")
        buf.write("Q\u013c\3\2\2\2S\u013f\3\2\2\2U\u0141\3\2\2\2W\u0143\3")
        buf.write("\2\2\2Y\u0145\3\2\2\2[\u0147\3\2\2\2]\u014a\3\2\2\2_\u014c")
        buf.write("\3\2\2\2a\u014e\3\2\2\2c\u0150\3\2\2\2e\u0152\3\2\2\2")
        buf.write("g\u0154\3\2\2\2i\u0156\3\2\2\2k\u0165\3\2\2\2m\u0167\3")
        buf.write("\2\2\2o\u016e\3\2\2\2q\u0175\3\2\2\2s\u017c\3\2\2\2u\u0181")
        buf.write("\3\2\2\2w\u0189\3\2\2\2y\u018b\3\2\2\2{\u0192\3\2\2\2")
        buf.write("}\u0198\3\2\2\2\177\u01a3\3\2\2\2\u0081\u01a9\3\2\2\2")
        buf.write("\u0083\u01ab\3\2\2\2\u0085\u01b0\3\2\2\2\u0087\u01b2\3")
        buf.write("\2\2\2\u0089\u01b5\3\2\2\2\u008b\u01bb\3\2\2\2\u008d\u01c1")
        buf.write("\3\2\2\2\u008f\u01cc\3\2\2\2\u0091\u01db\3\2\2\2\u0093")
        buf.write("\u01de\3\2\2\2\u0095\u01ec\3\2\2\2\u0097\u0098\7k\2\2")
        buf.write("\u0098\u0099\7h\2\2\u0099\4\3\2\2\2\u009a\u009b\7g\2\2")
        buf.write("\u009b\u009c\7n\2\2\u009c\u009d\7u\2\2\u009d\u009e\7g")
        buf.write("\2\2\u009e\6\3\2\2\2\u009f\u00a0\7h\2\2\u00a0\u00a1\7")
        buf.write("q\2\2\u00a1\u00a2\7t\2\2\u00a2\b\3\2\2\2\u00a3\u00a4\7")
        buf.write("t\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7")
        buf.write("\7w\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7p\2\2\u00a9\n")
        buf.write("\3\2\2\2\u00aa\u00ab\7h\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad")
        buf.write("\7p\2\2\u00ad\u00ae\7e\2\2\u00ae\f\3\2\2\2\u00af\u00b0")
        buf.write("\7v\2\2\u00b0\u00b1\7{\2\2\u00b1\u00b2\7r\2\2\u00b2\u00b3")
        buf.write("\7g\2\2\u00b3\16\3\2\2\2\u00b4\u00b5\7u\2\2\u00b5\u00b6")
        buf.write("\7v\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8\7w\2\2\u00b8\u00b9")
        buf.write("\7e\2\2\u00b9\u00ba\7v\2\2\u00ba\20\3\2\2\2\u00bb\u00bc")
        buf.write("\7k\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be\7v\2\2\u00be\u00bf")
        buf.write("\7g\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7h\2\2\u00c1\u00c2")
        buf.write("\7c\2\2\u00c2\u00c3\7e\2\2\u00c3\u00c4\7g\2\2\u00c4\22")
        buf.write("\3\2\2\2\u00c5\u00c6\7u\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8")
        buf.write("\7t\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb")
        buf.write("\7i\2\2\u00cb\24\3\2\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce")
        buf.write("\7p\2\2\u00ce\u00cf\7v\2\2\u00cf\26\3\2\2\2\u00d0\u00d1")
        buf.write("\7h\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4")
        buf.write("\7c\2\2\u00d4\u00d5\7v\2\2\u00d5\30\3\2\2\2\u00d6\u00d7")
        buf.write("\7d\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da")
        buf.write("\7n\2\2\u00da\u00db\7g\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd")
        buf.write("\7p\2\2\u00dd\32\3\2\2\2\u00de\u00df\7e\2\2\u00df\u00e0")
        buf.write("\7q\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7u\2\2\u00e2\u00e3")
        buf.write("\7v\2\2\u00e3\34\3\2\2\2\u00e4\u00e5\7x\2\2\u00e5\u00e6")
        buf.write("\7c\2\2\u00e6\u00e7\7t\2\2\u00e7\36\3\2\2\2\u00e8\u00e9")
        buf.write("\7e\2\2\u00e9\u00ea\7q\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec")
        buf.write("\7v\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef")
        buf.write("\7w\2\2\u00ef\u00f0\7g\2\2\u00f0 \3\2\2\2\u00f1\u00f2")
        buf.write("\7d\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5")
        buf.write("\7c\2\2\u00f5\u00f6\7m\2\2\u00f6\"\3\2\2\2\u00f7\u00f8")
        buf.write("\7t\2\2\u00f8\u00f9\7c\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb")
        buf.write("\7i\2\2\u00fb\u00fc\7g\2\2\u00fc$\3\2\2\2\u00fd\u00fe")
        buf.write("\7p\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100\7n\2\2\u0100&\3")
        buf.write("\2\2\2\u0101\u0102\7v\2\2\u0102\u0103\7t\2\2\u0103\u0104")
        buf.write("\7w\2\2\u0104\u0105\7g\2\2\u0105(\3\2\2\2\u0106\u0107")
        buf.write("\7h\2\2\u0107\u0108\7c\2\2\u0108\u0109\7n\2\2\u0109\u010a")
        buf.write("\7u\2\2\u010a\u010b\7g\2\2\u010b*\3\2\2\2\u010c\u010d")
        buf.write("\7-\2\2\u010d,\3\2\2\2\u010e\u010f\7/\2\2\u010f.\3\2\2")
        buf.write("\2\u0110\u0111\7,\2\2\u0111\60\3\2\2\2\u0112\u0113\7\61")
        buf.write("\2\2\u0113\62\3\2\2\2\u0114\u0115\7\'\2\2\u0115\64\3\2")
        buf.write("\2\2\u0116\u0117\7?\2\2\u0117\u0118\7?\2\2\u0118\66\3")
        buf.write("\2\2\2\u0119\u011a\7#\2\2\u011a\u011b\7?\2\2\u011b8\3")
        buf.write("\2\2\2\u011c\u011d\7>\2\2\u011d:\3\2\2\2\u011e\u011f\7")
        buf.write(">\2\2\u011f\u0120\7?\2\2\u0120<\3\2\2\2\u0121\u0122\7")
        buf.write("@\2\2\u0122>\3\2\2\2\u0123\u0124\7@\2\2\u0124\u0125\7")
        buf.write("?\2\2\u0125@\3\2\2\2\u0126\u0127\7(\2\2\u0127\u0128\7")
        buf.write("(\2\2\u0128B\3\2\2\2\u0129\u012a\7~\2\2\u012a\u012b\7")
        buf.write("~\2\2\u012bD\3\2\2\2\u012c\u012d\7#\2\2\u012dF\3\2\2\2")
        buf.write("\u012e\u012f\7?\2\2\u012fH\3\2\2\2\u0130\u0131\7-\2\2")
        buf.write("\u0131\u0132\7?\2\2\u0132J\3\2\2\2\u0133\u0134\7/\2\2")
        buf.write("\u0134\u0135\7?\2\2\u0135L\3\2\2\2\u0136\u0137\7,\2\2")
        buf.write("\u0137\u0138\7?\2\2\u0138N\3\2\2\2\u0139\u013a\7\61\2")
        buf.write("\2\u013a\u013b\7?\2\2\u013bP\3\2\2\2\u013c\u013d\7\'\2")
        buf.write("\2\u013d\u013e\7?\2\2\u013eR\3\2\2\2\u013f\u0140\7\60")
        buf.write("\2\2\u0140T\3\2\2\2\u0141\u0142\7<\2\2\u0142V\3\2\2\2")
        buf.write("\u0143\u0144\7.\2\2\u0144X\3\2\2\2\u0145\u0146\7=\2\2")
        buf.write("\u0146Z\3\2\2\2\u0147\u0148\7<\2\2\u0148\u0149\7?\2\2")
        buf.write("\u0149\\\3\2\2\2\u014a\u014b\7*\2\2\u014b^\3\2\2\2\u014c")
        buf.write("\u014d\7+\2\2\u014d`\3\2\2\2\u014e\u014f\7}\2\2\u014f")
        buf.write("b\3\2\2\2\u0150\u0151\7\177\2\2\u0151d\3\2\2\2\u0152\u0153")
        buf.write("\7]\2\2\u0153f\3\2\2\2\u0154\u0155\7_\2\2\u0155h\3\2\2")
        buf.write("\2\u0156\u015a\t\2\2\2\u0157\u0159\t\3\2\2\u0158\u0157")
        buf.write("\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158\3\2\2\2\u015a")
        buf.write("\u015b\3\2\2\2\u015bj\3\2\2\2\u015c\u015a\3\2\2\2\u015d")
        buf.write("\u0166\7\62\2\2\u015e\u0162\t\4\2\2\u015f\u0161\t\5\2")
        buf.write("\2\u0160\u015f\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160")
        buf.write("\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0166\3\2\2\2\u0164")
        buf.write("\u0162\3\2\2\2\u0165\u015d\3\2\2\2\u0165\u015e\3\2\2\2")
        buf.write("\u0166l\3\2\2\2\u0167\u0168\7\62\2\2\u0168\u016a\t\6\2")
        buf.write("\2\u0169\u016b\t\7\2\2\u016a\u0169\3\2\2\2\u016b\u016c")
        buf.write("\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("n\3\2\2\2\u016e\u016f\7\62\2\2\u016f\u0171\t\b\2\2\u0170")
        buf.write("\u0172\t\t\2\2\u0171\u0170\3\2\2\2\u0172\u0173\3\2\2\2")
        buf.write("\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174p\3\2\2")
        buf.write("\2\u0175\u0176\7\62\2\2\u0176\u0178\t\n\2\2\u0177\u0179")
        buf.write("\t\13\2\2\u0178\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017br\3\2\2\2\u017c")
        buf.write("\u017d\5w<\2\u017d\u017f\5y=\2\u017e\u0180\5{>\2\u017f")
        buf.write("\u017e\3\2\2\2\u017f\u0180\3\2\2\2\u0180t\3\2\2\2\u0181")
        buf.write("\u0182\t\5\2\2\u0182v\3\2\2\2\u0183\u018a\7\62\2\2\u0184")
        buf.write("\u0186\5u;\2\u0185\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187")
        buf.write("\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u018a\3\2\2\2")
        buf.write("\u0189\u0183\3\2\2\2\u0189\u0185\3\2\2\2\u018ax\3\2\2")
        buf.write("\2\u018b\u018f\7\60\2\2\u018c\u018e\5u;\2\u018d\u018c")
        buf.write("\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f")
        buf.write("\u0190\3\2\2\2\u0190z\3\2\2\2\u0191\u018f\3\2\2\2\u0192")
        buf.write("\u0194\t\f\2\2\u0193\u0195\t\r\2\2\u0194\u0193\3\2\2\2")
        buf.write("\u0194\u0195\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197\5")
        buf.write("w<\2\u0197|\3\2\2\2\u0198\u019c\7$\2\2\u0199\u019b\5\177")
        buf.write("@\2\u019a\u0199\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019a")
        buf.write("\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019f\3\2\2\2\u019e")
        buf.write("\u019c\3\2\2\2\u019f\u01a0\7$\2\2\u01a0~\3\2\2\2\u01a1")
        buf.write("\u01a4\n\16\2\2\u01a2\u01a4\5\u0081A\2\u01a3\u01a1\3\2")
        buf.write("\2\2\u01a3\u01a2\3\2\2\2\u01a4\u0080\3\2\2\2\u01a5\u01a6")
        buf.write("\7^\2\2\u01a6\u01aa\t\17\2\2\u01a7\u01a8\7)\2\2\u01a8")
        buf.write("\u01aa\7$\2\2\u01a9\u01a5\3\2\2\2\u01a9\u01a7\3\2\2\2")
        buf.write("\u01aa\u0082\3\2\2\2\u01ab\u01ac\7^\2\2\u01ac\u01ad\n")
        buf.write("\17\2\2\u01ad\u0084\3\2\2\2\u01ae\u01b1\5\'\24\2\u01af")
        buf.write("\u01b1\5)\25\2\u01b0\u01ae\3\2\2\2\u01b0\u01af\3\2\2\2")
        buf.write("\u01b1\u0086\3\2\2\2\u01b2\u01b3\5%\23\2\u01b3\u0088\3")
        buf.write("\2\2\2\u01b4\u01b6\7\17\2\2\u01b5\u01b4\3\2\2\2\u01b5")
        buf.write("\u01b6\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8\7\f\2\2")
        buf.write("\u01b8\u01b9\bE\2\2\u01b9\u008a\3\2\2\2\u01ba\u01bc\t")
        buf.write("\20\2\2\u01bb\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01bf\3\2\2\2")
        buf.write("\u01bf\u01c0\bF\3\2\u01c0\u008c\3\2\2\2\u01c1\u01c2\7")
        buf.write("\61\2\2\u01c2\u01c3\7\61\2\2\u01c3\u01c7\3\2\2\2\u01c4")
        buf.write("\u01c6\n\21\2\2\u01c5\u01c4\3\2\2\2\u01c6\u01c9\3\2\2")
        buf.write("\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01ca")
        buf.write("\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca\u01cb\bG\3\2\u01cb")
        buf.write("\u008e\3\2\2\2\u01cc\u01cd\7\61\2\2\u01cd\u01ce\7,\2\2")
        buf.write("\u01ce\u01d3\3\2\2\2\u01cf\u01d2\5\u008fH\2\u01d0\u01d2")
        buf.write("\13\2\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d0\3\2\2\2\u01d2")
        buf.write("\u01d5\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d3\u01d1\3\2\2\2")
        buf.write("\u01d4\u01d6\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6\u01d7\7")
        buf.write(",\2\2\u01d7\u01d8\7\61\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da")
        buf.write("\bH\3\2\u01da\u0090\3\2\2\2\u01db\u01dc\13\2\2\2\u01dc")
        buf.write("\u01dd\bI\4\2\u01dd\u0092\3\2\2\2\u01de\u01e2\7$\2\2\u01df")
        buf.write("\u01e1\5\177@\2\u01e0\u01df\3\2\2\2\u01e1\u01e4\3\2\2")
        buf.write("\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e8")
        buf.write("\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e5\u01e6\7\17\2\2\u01e6")
        buf.write("\u01e9\7\f\2\2\u01e7\u01e9\t\22\2\2\u01e8\u01e5\3\2\2")
        buf.write("\2\u01e8\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01eb")
        buf.write("\bJ\5\2\u01eb\u0094\3\2\2\2\u01ec\u01f0\7$\2\2\u01ed\u01ef")
        buf.write("\5\177@\2\u01ee\u01ed\3\2\2\2\u01ef\u01f2\3\2\2\2\u01f0")
        buf.write("\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f3\3\2\2\2")
        buf.write("\u01f2\u01f0\3\2\2\2\u01f3\u01f4\5\u0083B\2\u01f4\u01f5")
        buf.write("\bK\6\2\u01f5\u0096\3\2\2\2\32\2\u015a\u0162\u0165\u016c")
        buf.write("\u0173\u017a\u017f\u0187\u0189\u018f\u0194\u019c\u01a3")
        buf.write("\u01a9\u01b0\u01b5\u01bd\u01c7\u01d1\u01d3\u01e2\u01e8")
        buf.write("\u01f0\7\3E\2\b\2\2\3I\3\3J\4\3K\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    FOR = 3
    RETURN = 4
    FUNC = 5
    TYPE = 6
    STRUCT = 7
    INTERFACE = 8
    STRING = 9
    INT = 10
    FLOAT = 11
    BOOLEAN = 12
    CONST = 13
    VAR = 14
    CONTINUE = 15
    BREAK = 16
    RANGE = 17
    NIL = 18
    TRUE = 19
    FALSE = 20
    ADD = 21
    SUB = 22
    MUL = 23
    DIV = 24
    MOD = 25
    EQUAL = 26
    NEQUAL = 27
    LT = 28
    LTE = 29
    GT = 30
    GTE = 31
    AND = 32
    OR = 33
    NOT = 34
    ASSIGN = 35
    ADD_ASSIGN = 36
    SUB_ASSIGN = 37
    MUL_ASSIGN = 38
    DIV_ASSIGN = 39
    MOD_ASSIGN = 40
    DOT = 41
    COLON = 42
    COMMA = 43
    COCOM = 44
    COLONEQUAL = 45
    LPAREN = 46
    RPAREN = 47
    LCPAREN = 48
    RCPAREN = 49
    LSPAREN = 50
    RSPAREN = 51
    ID = 52
    INT_LIT = 53
    BIN_LIT = 54
    OCT_LIT = 55
    HEX_LIT = 56
    FLOAT_LIT = 57
    STRING_LIT = 58
    BOOL_LIT = 59
    NIL_LIT = 60
    NEWLINE = 61
    WS = 62
    COMMENT_LINE = 63
    COMMENT = 64
    ERROR_CHAR = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", "':'", 
            "','", "';'", "':='", "'('", "')'", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "EQUAL", "NEQUAL", "LT", "LTE", "GT", "GTE", "AND", 
            "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
            "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "COLON", "COMMA", "COCOM", 
            "COLONEQUAL", "LPAREN", "RPAREN", "LCPAREN", "RCPAREN", "LSPAREN", 
            "RSPAREN", "ID", "INT_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", 
            "FLOAT_LIT", "STRING_LIT", "BOOL_LIT", "NIL_LIT", "NEWLINE", 
            "WS", "COMMENT_LINE", "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "NEQUAL", 
                  "LT", "LTE", "GT", "GTE", "AND", "OR", "NOT", "ASSIGN", 
                  "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                  "MOD_ASSIGN", "DOT", "COLON", "COMMA", "COCOM", "COLONEQUAL", 
                  "LPAREN", "RPAREN", "LCPAREN", "RCPAREN", "LSPAREN", "RSPAREN", 
                  "ID", "INT_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", "FLOAT_LIT", 
                  "DIGIT", "DIGITS", "FRAC", "EXP", "STRING_LIT", "STRING_CHAR", 
                  "ESC_SEQ", "ESC_ILLEGAL", "BOOL_LIT", "NIL_LIT", "NEWLINE", 
                  "WS", "COMMENT_LINE", "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
        self.preType = None

    def emit(self):
        tk = self.type
        self.preType = tk;
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[67] = self.NEWLINE_action 
            actions[71] = self.ERROR_CHAR_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                if self.preType in [self.ID, self.INT_LIT, self.BIN_LIT, self.OCT_LIT, self.HEX_LIT, self.STRING_LIT, self.FLOAT_LIT,
                                    self.TRUE, self.FALSE, self.INT, self.FLOAT, self.STRING, self.BOOLEAN, self.NIL,
                                    self.RETURN, self.CONTINUE, self.BREAK,
                                    self.RPAREN, self.RCPAREN, self.RSPAREN]:
                    self.text = ";"
                    self.type = self.COCOM
                else:
                    self.skip()

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[:-2])
                elif(self.text[-1] == '\n') :
                    raise UncloseString(self.text[:-1])
                else:
                    raise UncloseString(self.text[:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise IllegalEscape(self.text[:])

     


