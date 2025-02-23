# Generated from main/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_declared.
    def visitList_declared(self, ctx:MiniGoParser.List_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared.
    def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_declared.
    def visitConst_declared(self, ctx:MiniGoParser.Const_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_declared.
    def visitVar_declared(self, ctx:MiniGoParser.Var_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_declared.
    def visitFunc_declared(self, ctx:MiniGoParser.Func_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameter_lit.
    def visitParameter_lit(self, ctx:MiniGoParser.Parameter_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#parameter.
    def visitParameter(self, ctx:MiniGoParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_ID.
    def visitList_ID(self, ctx:MiniGoParser.List_IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_declared.
    def visitMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_declared.
    def visitStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_declared.
    def visitInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#sec_lit.
    def visitSec_lit(self, ctx:MiniGoParser.Sec_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#all_type.
    def visitAll_type(self, ctx:MiniGoParser.All_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basic_type.
    def visitBasic_type(self, ctx:MiniGoParser.Basic_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_array_type_lit.
    def visitList_array_type_lit(self, ctx:MiniGoParser.List_array_type_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type_lit.
    def visitArray_type_lit(self, ctx:MiniGoParser.Array_type_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dim_lit.
    def visitDim_lit(self, ctx:MiniGoParser.Dim_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dim.
    def visitDim(self, ctx:MiniGoParser.DimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_array_element.
    def visitList_array_element(self, ctx:MiniGoParser.List_array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_element.
    def visitArray_element(self, ctx:MiniGoParser.Array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_elements_lit.
    def visitList_elements_lit(self, ctx:MiniGoParser.List_elements_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_element.
    def visitList_element(self, ctx:MiniGoParser.List_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expression.
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression1.
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression2.
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression3.
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression4.
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression5.
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression6.
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression7.
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcall.
    def visitFuncall(self, ctx:MiniGoParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcall_noempty.
    def visitFuncall_noempty(self, ctx:MiniGoParser.Funcall_noemptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_statement.
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#operators.
    def visitOperators(self, ctx:MiniGoParser.OperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_lhs.
    def visitAssignment_lhs(self, ctx:MiniGoParser.Assignment_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_statement.
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elif_statement.
    def visitElif_statement(self, ctx:MiniGoParser.Elif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elif_statement_lit.
    def visitElif_statement_lit(self, ctx:MiniGoParser.Elif_statement_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_declared_for.
    def visitVar_declared_for(self, ctx:MiniGoParser.Var_declared_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#range_loop.
    def visitRange_loop(self, ctx:MiniGoParser.Range_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#init_loop.
    def visitInit_loop(self, ctx:MiniGoParser.Init_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basic_loop.
    def visitBasic_loop(self, ctx:MiniGoParser.Basic_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_statement.
    def visitStruct_statement(self, ctx:MiniGoParser.Struct_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_struct_statement.
    def visitList_struct_statement(self, ctx:MiniGoParser.List_struct_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_parameter.
    def visitMethod_parameter(self, ctx:MiniGoParser.Method_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_parameter_lit.
    def visitMethod_parameter_lit(self, ctx:MiniGoParser.Method_parameter_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_statement.
    def visitMethod_statement(self, ctx:MiniGoParser.Method_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_method_statement.
    def visitList_method_statement(self, ctx:MiniGoParser.List_method_statementContext):
        return self.visitChildren(ctx)



del MiniGoParser