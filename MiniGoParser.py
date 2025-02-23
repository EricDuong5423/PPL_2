# Generated from main/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u026b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0082\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u008a\n\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6\u0096\n\6\3\6\3\6\5\6\u009a")
        buf.write("\n\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u00a2\n\7\3\7\3\7\5\7")
        buf.write("\u00a6\n\7\3\7\3\7\5\7\u00aa\n\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\5\b\u00b4\n\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\5")
        buf.write("\n\u00bd\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5")
        buf.write("\13\u00c7\n\13\3\13\3\13\5\13\u00cb\n\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u00ed\n\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00fa\n\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u0102\n\20\3\21\3")
        buf.write("\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u010d\n\23")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u011d\n\26\3\27\3\27\3\27\3\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\5\30\u0128\n\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\5\31\u012f\n\31\3\32\3\32\3\32\3\32\5\32\u0135")
        buf.write("\n\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\5\33\u013e\n")
        buf.write("\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u0149\n\35\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u0151\n")
        buf.write("\36\f\36\16\36\u0154\13\36\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\7\37\u015c\n\37\f\37\16\37\u015f\13\37\3 \3 \3 \3")
        buf.write(" \3 \3 \7 \u0167\n \f \16 \u016a\13 \3!\3!\3!\3!\3!\3")
        buf.write("!\7!\u0172\n!\f!\16!\u0175\13!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\7\"\u017d\n\"\f\"\16\"\u0180\13\"\3#\3#\3#\5#\u0185\n")
        buf.write("#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\7$\u0199\n$\f$\16$\u019c\13$\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\5%\u01a9\n%\3&\3&\5&\u01ad\n&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\5\'\u01b4\n\'\3(\3(\3(\3(\5(\u01ba\n(\3)\3)\3)")
        buf.write("\3)\3)\3)\3)\3)\3)\3)\5)\u01c6\n)\3*\3*\3+\3+\3+\3+\3")
        buf.write("+\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01db\n-\7-\u01dd")
        buf.write("\n-\f-\16-\u01e0\13-\3.\3.\3.\5.\u01e5\n.\3.\3.\3/\3/")
        buf.write("\3/\3/\3/\3/\3/\5/\u01f0\n/\3/\3/\5/\u01f4\n/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\5\60\u01fc\n\60\3\60\3\60\5\60\u0200")
        buf.write("\n\60\3\60\5\60\u0203\n\60\3\60\3\60\3\61\3\61\3\61\5")
        buf.write("\61\u020a\n\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u021d")
        buf.write("\n\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\5\65\u022b\n\65\3\65\3\65\5\65\u022f\n\65\3")
        buf.write("\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\38\38\38\3")
        buf.write("8\58\u023e\n8\38\38\38\38\58\u0244\n8\38\38\38\39\39\3")
        buf.write("9\59\u024c\n9\39\39\3:\3:\3:\3:\3;\3;\3;\3<\3<\3<\3<\3")
        buf.write("<\5<\u025c\n<\3=\3=\3=\3=\5=\u0262\n=\3=\3=\3=\5=\u0267")
        buf.write("\n=\3=\3=\3=\2\t:<>@BFX>\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b")
        buf.write("dfhjlnprtvx\2\t\4\2\13\16\66\66\3\2\66\67\3\2\34!\3\2")
        buf.write("\27\30\3\2\31\33\4\2\30\30$$\4\2&*//\2\u0288\2z\3\2\2")
        buf.write("\2\4\u0081\3\2\2\2\6\u0089\3\2\2\2\b\u008b\3\2\2\2\n\u0091")
        buf.write("\3\2\2\2\f\u009d\3\2\2\2\16\u00b3\3\2\2\2\20\u00b5\3\2")
        buf.write("\2\2\22\u00bc\3\2\2\2\24\u00be\3\2\2\2\26\u00d1\3\2\2")
        buf.write("\2\30\u00d9\3\2\2\2\32\u00ec\3\2\2\2\34\u00f9\3\2\2\2")
        buf.write("\36\u0101\3\2\2\2 \u0103\3\2\2\2\"\u0105\3\2\2\2$\u010c")
        buf.write("\3\2\2\2&\u010e\3\2\2\2(\u0112\3\2\2\2*\u011c\3\2\2\2")
        buf.write(",\u011e\3\2\2\2.\u0127\3\2\2\2\60\u012e\3\2\2\2\62\u0130")
        buf.write("\3\2\2\2\64\u013d\3\2\2\2\66\u013f\3\2\2\28\u0148\3\2")
        buf.write("\2\2:\u014a\3\2\2\2<\u0155\3\2\2\2>\u0160\3\2\2\2@\u016b")
        buf.write("\3\2\2\2B\u0176\3\2\2\2D\u0184\3\2\2\2F\u0186\3\2\2\2")
        buf.write("H\u01a8\3\2\2\2J\u01ac\3\2\2\2L\u01b3\3\2\2\2N\u01b9\3")
        buf.write("\2\2\2P\u01c5\3\2\2\2R\u01c7\3\2\2\2T\u01c9\3\2\2\2V\u01ce")
        buf.write("\3\2\2\2X\u01d0\3\2\2\2Z\u01e1\3\2\2\2\\\u01e8\3\2\2\2")
        buf.write("^\u01f5\3\2\2\2`\u0206\3\2\2\2b\u020f\3\2\2\2d\u021c\3")
        buf.write("\2\2\2f\u0224\3\2\2\2h\u0226\3\2\2\2j\u0233\3\2\2\2l\u0236")
        buf.write("\3\2\2\2n\u023d\3\2\2\2p\u0248\3\2\2\2r\u024f\3\2\2\2")
        buf.write("t\u0253\3\2\2\2v\u025b\3\2\2\2x\u025d\3\2\2\2z{\5\4\3")
        buf.write("\2{|\7\2\2\3|\3\3\2\2\2}~\5\6\4\2~\177\5\4\3\2\177\u0082")
        buf.write("\3\2\2\2\u0080\u0082\5\6\4\2\u0081}\3\2\2\2\u0081\u0080")
        buf.write("\3\2\2\2\u0082\5\3\2\2\2\u0083\u008a\5\n\6\2\u0084\u008a")
        buf.write("\5\b\5\2\u0085\u008a\5\f\7\2\u0086\u008a\5\24\13\2\u0087")
        buf.write("\u008a\5\26\f\2\u0088\u008a\5\30\r\2\u0089\u0083\3\2\2")
        buf.write("\2\u0089\u0084\3\2\2\2\u0089\u0085\3\2\2\2\u0089\u0086")
        buf.write("\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u0088\3\2\2\2\u008a")
        buf.write("\7\3\2\2\2\u008b\u008c\7\17\2\2\u008c\u008d\7\66\2\2\u008d")
        buf.write("\u008e\7%\2\2\u008e\u008f\5:\36\2\u008f\u0090\7.\2\2\u0090")
        buf.write("\t\3\2\2\2\u0091\u0092\7\20\2\2\u0092\u0099\7\66\2\2\u0093")
        buf.write("\u009a\5\36\20\2\u0094\u0096\5\36\20\2\u0095\u0094\3\2")
        buf.write("\2\2\u0095\u0096\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098")
        buf.write("\7%\2\2\u0098\u009a\5:\36\2\u0099\u0093\3\2\2\2\u0099")
        buf.write("\u0095\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c\7.\2\2")
        buf.write("\u009c\13\3\2\2\2\u009d\u009e\7\7\2\2\u009e\u009f\7\66")
        buf.write("\2\2\u009f\u00a1\7\60\2\2\u00a0\u00a2\5\16\b\2\u00a1\u00a0")
        buf.write("\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write("\u00a5\7\61\2\2\u00a4\u00a6\5\36\20\2\u00a5\u00a4\3\2")
        buf.write("\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a9")
        buf.write("\7\62\2\2\u00a8\u00aa\5N(\2\u00a9\u00a8\3\2\2\2\u00a9")
        buf.write("\u00aa\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\7\63\2")
        buf.write("\2\u00ac\u00ad\7.\2\2\u00ad\r\3\2\2\2\u00ae\u00af\5\20")
        buf.write("\t\2\u00af\u00b0\7-\2\2\u00b0\u00b1\5\16\b\2\u00b1\u00b4")
        buf.write("\3\2\2\2\u00b2\u00b4\5\20\t\2\u00b3\u00ae\3\2\2\2\u00b3")
        buf.write("\u00b2\3\2\2\2\u00b4\17\3\2\2\2\u00b5\u00b6\5\22\n\2\u00b6")
        buf.write("\u00b7\5\36\20\2\u00b7\21\3\2\2\2\u00b8\u00b9\7\66\2\2")
        buf.write("\u00b9\u00ba\7-\2\2\u00ba\u00bd\5\22\n\2\u00bb\u00bd\7")
        buf.write("\66\2\2\u00bc\u00b8\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd")
        buf.write("\23\3\2\2\2\u00be\u00bf\7\7\2\2\u00bf\u00c0\7\60\2\2\u00c0")
        buf.write("\u00c1\7\66\2\2\u00c1\u00c2\7\66\2\2\u00c2\u00c3\7\61")
        buf.write("\2\2\u00c3\u00c4\7\66\2\2\u00c4\u00c6\7\60\2\2\u00c5\u00c7")
        buf.write("\5\16\b\2\u00c6\u00c5\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7")
        buf.write("\u00c8\3\2\2\2\u00c8\u00ca\7\61\2\2\u00c9\u00cb\5\36\20")
        buf.write("\2\u00ca\u00c9\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc")
        buf.write("\3\2\2\2\u00cc\u00cd\7\62\2\2\u00cd\u00ce\5N(\2\u00ce")
        buf.write("\u00cf\7\63\2\2\u00cf\u00d0\7.\2\2\u00d0\25\3\2\2\2\u00d1")
        buf.write("\u00d2\7\b\2\2\u00d2\u00d3\7\66\2\2\u00d3\u00d4\7\t\2")
        buf.write("\2\u00d4\u00d5\7\62\2\2\u00d5\u00d6\5N(\2\u00d6\u00d7")
        buf.write("\7\63\2\2\u00d7\u00d8\7.\2\2\u00d8\27\3\2\2\2\u00d9\u00da")
        buf.write("\7\b\2\2\u00da\u00db\7\66\2\2\u00db\u00dc\7\n\2\2\u00dc")
        buf.write("\u00dd\7\62\2\2\u00dd\u00de\5N(\2\u00de\u00df\7\63\2\2")
        buf.write("\u00df\u00e0\7.\2\2\u00e0\31\3\2\2\2\u00e1\u00ed\7\67")
        buf.write("\2\2\u00e2\u00ed\78\2\2\u00e3\u00ed\79\2\2\u00e4\u00ed")
        buf.write("\7:\2\2\u00e5\u00ed\7;\2\2\u00e6\u00ed\7<\2\2\u00e7\u00ed")
        buf.write("\7\25\2\2\u00e8\u00ed\7\26\2\2\u00e9\u00ed\7\24\2\2\u00ea")
        buf.write("\u00ed\5(\25\2\u00eb\u00ed\5\62\32\2\u00ec\u00e1\3\2\2")
        buf.write("\2\u00ec\u00e2\3\2\2\2\u00ec\u00e3\3\2\2\2\u00ec\u00e4")
        buf.write("\3\2\2\2\u00ec\u00e5\3\2\2\2\u00ec\u00e6\3\2\2\2\u00ec")
        buf.write("\u00e7\3\2\2\2\u00ec\u00e8\3\2\2\2\u00ec\u00e9\3\2\2\2")
        buf.write("\u00ec\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed\33\3\2")
        buf.write("\2\2\u00ee\u00fa\7\67\2\2\u00ef\u00fa\78\2\2\u00f0\u00fa")
        buf.write("\79\2\2\u00f1\u00fa\7:\2\2\u00f2\u00fa\7;\2\2\u00f3\u00fa")
        buf.write("\7<\2\2\u00f4\u00fa\7\25\2\2\u00f5\u00fa\7\26\2\2\u00f6")
        buf.write("\u00fa\7\24\2\2\u00f7\u00fa\7\66\2\2\u00f8\u00fa\5\62")
        buf.write("\32\2\u00f9\u00ee\3\2\2\2\u00f9\u00ef\3\2\2\2\u00f9\u00f0")
        buf.write("\3\2\2\2\u00f9\u00f1\3\2\2\2\u00f9\u00f2\3\2\2\2\u00f9")
        buf.write("\u00f3\3\2\2\2\u00f9\u00f4\3\2\2\2\u00f9\u00f5\3\2\2\2")
        buf.write("\u00f9\u00f6\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00f8\3")
        buf.write("\2\2\2\u00fa\35\3\2\2\2\u00fb\u0102\7\f\2\2\u00fc\u0102")
        buf.write("\7\r\2\2\u00fd\u0102\7\16\2\2\u00fe\u0102\7\13\2\2\u00ff")
        buf.write("\u0102\5\"\22\2\u0100\u0102\7\66\2\2\u0101\u00fb\3\2\2")
        buf.write("\2\u0101\u00fc\3\2\2\2\u0101\u00fd\3\2\2\2\u0101\u00fe")
        buf.write("\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0100\3\2\2\2\u0102")
        buf.write("\37\3\2\2\2\u0103\u0104\t\2\2\2\u0104!\3\2\2\2\u0105\u0106")
        buf.write("\5$\23\2\u0106\u0107\5 \21\2\u0107#\3\2\2\2\u0108\u0109")
        buf.write("\5&\24\2\u0109\u010a\5$\23\2\u010a\u010d\3\2\2\2\u010b")
        buf.write("\u010d\5&\24\2\u010c\u0108\3\2\2\2\u010c\u010b\3\2\2\2")
        buf.write("\u010d%\3\2\2\2\u010e\u010f\7\64\2\2\u010f\u0110\t\3\2")
        buf.write("\2\u0110\u0111\7\65\2\2\u0111\'\3\2\2\2\u0112\u0113\5")
        buf.write("*\26\2\u0113\u0114\5\36\20\2\u0114\u0115\7\62\2\2\u0115")
        buf.write("\u0116\5.\30\2\u0116\u0117\7\63\2\2\u0117)\3\2\2\2\u0118")
        buf.write("\u0119\5,\27\2\u0119\u011a\5*\26\2\u011a\u011d\3\2\2\2")
        buf.write("\u011b\u011d\5,\27\2\u011c\u0118\3\2\2\2\u011c\u011b\3")
        buf.write("\2\2\2\u011d+\3\2\2\2\u011e\u011f\7\64\2\2\u011f\u0120")
        buf.write("\t\3\2\2\u0120\u0121\7\65\2\2\u0121-\3\2\2\2\u0122\u0123")
        buf.write("\5\60\31\2\u0123\u0124\7-\2\2\u0124\u0125\5.\30\2\u0125")
        buf.write("\u0128\3\2\2\2\u0126\u0128\5\60\31\2\u0127\u0122\3\2\2")
        buf.write("\2\u0127\u0126\3\2\2\2\u0128/\3\2\2\2\u0129\u012f\5\34")
        buf.write("\17\2\u012a\u012b\7\62\2\2\u012b\u012c\5.\30\2\u012c\u012d")
        buf.write("\7\63\2\2\u012d\u012f\3\2\2\2\u012e\u0129\3\2\2\2\u012e")
        buf.write("\u012a\3\2\2\2\u012f\61\3\2\2\2\u0130\u0131\7\66\2\2\u0131")
        buf.write("\u0134\7\62\2\2\u0132\u0135\5\64\33\2\u0133\u0135\3\2")
        buf.write("\2\2\u0134\u0132\3\2\2\2\u0134\u0133\3\2\2\2\u0135\u0136")
        buf.write("\3\2\2\2\u0136\u0137\7\63\2\2\u0137\63\3\2\2\2\u0138\u0139")
        buf.write("\5\66\34\2\u0139\u013a\7-\2\2\u013a\u013b\5\64\33\2\u013b")
        buf.write("\u013e\3\2\2\2\u013c\u013e\5\66\34\2\u013d\u0138\3\2\2")
        buf.write("\2\u013d\u013c\3\2\2\2\u013e\65\3\2\2\2\u013f\u0140\7")
        buf.write("\66\2\2\u0140\u0141\7,\2\2\u0141\u0142\5:\36\2\u0142\67")
        buf.write("\3\2\2\2\u0143\u0144\5:\36\2\u0144\u0145\7-\2\2\u0145")
        buf.write("\u0146\58\35\2\u0146\u0149\3\2\2\2\u0147\u0149\5:\36\2")
        buf.write("\u0148\u0143\3\2\2\2\u0148\u0147\3\2\2\2\u01499\3\2\2")
        buf.write("\2\u014a\u014b\b\36\1\2\u014b\u014c\5<\37\2\u014c\u0152")
        buf.write("\3\2\2\2\u014d\u014e\f\4\2\2\u014e\u014f\7#\2\2\u014f")
        buf.write("\u0151\5<\37\2\u0150\u014d\3\2\2\2\u0151\u0154\3\2\2\2")
        buf.write("\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153;\3\2\2")
        buf.write("\2\u0154\u0152\3\2\2\2\u0155\u0156\b\37\1\2\u0156\u0157")
        buf.write("\5> \2\u0157\u015d\3\2\2\2\u0158\u0159\f\4\2\2\u0159\u015a")
        buf.write("\7\"\2\2\u015a\u015c\5> \2\u015b\u0158\3\2\2\2\u015c\u015f")
        buf.write("\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e")
        buf.write("=\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u0161\b \1\2\u0161")
        buf.write("\u0162\5@!\2\u0162\u0168\3\2\2\2\u0163\u0164\f\4\2\2\u0164")
        buf.write("\u0165\t\4\2\2\u0165\u0167\5@!\2\u0166\u0163\3\2\2\2\u0167")
        buf.write("\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2")
        buf.write("\u0169?\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u016c\b!\1\2")
        buf.write("\u016c\u016d\5B\"\2\u016d\u0173\3\2\2\2\u016e\u016f\f")
        buf.write("\4\2\2\u016f\u0170\t\5\2\2\u0170\u0172\5B\"\2\u0171\u016e")
        buf.write("\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2\u0173")
        buf.write("\u0174\3\2\2\2\u0174A\3\2\2\2\u0175\u0173\3\2\2\2\u0176")
        buf.write("\u0177\b\"\1\2\u0177\u0178\5D#\2\u0178\u017e\3\2\2\2\u0179")
        buf.write("\u017a\f\4\2\2\u017a\u017b\t\6\2\2\u017b\u017d\5D#\2\u017c")
        buf.write("\u0179\3\2\2\2\u017d\u0180\3\2\2\2\u017e\u017c\3\2\2\2")
        buf.write("\u017e\u017f\3\2\2\2\u017fC\3\2\2\2\u0180\u017e\3\2\2")
        buf.write("\2\u0181\u0182\t\7\2\2\u0182\u0185\5D#\2\u0183\u0185\5")
        buf.write("F$\2\u0184\u0181\3\2\2\2\u0184\u0183\3\2\2\2\u0185E\3")
        buf.write("\2\2\2\u0186\u0187\b$\1\2\u0187\u0188\5H%\2\u0188\u019a")
        buf.write("\3\2\2\2\u0189\u018a\f\6\2\2\u018a\u018b\7\64\2\2\u018b")
        buf.write("\u018c\5:\36\2\u018c\u018d\7\65\2\2\u018d\u0199\3\2\2")
        buf.write("\2\u018e\u018f\f\5\2\2\u018f\u0190\7+\2\2\u0190\u0199")
        buf.write("\7\66\2\2\u0191\u0192\f\4\2\2\u0192\u0193\7+\2\2\u0193")
        buf.write("\u0194\7\66\2\2\u0194\u0195\7\60\2\2\u0195\u0196\5J&\2")
        buf.write("\u0196\u0197\7\61\2\2\u0197\u0199\3\2\2\2\u0198\u0189")
        buf.write("\3\2\2\2\u0198\u018e\3\2\2\2\u0198\u0191\3\2\2\2\u0199")
        buf.write("\u019c\3\2\2\2\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2")
        buf.write("\u019bG\3\2\2\2\u019c\u019a\3\2\2\2\u019d\u01a9\5\32\16")
        buf.write("\2\u019e\u019f\7\60\2\2\u019f\u01a0\5:\36\2\u01a0\u01a1")
        buf.write("\7\61\2\2\u01a1\u01a9\3\2\2\2\u01a2\u01a9\7\66\2\2\u01a3")
        buf.write("\u01a4\7\66\2\2\u01a4\u01a5\7\60\2\2\u01a5\u01a6\5J&\2")
        buf.write("\u01a6\u01a7\7\61\2\2\u01a7\u01a9\3\2\2\2\u01a8\u019d")
        buf.write("\3\2\2\2\u01a8\u019e\3\2\2\2\u01a8\u01a2\3\2\2\2\u01a8")
        buf.write("\u01a3\3\2\2\2\u01a9I\3\2\2\2\u01aa\u01ad\5L\'\2\u01ab")
        buf.write("\u01ad\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ab\3\2\2\2")
        buf.write("\u01adK\3\2\2\2\u01ae\u01b4\5:\36\2\u01af\u01b0\5:\36")
        buf.write("\2\u01b0\u01b1\7-\2\2\u01b1\u01b2\5L\'\2\u01b2\u01b4\3")
        buf.write("\2\2\2\u01b3\u01ae\3\2\2\2\u01b3\u01af\3\2\2\2\u01b4M")
        buf.write("\3\2\2\2\u01b5\u01b6\5P)\2\u01b6\u01b7\5N(\2\u01b7\u01ba")
        buf.write("\3\2\2\2\u01b8\u01ba\5P)\2\u01b9\u01b5\3\2\2\2\u01b9\u01b8")
        buf.write("\3\2\2\2\u01baO\3\2\2\2\u01bb\u01c6\5T+\2\u01bc\u01c6")
        buf.write("\5^\60\2\u01bd\u01c6\5h\65\2\u01be\u01c6\5j\66\2\u01bf")
        buf.write("\u01c6\5l\67\2\u01c0\u01c6\5n8\2\u01c1\u01c6\5p9\2\u01c2")
        buf.write("\u01c6\5r:\2\u01c3\u01c6\5x=\2\u01c4\u01c6\5R*\2\u01c5")
        buf.write("\u01bb\3\2\2\2\u01c5\u01bc\3\2\2\2\u01c5\u01bd\3\2\2\2")
        buf.write("\u01c5\u01be\3\2\2\2\u01c5\u01bf\3\2\2\2\u01c5\u01c0\3")
        buf.write("\2\2\2\u01c5\u01c1\3\2\2\2\u01c5\u01c2\3\2\2\2\u01c5\u01c3")
        buf.write("\3\2\2\2\u01c5\u01c4\3\2\2\2\u01c6Q\3\2\2\2\u01c7\u01c8")
        buf.write("\5\6\4\2\u01c8S\3\2\2\2\u01c9\u01ca\5X-\2\u01ca\u01cb")
        buf.write("\5V,\2\u01cb\u01cc\5:\36\2\u01cc\u01cd\7.\2\2\u01cdU\3")
        buf.write("\2\2\2\u01ce\u01cf\t\b\2\2\u01cfW\3\2\2\2\u01d0\u01d1")
        buf.write("\b-\1\2\u01d1\u01d2\7\66\2\2\u01d2\u01de\3\2\2\2\u01d3")
        buf.write("\u01da\f\4\2\2\u01d4\u01d5\7\64\2\2\u01d5\u01d6\5:\36")
        buf.write("\2\u01d6\u01d7\7\65\2\2\u01d7\u01db\3\2\2\2\u01d8\u01d9")
        buf.write("\7+\2\2\u01d9\u01db\7\66\2\2\u01da\u01d4\3\2\2\2\u01da")
        buf.write("\u01d8\3\2\2\2\u01db\u01dd\3\2\2\2\u01dc\u01d3\3\2\2\2")
        buf.write("\u01dd\u01e0\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01df\3")
        buf.write("\2\2\2\u01dfY\3\2\2\2\u01e0\u01de\3\2\2\2\u01e1\u01e2")
        buf.write("\7\4\2\2\u01e2\u01e4\7\62\2\2\u01e3\u01e5\5N(\2\u01e4")
        buf.write("\u01e3\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e6\3\2\2\2")
        buf.write("\u01e6\u01e7\7\63\2\2\u01e7[\3\2\2\2\u01e8\u01e9\7\4\2")
        buf.write("\2\u01e9\u01ea\7\3\2\2\u01ea\u01eb\7\60\2\2\u01eb\u01ec")
        buf.write("\5:\36\2\u01ec\u01ed\7\61\2\2\u01ed\u01ef\7\62\2\2\u01ee")
        buf.write("\u01f0\5N(\2\u01ef\u01ee\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0")
        buf.write("\u01f1\3\2\2\2\u01f1\u01f3\7\63\2\2\u01f2\u01f4\5\\/\2")
        buf.write("\u01f3\u01f2\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4]\3\2\2")
        buf.write("\2\u01f5\u01f6\7\3\2\2\u01f6\u01f7\7\60\2\2\u01f7\u01f8")
        buf.write("\5:\36\2\u01f8\u01f9\7\61\2\2\u01f9\u01fb\7\62\2\2\u01fa")
        buf.write("\u01fc\5N(\2\u01fb\u01fa\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc")
        buf.write("\u01fd\3\2\2\2\u01fd\u01ff\7\63\2\2\u01fe\u0200\5\\/\2")
        buf.write("\u01ff\u01fe\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0202\3")
        buf.write("\2\2\2\u0201\u0203\5Z.\2\u0202\u0201\3\2\2\2\u0202\u0203")
        buf.write("\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0205\7.\2\2\u0205")
        buf.write("_\3\2\2\2\u0206\u0207\7\20\2\2\u0207\u0209\7\66\2\2\u0208")
        buf.write("\u020a\5\36\20\2\u0209\u0208\3\2\2\2\u0209\u020a\3\2\2")
        buf.write("\2\u020a\u020b\3\2\2\2\u020b\u020c\7%\2\2\u020c\u020d")
        buf.write("\5:\36\2\u020d\u020e\7.\2\2\u020ea\3\2\2\2\u020f\u0210")
        buf.write("\7\66\2\2\u0210\u0211\7-\2\2\u0211\u0212\7\66\2\2\u0212")
        buf.write("\u0213\7/\2\2\u0213\u0214\7\23\2\2\u0214\u0215\5:\36\2")
        buf.write("\u0215c\3\2\2\2\u0216\u0217\7\66\2\2\u0217\u0218\5V,\2")
        buf.write("\u0218\u0219\5:\36\2\u0219\u021a\7.\2\2\u021a\u021d\3")
        buf.write("\2\2\2\u021b\u021d\5`\61\2\u021c\u0216\3\2\2\2\u021c\u021b")
        buf.write("\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u021f\5:\36\2\u021f")
        buf.write("\u0220\7.\2\2\u0220\u0221\7\66\2\2\u0221\u0222\5V,\2\u0222")
        buf.write("\u0223\5:\36\2\u0223e\3\2\2\2\u0224\u0225\5:\36\2\u0225")
        buf.write("g\3\2\2\2\u0226\u022a\7\5\2\2\u0227\u022b\5f\64\2\u0228")
        buf.write("\u022b\5d\63\2\u0229\u022b\5b\62\2\u022a\u0227\3\2\2\2")
        buf.write("\u022a\u0228\3\2\2\2\u022a\u0229\3\2\2\2\u022b\u022c\3")
        buf.write("\2\2\2\u022c\u022e\7\62\2\2\u022d\u022f\5N(\2\u022e\u022d")
        buf.write("\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u0230\3\2\2\2\u0230")
        buf.write("\u0231\7\63\2\2\u0231\u0232\7.\2\2\u0232i\3\2\2\2\u0233")
        buf.write("\u0234\7\22\2\2\u0234\u0235\7.\2\2\u0235k\3\2\2\2\u0236")
        buf.write("\u0237\7\21\2\2\u0237\u0238\7.\2\2\u0238m\3\2\2\2\u0239")
        buf.write("\u023a\5X-\2\u023a\u023b\7+\2\2\u023b\u023e\3\2\2\2\u023c")
        buf.write("\u023e\3\2\2\2\u023d\u0239\3\2\2\2\u023d\u023c\3\2\2\2")
        buf.write("\u023e\u023f\3\2\2\2\u023f\u0240\7\66\2\2\u0240\u0243")
        buf.write("\7\60\2\2\u0241\u0244\58\35\2\u0242\u0244\3\2\2\2\u0243")
        buf.write("\u0241\3\2\2\2\u0243\u0242\3\2\2\2\u0244\u0245\3\2\2\2")
        buf.write("\u0245\u0246\7\61\2\2\u0246\u0247\7.\2\2\u0247o\3\2\2")
        buf.write("\2\u0248\u024b\7\6\2\2\u0249\u024c\5:\36\2\u024a\u024c")
        buf.write("\3\2\2\2\u024b\u0249\3\2\2\2\u024b\u024a\3\2\2\2\u024c")
        buf.write("\u024d\3\2\2\2\u024d\u024e\7.\2\2\u024eq\3\2\2\2\u024f")
        buf.write("\u0250\7\66\2\2\u0250\u0251\5\36\20\2\u0251\u0252\7.\2")
        buf.write("\2\u0252s\3\2\2\2\u0253\u0254\5\22\n\2\u0254\u0255\5\36")
        buf.write("\20\2\u0255u\3\2\2\2\u0256\u0257\5t;\2\u0257\u0258\7-")
        buf.write("\2\2\u0258\u0259\5v<\2\u0259\u025c\3\2\2\2\u025a\u025c")
        buf.write("\5t;\2\u025b\u0256\3\2\2\2\u025b\u025a\3\2\2\2\u025cw")
        buf.write("\3\2\2\2\u025d\u025e\7\66\2\2\u025e\u0261\7\60\2\2\u025f")
        buf.write("\u0262\5v<\2\u0260\u0262\3\2\2\2\u0261\u025f\3\2\2\2\u0261")
        buf.write("\u0260\3\2\2\2\u0262\u0263\3\2\2\2\u0263\u0266\7\61\2")
        buf.write("\2\u0264\u0267\5\36\20\2\u0265\u0267\3\2\2\2\u0266\u0264")
        buf.write("\3\2\2\2\u0266\u0265\3\2\2\2\u0267\u0268\3\2\2\2\u0268")
        buf.write("\u0269\7.\2\2\u0269y\3\2\2\2\66\u0081\u0089\u0095\u0099")
        buf.write("\u00a1\u00a5\u00a9\u00b3\u00bc\u00c6\u00ca\u00ec\u00f9")
        buf.write("\u0101\u010c\u011c\u0127\u012e\u0134\u013d\u0148\u0152")
        buf.write("\u015d\u0168\u0173\u017e\u0184\u0198\u019a\u01a8\u01ac")
        buf.write("\u01b3\u01b9\u01c5\u01da\u01de\u01e4\u01ef\u01f3\u01fb")
        buf.write("\u01ff\u0202\u0209\u021c\u022a\u022e\u023d\u0243\u024b")
        buf.write("\u025b\u0261\u0266")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'.'", "':'", "','", "';'", "':='", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQUAL", "NEQUAL", "LT", "LTE", "GT", "GTE", 
                      "AND", "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                      "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "COLON", 
                      "COMMA", "COCOM", "COLONEQUAL", "LPAREN", "RPAREN", 
                      "LCPAREN", "RCPAREN", "LSPAREN", "RSPAREN", "ID", 
                      "INT_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", "FLOAT_LIT", 
                      "STRING_LIT", "BOOL_LIT", "NIL_LIT", "NEWLINE", "WS", 
                      "COMMENT_LINE", "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_list_declared = 1
    RULE_declared = 2
    RULE_const_declared = 3
    RULE_var_declared = 4
    RULE_func_declared = 5
    RULE_parameter_lit = 6
    RULE_parameter = 7
    RULE_list_ID = 8
    RULE_method_declared = 9
    RULE_struct_declared = 10
    RULE_interface_declared = 11
    RULE_literal = 12
    RULE_sec_lit = 13
    RULE_all_type = 14
    RULE_basic_type = 15
    RULE_list_array_type_lit = 16
    RULE_array_type_lit = 17
    RULE_array_type = 18
    RULE_array_literal = 19
    RULE_dim_lit = 20
    RULE_dim = 21
    RULE_list_array_element = 22
    RULE_array_element = 23
    RULE_struct_literal = 24
    RULE_list_elements_lit = 25
    RULE_list_element = 26
    RULE_list_expression = 27
    RULE_expression = 28
    RULE_expression1 = 29
    RULE_expression2 = 30
    RULE_expression3 = 31
    RULE_expression4 = 32
    RULE_expression5 = 33
    RULE_expression6 = 34
    RULE_expression7 = 35
    RULE_funcall = 36
    RULE_funcall_noempty = 37
    RULE_list_statement = 38
    RULE_statement = 39
    RULE_declared_statement = 40
    RULE_assign_statement = 41
    RULE_operators = 42
    RULE_assignment_lhs = 43
    RULE_else_statement = 44
    RULE_elif_statement = 45
    RULE_if_statement = 46
    RULE_var_declared_for = 47
    RULE_range_loop = 48
    RULE_init_loop = 49
    RULE_basic_loop = 50
    RULE_for_statement = 51
    RULE_break_statement = 52
    RULE_continue_statement = 53
    RULE_call_statement = 54
    RULE_return_statement = 55
    RULE_struct_statement = 56
    RULE_method_parameter = 57
    RULE_method_parameter_lit = 58
    RULE_method_statement = 59

    ruleNames =  [ "program", "list_declared", "declared", "const_declared", 
                   "var_declared", "func_declared", "parameter_lit", "parameter", 
                   "list_ID", "method_declared", "struct_declared", "interface_declared", 
                   "literal", "sec_lit", "all_type", "basic_type", "list_array_type_lit", 
                   "array_type_lit", "array_type", "array_literal", "dim_lit", 
                   "dim", "list_array_element", "array_element", "struct_literal", 
                   "list_elements_lit", "list_element", "list_expression", 
                   "expression", "expression1", "expression2", "expression3", 
                   "expression4", "expression5", "expression6", "expression7", 
                   "funcall", "funcall_noempty", "list_statement", "statement", 
                   "declared_statement", "assign_statement", "operators", 
                   "assignment_lhs", "else_statement", "elif_statement", 
                   "if_statement", "var_declared_for", "range_loop", "init_loop", 
                   "basic_loop", "for_statement", "break_statement", "continue_statement", 
                   "call_statement", "return_statement", "struct_statement", 
                   "method_parameter", "method_parameter_lit", "method_statement" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    EQUAL=26
    NEQUAL=27
    LT=28
    LTE=29
    GT=30
    GTE=31
    AND=32
    OR=33
    NOT=34
    ASSIGN=35
    ADD_ASSIGN=36
    SUB_ASSIGN=37
    MUL_ASSIGN=38
    DIV_ASSIGN=39
    MOD_ASSIGN=40
    DOT=41
    COLON=42
    COMMA=43
    COCOM=44
    COLONEQUAL=45
    LPAREN=46
    RPAREN=47
    LCPAREN=48
    RCPAREN=49
    LSPAREN=50
    RSPAREN=51
    ID=52
    INT_LIT=53
    BIN_LIT=54
    OCT_LIT=55
    HEX_LIT=56
    FLOAT_LIT=57
    STRING_LIT=58
    BOOL_LIT=59
    NIL_LIT=60
    NEWLINE=61
    WS=62
    COMMENT_LINE=63
    COMMENT=64
    ERROR_CHAR=65
    UNCLOSE_STRING=66
    ILLEGAL_ESCAPE=67

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_declared(self):
            return self.getTypedRuleContext(MiniGoParser.List_declaredContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.list_declared()
            self.state = 121
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared(self):
            return self.getTypedRuleContext(MiniGoParser.DeclaredContext,0)


        def list_declared(self):
            return self.getTypedRuleContext(MiniGoParser.List_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_declared" ):
                return visitor.visitList_declared(self)
            else:
                return visitor.visitChildren(self)




    def list_declared(self):

        localctx = MiniGoParser.List_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_declared)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.declared()
                self.state = 124
                self.list_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declaredContext,0)


        def const_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declaredContext,0)


        def func_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declaredContext,0)


        def method_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declaredContext,0)


        def struct_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declaredContext,0)


        def interface_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = MiniGoParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declared)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.var_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.const_declared()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.func_declared()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 132
                self.method_declared()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 133
                self.struct_declared()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 134
                self.interface_declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_const_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_declared" ):
                return visitor.visitConst_declared(self)
            else:
                return visitor.visitChildren(self)




    def const_declared(self):

        localctx = MiniGoParser.Const_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_const_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(MiniGoParser.CONST)
            self.state = 138
            self.match(MiniGoParser.ID)
            self.state = 139
            self.match(MiniGoParser.ASSIGN)
            self.state = 140
            self.expression(0)
            self.state = 141
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declared" ):
                return visitor.visitVar_declared(self)
            else:
                return visitor.visitChildren(self)




    def var_declared(self):

        localctx = MiniGoParser.Var_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(MiniGoParser.VAR)
            self.state = 144
            self.match(MiniGoParser.ID)
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 145
                self.all_type()
                pass

            elif la_ == 2:
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSPAREN) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 146
                    self.all_type()


                self.state = 149
                self.match(MiniGoParser.ASSIGN)
                self.state = 150
                self.expression(0)
                pass


            self.state = 153
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def parameter_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_litContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declared" ):
                return visitor.visitFunc_declared(self)
            else:
                return visitor.visitChildren(self)




    def func_declared(self):

        localctx = MiniGoParser.Func_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(MiniGoParser.FUNC)
            self.state = 156
            self.match(MiniGoParser.ID)
            self.state = 157
            self.match(MiniGoParser.LPAREN)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 158
                self.parameter_lit()


            self.state = 161
            self.match(MiniGoParser.RPAREN)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSPAREN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 162
                self.all_type()


            self.state = 165
            self.match(MiniGoParser.LCPAREN)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 166
                self.list_statement()


            self.state = 169
            self.match(MiniGoParser.RCPAREN)
            self.state = 170
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def parameter_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameter_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_lit" ):
                return visitor.visitParameter_lit(self)
            else:
                return visitor.visitChildren(self)




    def parameter_lit(self):

        localctx = MiniGoParser.Parameter_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parameter_lit)
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.parameter()
                self.state = 173
                self.match(MiniGoParser.COMMA)
                self.state = 174
                self.parameter_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_ID(self):
            return self.getTypedRuleContext(MiniGoParser.List_IDContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = MiniGoParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.list_ID()
            self.state = 180
            self.all_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_IDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_ID(self):
            return self.getTypedRuleContext(MiniGoParser.List_IDContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_ID

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_ID" ):
                return visitor.visitList_ID(self)
            else:
                return visitor.visitChildren(self)




    def list_ID(self):

        localctx = MiniGoParser.List_IDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list_ID)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(MiniGoParser.ID)
                self.state = 183
                self.match(MiniGoParser.COMMA)
                self.state = 184
                self.list_ID()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def parameter_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Parameter_litContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declared" ):
                return visitor.visitMethod_declared(self)
            else:
                return visitor.visitChildren(self)




    def method_declared(self):

        localctx = MiniGoParser.Method_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_method_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(MiniGoParser.FUNC)
            self.state = 189
            self.match(MiniGoParser.LPAREN)
            self.state = 190
            self.match(MiniGoParser.ID)
            self.state = 191
            self.match(MiniGoParser.ID)
            self.state = 192
            self.match(MiniGoParser.RPAREN)
            self.state = 193
            self.match(MiniGoParser.ID)
            self.state = 194
            self.match(MiniGoParser.LPAREN)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 195
                self.parameter_lit()


            self.state = 198
            self.match(MiniGoParser.RPAREN)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSPAREN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 199
                self.all_type()


            self.state = 202
            self.match(MiniGoParser.LCPAREN)
            self.state = 203
            self.list_statement()
            self.state = 204
            self.match(MiniGoParser.RCPAREN)
            self.state = 205
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_declared" ):
                return visitor.visitStruct_declared(self)
            else:
                return visitor.visitChildren(self)




    def struct_declared(self):

        localctx = MiniGoParser.Struct_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_struct_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(MiniGoParser.TYPE)
            self.state = 208
            self.match(MiniGoParser.ID)
            self.state = 209
            self.match(MiniGoParser.STRUCT)
            self.state = 210
            self.match(MiniGoParser.LCPAREN)
            self.state = 211
            self.list_statement()
            self.state = 212
            self.match(MiniGoParser.RCPAREN)
            self.state = 213
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declared" ):
                return visitor.visitInterface_declared(self)
            else:
                return visitor.visitChildren(self)




    def interface_declared(self):

        localctx = MiniGoParser.Interface_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_interface_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(MiniGoParser.TYPE)
            self.state = 216
            self.match(MiniGoParser.ID)
            self.state = 217
            self.match(MiniGoParser.INTERFACE)
            self.state = 218
            self.match(MiniGoParser.LCPAREN)
            self.state = 219
            self.list_statement()
            self.state = 220
            self.match(MiniGoParser.RCPAREN)
            self.state = 221
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def BIN_LIT(self):
            return self.getToken(MiniGoParser.BIN_LIT, 0)

        def OCT_LIT(self):
            return self.getToken(MiniGoParser.OCT_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(MiniGoParser.HEX_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_literal)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.BIN_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.match(MiniGoParser.BIN_LIT)
                pass
            elif token in [MiniGoParser.OCT_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
                self.match(MiniGoParser.OCT_LIT)
                pass
            elif token in [MiniGoParser.HEX_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 226
                self.match(MiniGoParser.HEX_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 227
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 228
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 229
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 230
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 9)
                self.state = 231
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.LSPAREN]:
                self.enterOuterAlt(localctx, 10)
                self.state = 232
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 11)
                self.state = 233
                self.struct_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sec_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def BIN_LIT(self):
            return self.getToken(MiniGoParser.BIN_LIT, 0)

        def OCT_LIT(self):
            return self.getToken(MiniGoParser.OCT_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(MiniGoParser.HEX_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_sec_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSec_lit" ):
                return visitor.visitSec_lit(self)
            else:
                return visitor.visitChildren(self)




    def sec_lit(self):

        localctx = MiniGoParser.Sec_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_sec_lit)
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.match(MiniGoParser.BIN_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 238
                self.match(MiniGoParser.OCT_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 239
                self.match(MiniGoParser.HEX_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 240
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 241
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 242
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 243
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 244
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 245
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 246
                self.struct_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def list_array_type_lit(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_type_litContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_all_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_type" ):
                return visitor.visitAll_type(self)
            else:
                return visitor.visitChildren(self)




    def all_type(self):

        localctx = MiniGoParser.All_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_all_type)
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 252
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.LSPAREN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 253
                self.list_array_type_lit()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 254
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_type" ):
                return visitor.visitBasic_type(self)
            else:
                return visitor.visitChildren(self)




    def basic_type(self):

        localctx = MiniGoParser.Basic_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_basic_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_array_type_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Array_type_litContext,0)


        def basic_type(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_array_type_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_array_type_lit" ):
                return visitor.visitList_array_type_lit(self)
            else:
                return visitor.visitChildren(self)




    def list_array_type_lit(self):

        localctx = MiniGoParser.List_array_type_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list_array_type_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.array_type_lit()
            self.state = 260
            self.basic_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_type_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def array_type_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Array_type_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type_lit" ):
                return visitor.visitArray_type_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_type_lit(self):

        localctx = MiniGoParser.Array_type_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_array_type_lit)
        try:
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.array_type()
                self.state = 263
                self.array_type_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.array_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSPAREN(self):
            return self.getToken(MiniGoParser.LSPAREN, 0)

        def RSPAREN(self):
            return self.getToken(MiniGoParser.RSPAREN, 0)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(MiniGoParser.LSPAREN)
            self.state = 269
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 270
            self.match(MiniGoParser.RSPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dim_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Dim_litContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def list_array_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_elementContext,0)


        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.dim_lit()
            self.state = 273
            self.all_type()
            self.state = 274
            self.match(MiniGoParser.LCPAREN)
            self.state = 275
            self.list_array_element()
            self.state = 276
            self.match(MiniGoParser.RCPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dim_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dim(self):
            return self.getTypedRuleContext(MiniGoParser.DimContext,0)


        def dim_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Dim_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_dim_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDim_lit" ):
                return visitor.visitDim_lit(self)
            else:
                return visitor.visitChildren(self)




    def dim_lit(self):

        localctx = MiniGoParser.Dim_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_dim_lit)
        try:
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.dim()
                self.state = 279
                self.dim_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.dim()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSPAREN(self):
            return self.getToken(MiniGoParser.LSPAREN, 0)

        def RSPAREN(self):
            return self.getToken(MiniGoParser.RSPAREN, 0)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dim

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDim" ):
                return visitor.visitDim(self)
            else:
                return visitor.visitChildren(self)




    def dim(self):

        localctx = MiniGoParser.DimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_dim)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(MiniGoParser.LSPAREN)
            self.state = 285
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 286
            self.match(MiniGoParser.RSPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_array_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_array_element" ):
                return visitor.visitList_array_element(self)
            else:
                return visitor.visitChildren(self)




    def list_array_element(self):

        localctx = MiniGoParser.List_array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_list_array_element)
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.array_element()
                self.state = 289
                self.match(MiniGoParser.COMMA)
                self.state = 290
                self.list_array_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                self.array_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sec_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Sec_litContext,0)


        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def list_array_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_elementContext,0)


        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




    def array_element(self):

        localctx = MiniGoParser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_array_element)
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.sec_lit()
                pass
            elif token in [MiniGoParser.LCPAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.match(MiniGoParser.LCPAREN)
                self.state = 297
                self.list_array_element()
                self.state = 298
                self.match(MiniGoParser.RCPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def list_elements_lit(self):
            return self.getTypedRuleContext(MiniGoParser.List_elements_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(MiniGoParser.ID)
            self.state = 303
            self.match(MiniGoParser.LCPAREN)
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 304
                self.list_elements_lit()
                pass
            elif token in [MiniGoParser.RCPAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 308
            self.match(MiniGoParser.RCPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elements_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_elements_lit(self):
            return self.getTypedRuleContext(MiniGoParser.List_elements_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_elements_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_elements_lit" ):
                return visitor.visitList_elements_lit(self)
            else:
                return visitor.visitChildren(self)




    def list_elements_lit(self):

        localctx = MiniGoParser.List_elements_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_list_elements_lit)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.list_element()
                self.state = 311
                self.match(MiniGoParser.COMMA)
                self.state = 312
                self.list_elements_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.list_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_element" ):
                return visitor.visitList_element(self)
            else:
                return visitor.visitChildren(self)




    def list_element(self):

        localctx = MiniGoParser.List_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_list_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(MiniGoParser.ID)
            self.state = 318
            self.match(MiniGoParser.COLON)
            self.state = 319
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = MiniGoParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_list_expression)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.expression(0)
                self.state = 322
                self.match(MiniGoParser.COMMA)
                self.state = 323
                self.list_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 336
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 331
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 332
                    self.match(MiniGoParser.OR)
                    self.state = 333
                    self.expression1(0) 
                self.state = 338
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 347
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 342
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 343
                    self.match(MiniGoParser.AND)
                    self.state = 344
                    self.expression2(0) 
                self.state = 349
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def NEQUAL(self):
            return self.getToken(MiniGoParser.NEQUAL, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LTE(self):
            return self.getToken(MiniGoParser.LTE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GTE(self):
            return self.getToken(MiniGoParser.GTE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 358
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 353
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 354
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NEQUAL) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LTE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GTE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 355
                    self.expression3(0) 
                self.state = 360
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 369
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 364
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 365
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 366
                    self.expression4(0) 
                self.state = 371
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 380
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 375
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 376
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 377
                    self.expression5() 
                self.state = 382
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = MiniGoParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expression5)
        self._la = 0 # Token type
        try:
            self.state = 386
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 384
                self.expression5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LSPAREN, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.expression6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def LSPAREN(self):
            return self.getToken(MiniGoParser.LSPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RSPAREN(self):
            return self.getToken(MiniGoParser.RSPAREN, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def funcall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncallContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)



    def expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expression6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 408
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 406
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 391
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 392
                        self.match(MiniGoParser.LSPAREN)
                        self.state = 393
                        self.expression(0)
                        self.state = 394
                        self.match(MiniGoParser.RSPAREN)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 396
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 397
                        self.match(MiniGoParser.DOT)
                        self.state = 398
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 399
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 400
                        self.match(MiniGoParser.DOT)
                        self.state = 401
                        self.match(MiniGoParser.ID)
                        self.state = 402
                        self.match(MiniGoParser.LPAREN)
                        self.state = 403
                        self.funcall()
                        self.state = 404
                        self.match(MiniGoParser.RPAREN)
                        pass

             
                self.state = 410
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def funcall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = MiniGoParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expression7)
        try:
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.match(MiniGoParser.LPAREN)
                self.state = 413
                self.expression(0)
                self.state = 414
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 416
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 417
                self.match(MiniGoParser.ID)
                self.state = 418
                self.match(MiniGoParser.LPAREN)
                self.state = 419
                self.funcall()
                self.state = 420
                self.match(MiniGoParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall_noempty(self):
            return self.getTypedRuleContext(MiniGoParser.Funcall_noemptyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = MiniGoParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_funcall)
        try:
            self.state = 426
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LSPAREN, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.funcall_noempty()
                pass
            elif token in [MiniGoParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcall_noemptyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def funcall_noempty(self):
            return self.getTypedRuleContext(MiniGoParser.Funcall_noemptyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcall_noempty

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall_noempty" ):
                return visitor.visitFuncall_noempty(self)
            else:
                return visitor.visitChildren(self)




    def funcall_noempty(self):

        localctx = MiniGoParser.Funcall_noemptyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_funcall_noempty)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.expression(0)
                self.state = 430
                self.match(MiniGoParser.COMMA)
                self.state = 431
                self.funcall_noempty()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_statement(self):

        localctx = MiniGoParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_list_statement)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.statement()
                self.state = 436
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def struct_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_statementContext,0)


        def method_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Method_statementContext,0)


        def declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Declared_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_statement)
        try:
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.assign_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 443
                self.for_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 444
                self.break_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 445
                self.continue_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 446
                self.call_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 447
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 448
                self.struct_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 449
                self.method_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 450
                self.declared_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared(self):
            return self.getTypedRuleContext(MiniGoParser.DeclaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared_statement" ):
                return visitor.visitDeclared_statement(self)
            else:
                return visitor.visitChildren(self)




    def declared_statement(self):

        localctx = MiniGoParser.Declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_declared_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.declared()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_lhsContext,0)


        def operators(self):
            return self.getTypedRuleContext(MiniGoParser.OperatorsContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = MiniGoParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.assignment_lhs(0)
            self.state = 456
            self.operators()
            self.state = 457
            self.expression(0)
            self.state = 458
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLONEQUAL(self):
            return self.getToken(MiniGoParser.COLONEQUAL, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperators" ):
                return visitor.visitOperators(self)
            else:
                return visitor.visitChildren(self)




    def operators(self):

        localctx = MiniGoParser.OperatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN) | (1 << MiniGoParser.COLONEQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assignment_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_lhsContext,0)


        def LSPAREN(self):
            return self.getToken(MiniGoParser.LSPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RSPAREN(self):
            return self.getToken(MiniGoParser.RSPAREN, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_lhs" ):
                return visitor.visitAssignment_lhs(self)
            else:
                return visitor.visitChildren(self)



    def assignment_lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Assignment_lhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_assignment_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 476
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Assignment_lhsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignment_lhs)
                    self.state = 465
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 472
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LSPAREN]:
                        self.state = 466
                        self.match(MiniGoParser.LSPAREN)
                        self.state = 467
                        self.expression(0)
                        self.state = 468
                        self.match(MiniGoParser.RSPAREN)
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 470
                        self.match(MiniGoParser.DOT)
                        self.state = 471
                        self.match(MiniGoParser.ID)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 478
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = MiniGoParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_else_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.match(MiniGoParser.ELSE)
            self.state = 480
            self.match(MiniGoParser.LCPAREN)
            self.state = 482
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 481
                self.list_statement()


            self.state = 484
            self.match(MiniGoParser.RCPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def elif_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Elif_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elif_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_statement" ):
                return visitor.visitElif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elif_statement(self):

        localctx = MiniGoParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_elif_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(MiniGoParser.ELSE)
            self.state = 487
            self.match(MiniGoParser.IF)
            self.state = 488
            self.match(MiniGoParser.LPAREN)
            self.state = 489
            self.expression(0)
            self.state = 490
            self.match(MiniGoParser.RPAREN)
            self.state = 491
            self.match(MiniGoParser.LCPAREN)
            self.state = 493
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 492
                self.list_statement()


            self.state = 495
            self.match(MiniGoParser.RCPAREN)
            self.state = 497
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 496
                self.elif_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def elif_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Elif_statementContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Else_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(MiniGoParser.IF)
            self.state = 500
            self.match(MiniGoParser.LPAREN)
            self.state = 501
            self.expression(0)
            self.state = 502
            self.match(MiniGoParser.RPAREN)
            self.state = 503
            self.match(MiniGoParser.LCPAREN)
            self.state = 505
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 504
                self.list_statement()


            self.state = 507
            self.match(MiniGoParser.RCPAREN)
            self.state = 509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 508
                self.elif_statement()


            self.state = 512
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 511
                self.else_statement()


            self.state = 514
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declared_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_declared_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declared_for" ):
                return visitor.visitVar_declared_for(self)
            else:
                return visitor.visitChildren(self)




    def var_declared_for(self):

        localctx = MiniGoParser.Var_declared_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_var_declared_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.match(MiniGoParser.VAR)
            self.state = 517
            self.match(MiniGoParser.ID)
            self.state = 519
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSPAREN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 518
                self.all_type()


            self.state = 521
            self.match(MiniGoParser.ASSIGN)
            self.state = 522
            self.expression(0)
            self.state = 523
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def COLONEQUAL(self):
            return self.getToken(MiniGoParser.COLONEQUAL, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_range_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_loop" ):
                return visitor.visitRange_loop(self)
            else:
                return visitor.visitChildren(self)




    def range_loop(self):

        localctx = MiniGoParser.Range_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_range_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self.match(MiniGoParser.ID)
            self.state = 526
            self.match(MiniGoParser.COMMA)
            self.state = 527
            self.match(MiniGoParser.ID)
            self.state = 528
            self.match(MiniGoParser.COLONEQUAL)
            self.state = 529
            self.match(MiniGoParser.RANGE)
            self.state = 530
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def COCOM(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COCOM)
            else:
                return self.getToken(MiniGoParser.COCOM, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def operators(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.OperatorsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.OperatorsContext,i)


        def var_declared_for(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declared_forContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_init_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_loop" ):
                return visitor.visitInit_loop(self)
            else:
                return visitor.visitChildren(self)




    def init_loop(self):

        localctx = MiniGoParser.Init_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_init_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 532
                self.match(MiniGoParser.ID)
                self.state = 533
                self.operators()
                self.state = 534
                self.expression(0)
                self.state = 535
                self.match(MiniGoParser.COCOM)
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 537
                self.var_declared_for()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 540
            self.expression(0)
            self.state = 541
            self.match(MiniGoParser.COCOM)
            self.state = 542
            self.match(MiniGoParser.ID)
            self.state = 543
            self.operators()
            self.state = 544
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_loop" ):
                return visitor.visitBasic_loop(self)
            else:
                return visitor.visitChildren(self)




    def basic_loop(self):

        localctx = MiniGoParser.Basic_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_basic_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def LCPAREN(self):
            return self.getToken(MiniGoParser.LCPAREN, 0)

        def RCPAREN(self):
            return self.getToken(MiniGoParser.RCPAREN, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def basic_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_loopContext,0)


        def init_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Init_loopContext,0)


        def range_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Range_loopContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
            self.match(MiniGoParser.FOR)
            self.state = 552
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 549
                self.basic_loop()
                pass

            elif la_ == 2:
                self.state = 550
                self.init_loop()
                pass

            elif la_ == 3:
                self.state = 551
                self.range_loop()
                pass


            self.state = 554
            self.match(MiniGoParser.LCPAREN)
            self.state = 556
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 555
                self.list_statement()


            self.state = 558
            self.match(MiniGoParser.RCPAREN)
            self.state = 559
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.match(MiniGoParser.BREAK)
            self.state = 562
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self.match(MiniGoParser.CONTINUE)
            self.state = 565
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def assignment_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_lhsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 567
                self.assignment_lhs(0)
                self.state = 568
                self.match(MiniGoParser.DOT)
                pass

            elif la_ == 2:
                pass


            self.state = 573
            self.match(MiniGoParser.ID)
            self.state = 574
            self.match(MiniGoParser.LPAREN)
            self.state = 577
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LSPAREN, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 575
                self.list_expression()
                pass
            elif token in [MiniGoParser.RPAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 579
            self.match(MiniGoParser.RPAREN)
            self.state = 580
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 582
            self.match(MiniGoParser.RETURN)
            self.state = 585
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LSPAREN, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 583
                self.expression(0)
                pass
            elif token in [MiniGoParser.COCOM]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 587
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_statement" ):
                return visitor.visitStruct_statement(self)
            else:
                return visitor.visitChildren(self)




    def struct_statement(self):

        localctx = MiniGoParser.Struct_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_struct_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            self.match(MiniGoParser.ID)
            self.state = 590
            self.all_type()
            self.state = 591
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_ID(self):
            return self.getTypedRuleContext(MiniGoParser.List_IDContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_parameter" ):
                return visitor.visitMethod_parameter(self)
            else:
                return visitor.visitChildren(self)




    def method_parameter(self):

        localctx = MiniGoParser.Method_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_method_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            self.list_ID()
            self.state = 594
            self.all_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_parameter_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_parameter(self):
            return self.getTypedRuleContext(MiniGoParser.Method_parameterContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def method_parameter_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Method_parameter_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_parameter_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_parameter_lit" ):
                return visitor.visitMethod_parameter_lit(self)
            else:
                return visitor.visitChildren(self)




    def method_parameter_lit(self):

        localctx = MiniGoParser.Method_parameter_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_method_parameter_lit)
        try:
            self.state = 601
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 596
                self.method_parameter()
                self.state = 597
                self.match(MiniGoParser.COMMA)
                self.state = 598
                self.method_parameter_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 600
                self.method_parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def COCOM(self):
            return self.getToken(MiniGoParser.COCOM, 0)

        def method_parameter_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Method_parameter_litContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_statement" ):
                return visitor.visitMethod_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_statement(self):

        localctx = MiniGoParser.Method_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_method_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 603
            self.match(MiniGoParser.ID)
            self.state = 604
            self.match(MiniGoParser.LPAREN)
            self.state = 607
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 605
                self.method_parameter_lit()
                pass
            elif token in [MiniGoParser.RPAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 609
            self.match(MiniGoParser.RPAREN)
            self.state = 612
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LSPAREN, MiniGoParser.ID]:
                self.state = 610
                self.all_type()
                pass
            elif token in [MiniGoParser.COCOM]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 614
            self.match(MiniGoParser.COCOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[28] = self.expression_sempred
        self._predicates[29] = self.expression1_sempred
        self._predicates[30] = self.expression2_sempred
        self._predicates[31] = self.expression3_sempred
        self._predicates[32] = self.expression4_sempred
        self._predicates[34] = self.expression6_sempred
        self._predicates[43] = self.assignment_lhs_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression6_sempred(self, localctx:Expression6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def assignment_lhs_sempred(self, localctx:Assignment_lhsContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




