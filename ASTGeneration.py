"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""
from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce

##! continue update
class ASTGeneration(MiniGoVisitor):
    #program: list_declared EOF;
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.list_declared()))


    #list_declared: declared list_declared | declared;
    def visitList_declared(self, ctx:MiniGoParser.List_declaredContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.declared())]
        else:
            return [self.visit(ctx.declared())]+ self.visit(ctx.list_declared())


    """declared:
	var_declared 
	| const_declared
	| func_declared
	| method_declared
	| struct_declared
	| interface_declared;"""
    def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        return self.visit(ctx.getChild(0))


    # const_declared: CONST ID ASSIGN expression COCOM;
    def visitConst_declared(self, ctx:MiniGoParser.Const_declaredContext):
        return ConstDecl(ctx.ID().getText(), None, self.visit(ctx.expression()))


    # var_declared: VAR ID (all_type | all_type? ASSIGN expression) COCOM;
    def visitVar_declared(self, ctx:MiniGoParser.Var_declaredContext):
        if ctx.all_type() and ctx.expression():
            return VarDecl(ctx.ID().getText(), self.visit(ctx.all_type()), self.visit(ctx.expression()))
        elif ctx.expression():
            return VarDecl(ctx.ID().getText(), None, self.visit(ctx.expression()))
        else:
            return VarDecl(ctx.ID().getText(), self.visit(ctx.all_type()), None)


    # func_declared: FUNC ID LPAREN parameter_lit? RPAREN all_type? LCPAREN list_statement? RCPAREN COCOM;
    def visitFunc_declared(self, ctx:MiniGoParser.Func_declaredContext):
        return_type = self.visit(ctx.all_type()) if ctx.all_type() else VoidType()
        params = self.visit(ctx.parameter_lit()) if ctx.parameter_lit() else []
        statement = self.visit(ctx.list_statement()) if ctx.list_statement() else []
        return FuncDecl(ctx.ID().getText(), params, return_type, Block(statement))

    # parameter_lit: parameter COMMA parameter_lit | parameter;
    def visitParameter_lit(self, ctx:MiniGoParser.Parameter_litContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.parameter())
        else:
            return self.visit(ctx.parameter()) + self.visit(ctx.parameter_lit())


    # parameter: list_ID all_type;
    def visitParameter(self, ctx:MiniGoParser.ParameterContext):
        return [ParamDecl(item, self.visit(ctx.all_type())) for item in self.visit(ctx.list_ID())]


    # list_ID: ID COMMA list_ID | ID;
    def visitList_ID(self, ctx:MiniGoParser.List_IDContext):
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        else:
            return [ctx.ID().getText()] + self.visit(ctx.list_ID())


    # method_declared: FUNC LPAREN ID ID RPAREN ID LPAREN parameter_lit? RPAREN all_type? LCPAREN list_statement RCPAREN COCOM;
    def visitMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        return_type = self.visit(ctx.all_type()) if ctx.all_type() else VoidType()
        params = self.visit(ctx.parameter_lit()) if ctx.parameter_lit() else []
        statement = self.visit(ctx.list_statement()) if ctx.list_statement() else []
        return MethodDecl(ctx.ID()[0].getText(), Id(ctx.ID()[1].getText()), FuncDecl(ctx.ID()[2].getText(), params, return_type, Block(statement)))


    # struct_declared: TYPE ID STRUCT LCPAREN list_struct_statement RCPAREN COCOM;
    def visitStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        return StructType(ctx.ID().getText(), self.visit(ctx.list_struct_statement()), [])


    # interface_declared: TYPE ID INTERFACE LCPAREN list_method_statement RCPAREN COCOM;
    def visitInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        return InterfaceType(ctx.ID().getText(), self.visit(ctx.list_method_statement()))


    """literal:INT_LIT
       | BIN_LIT
       | OCT_LIT
       | HEX_LIT
	   | FLOAT_LIT
	   | STRING_LIT
	   | TRUE
	   | FALSE
       | NIL
	   | array_literal
	   | struct_literal;"""
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        if ctx.INT_LIT():
            return IntLiteral(ctx.INT_LIT().getText())
        elif ctx.BIN_LIT():
            return IntLiteral(int(ctx.BIN_LIT().getText(), 2))
        elif ctx.OCT_LIT():
            return IntLiteral(int(ctx.OCT_LIT().getText(), 8))
        elif ctx.HEX_LIT():
            return IntLiteral(int(ctx.HEX_LIT().getText(), 16))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText()[1:-1])
        elif ctx.TRUE():
            return BooleanLiteral(ctx.TRUE().getText())
        elif ctx.FALSE():
            return BooleanLiteral(ctx.FALSE().getText())
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.array_literal():
            return self.visit(ctx.array_literal())
        else:
            return self.visit(ctx.struct_literal())


    """sec_lit: INT_LIT
       | BIN_LIT
       | OCT_LIT
       | HEX_LIT
	   | FLOAT_LIT
	   | STRING_LIT
	   | TRUE
	   | FALSE
       | NIL
       | ID
	   | struct_literal;"""
    def visitSec_lit(self, ctx:MiniGoParser.Sec_litContext):
        if ctx.INT_LIT():
            return IntLiteral(ctx.INT_LIT().getText())
        elif ctx.BIN_LIT():
            return IntLiteral(int(ctx.BIN_LIT().getText(), 2))
        elif ctx.OCT_LIT():
            return IntLiteral(int(ctx.OCT_LIT().getText(), 8))
        elif ctx.HEX_LIT():
            return IntLiteral(int(ctx.HEX_LIT().getText(), 16))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText()[1:-1])
        elif ctx.TRUE():
            return BooleanLiteral(ctx.TRUE().getText())
        elif ctx.FALSE():
            return BooleanLiteral(ctx.FALSE().getText())
        elif ctx.NIL():
            return NilLiteral()
        else:
            return self.visit(ctx.struct_literal())

    """all_type: INT 
        | FLOAT 
        | BOOLEAN 
        | STRING 
        | list_array_type_lit 
        | ID;"""
    def visitAll_type(self, ctx:MiniGoParser.All_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.list_array_type_lit())


    """basic_type: INT 
          | FLOAT 
          | BOOLEAN 
          | STRING 
          | ID;"""
    def visitBasic_type(self, ctx:MiniGoParser.Basic_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        else:
            return Id(ctx.ID().getText())


    # list_array_type_lit: array_type_lit basic_type;
    def visitList_array_type_lit(self, ctx:MiniGoParser.List_array_type_litContext):
        return ArrayType(self.visit(ctx.array_type_lit()), self.visit(ctx.basic_type()))


    # array_type_lit: array_type array_type_lit | array_type;
    def visitArray_type_lit(self, ctx:MiniGoParser.Array_type_litContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.array_type())]
        else:
            return [self.visit(ctx.array_type())] + self.visit(ctx.array_type_lit())


    # array_type: LSPAREN (INT_LIT | ID) RSPAREN;
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        if ctx.INT_LIT():
            return IntLiteral(ctx.INT_LIT().getText())
        else:
            return Id(ctx.ID().getText())


    # array_literal: dim_lit all_type LCPAREN list_array_element RCPAREN;
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return ArrayLiteral(self.visit(ctx.dim_lit())
                            , self.visit(ctx.all_type())
                            , self.visit(ctx.list_array_element()))


    # dim_lit: dim dim_lit | dim;
    def visitDim_lit(self, ctx:MiniGoParser.Dim_litContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.dim())]
        else:
            return [self.visit(ctx.dim())] + self.visit(ctx.dim_lit())


    # dim: LSPAREN (INT_LIT | ID) RSPAREN;
    def visitDim(self, ctx:MiniGoParser.DimContext):
        if ctx.INT_LIT():
            return IntLiteral(ctx.INT_LIT().getText())
        else:
            return Id(ctx.ID().getText())


    # list_array_element: array_element COMMA list_array_element | array_element;
    def visitList_array_element(self, ctx:MiniGoParser.List_array_elementContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.array_element())]
        else:
            return [self.visit(ctx.array_element())] + self.visit(ctx.list_array_element())


    # array_element: sec_lit | LCPAREN list_array_element RCPAREN;
    def visitArray_element(self, ctx:MiniGoParser.Array_elementContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.sec_lit())
        else:
            return self.visit(ctx.list_array_element())


    # struct_literal: ID LCPAREN (list_elements_lit | ) RCPAREN;
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        if ctx.list_elements_lit():
            return StructLiteral(ctx.ID().getText(), self.visit(ctx.list_elements_lit()))
        else:
            return StructLiteral(ctx.ID().getText(), [])


    # list_elements_lit: list_element COMMA list_elements_lit | list_element;
    def visitList_elements_lit(self, ctx:MiniGoParser.List_elements_litContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.list_element())]
        else:
            return [self.visit(ctx.list_element())] + self.visit(ctx.list_elements_lit())



    # list_element: ID COLON expression;
    def visitList_element(self, ctx:MiniGoParser.List_elementContext):
        return (ctx.ID().getText(), self.visit(ctx.expression()))


    # list_expression: expression COMMA list_expression | expression;
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        else:
            return [self.visit(ctx.expression())] + self.visit(ctx.list_expression())


    # expression: expression OR expression1 | expression1;
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression1())
        else:
            return BinaryOp(ctx.OR().getText(),self.visit(ctx.expression()), self.visit(ctx.expression1()))


    # expression1: expression1 AND expression2 | expression2;
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression2())
        else:
            return BinaryOp(ctx.AND().getText(), self.visit(ctx.expression1()), self.visit(ctx.expression2()))


    # expression2: expression2 (EQUAL | NEQUAL | LT | LTE | GT | GTE) expression3 | expression3;
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression3())
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression2()), self.visit(ctx.expression3()))


    # expression3: expression3 (ADD | SUB) expression4 | expression4;
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression4())
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))


    # expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression5())
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression4()), self.visit(ctx.expression5()))


    # expression5: (NOT | SUB) expression5 | expression6;
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression6())
        else:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expression5()))


    """expression6: expression6 LSPAREN expression RSPAREN 
            | expression6 DOT ID 
            | expression6 DOT ID LPAREN funcall RPAREN
            | expression7;"""
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression7())
        elif ctx.LSPAREN() and ctx.RSPAREN():
            expression6 = self.visit(ctx.expression6())
            if type(expression6) == ArrayCell:
                return ArrayCell(expression6.arr, expression6.idx  + [self.visit(ctx.expression())])
            return ArrayCell(expression6, [self.visit(ctx.expression())])
        elif ctx.DOT():
            if ctx.LPAREN() and ctx.RPAREN():
                return MethCall(self.visit(ctx.expression6()),ctx.ID().getText(), self.visit(ctx.funcall()))
            else:
                return FieldAccess(self.visit(ctx.expression6()), ctx.ID().getText())
        else:
            return self.visit(ctx.expression7())
        


    # expression7: literal | LPAREN expression RPAREN | ID | ID LPAREN funcall RPAREN;
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.ID() and ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        elif ctx.expression():
            return self.visit(ctx.expression())
        else:
            return FuncCall(ctx.ID().getText(), self.visit(ctx.funcall()))


    # funcall: funcall_noempty | ;
    def visitFuncall(self, ctx:MiniGoParser.FuncallContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.funcall_noempty())


    # funcall_noempty: expression | expression COMMA funcall_noempty;
    def visitFuncall_noempty(self, ctx:MiniGoParser.Funcall_noemptyContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        else:
            return [self.visit(ctx.expression())] + self.visit(ctx.funcall_noempty())


    # list_statement: statement list_statement | statement;
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.statement())]
        else:
            return [self.visit(ctx.statement())] + self.visit(ctx.list_statement())


    """statement:
    assign_statement
    | if_statement
    | for_statement
    | break_statement
    | continue_statement
    | call_statement
    | return_statement
    | const_declared
    | var_declared;"""
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visit(ctx.getChild(0))


    # assign_statement: assignment_lhs operators expression COCOM;
    def visitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        operator = self.visit(ctx.operators())
        assignment_lhs = self.visit(ctx.assignment_lhs())
        expression = self.visit(ctx.expression())
        if operator == "=":
            return Assign(assignment_lhs, expression)
        return Assign(assignment_lhs, BinaryOp(operator, assignment_lhs, expression))


    # operators:  COLONEQUAL | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN;
    def visitOperators(self, ctx:MiniGoParser.OperatorsContext):
        if ctx.COLONEQUAL():
            return "="
        elif ctx.ADD_ASSIGN():
            return "+"
        elif ctx.SUB_ASSIGN():
            return "-"
        elif ctx.MUL_ASSIGN():
            return "*"
        elif ctx.DIV_ASSIGN():
            return "/"
        return "%"


    # assignment_lhs: assignment_lhs (LSPAREN expression RSPAREN | DOT ID)  | ID;
    def visitAssignment_lhs(self, ctx:MiniGoParser.Assignment_lhsContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        else:
            if ctx.LSPAREN() and ctx.RSPAREN():
                assignment_lhs = self.visit(ctx.assignment_lhs())
                if type(assignment_lhs) == ArrayCell:
                    return ArrayCell(assignment_lhs.arr, assignment_lhs.idx  + [self.visit(ctx.expression())])
                return ArrayCell(assignment_lhs, [self.visit(ctx.expression())])
            else:
                return FieldAccess(self.visit(ctx.assignment_lhs()), ctx.ID().getText())



    # else_statement: ELSE LCPAREN list_statement? RCPAREN;
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        return Block(self.visit(ctx.list_statement())) if ctx.list_statement() else []


    # elif_statement: ELSE IF LPAREN expression RPAREN LCPAREN list_statement? RCPAREN;
    def visitElif_statement(self, ctx:MiniGoParser.Elif_statementContext):
        listStmt = self.visit(ctx.list_statement()) if ctx.list_statement() else []
        return (self.visit(ctx.expression()), Block(listStmt))
    
    # elif_statement_lit: elif_statement elif_statement_lit | elif_statement;
    def visitElif_statement_lit(self, ctx:MiniGoParser.Elif_statement_litContext):
        return [self.visit(ctx.elif_statement())] if ctx.getChildCount() == 1 else [self.visit(ctx.elif_statement())] + self.visit(ctx.elif_statement_lit())


    # if_statement: IF LPAREN expression RPAREN LCPAREN list_statement? RCPAREN elif_statement_lit? else_statement? COCOM;
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        def if_recursive(list_else_if, else_stament):
            if(len(list_else_if) == 0): return else_stament
            exp,block = list_else_if[0]
            return If(exp,block,if_recursive(list_else_if[1:], else_stament))
        listStmt = self.visit(ctx.list_statement()) if ctx.list_statement() else []
        list_else_if = self.visit(ctx.elif_statement_lit()) if ctx.elif_statement_lit() else []
        else_statement = self.visit(ctx.else_statement()) if ctx.else_statement() else []
        return If(self.visit(ctx.expression()), Block(listStmt), if_recursive(list_else_if, else_statement))
        


    # var_declared_for: VAR ID all_type? ASSIGN expression COCOM;
    def visitVar_declared_for(self, ctx:MiniGoParser.Var_declared_forContext):
        id = ctx.ID().getText()
        type_id = self.visit(ctx.all_type()) if ctx.all_type() else []
        expression = self.visit(ctx.expression())
        return VarDecl(id, type_id, expression)


    # range_loop: ID COMMA ID COLONEQUAL RANGE expression;
    def visitRange_loop(self, ctx:MiniGoParser.Range_loopContext):
        idx = Id(ctx.ID()[0].getText())
        value = Id(ctx.ID()[1].getText())
        arr = self.visit(ctx.expression())
        return idx, value, arr


    # init_loop: (ID operators expression COCOM | var_declared_for) expression COCOM ID operators expression;
    def visitInit_loop(self, ctx:MiniGoParser.Init_loopContext):
        if ctx.var_declared_for():
            init = self.visit(ctx.var_declared_for())
        else:
            operator_init = self.visit(ctx.operators(0))
            if operator_init == "=":
                init = Assign(Id(ctx.ID(0).getText()), self.visit(ctx.expression(0)))
            else:
                init = Assign(Id(ctx.ID(0).getText()), BinaryOp(operator_init, Id(ctx.ID(0).getText()), self.visit(ctx.expression(0))))
        cond = self.visit(ctx.expression(0)) if ctx.var_declared_for() else self.visit(ctx.expression(1))
        operator = self.visit(ctx.operators(0)) if ctx.var_declared_for() else self.visit(ctx.operators(1))
        id = Id(ctx.ID(0).getText()) if ctx.var_declared_for() else Id(ctx.ID(1).getText())
        expression = self.visit(ctx.expression(1)) if ctx.var_declared_for() else self.visit(ctx.expression(2))
        if operator == "=":
            upda = Assign(id, expression)
        else:
            upda = Assign(id, BinaryOp(operator, id, expression))
        return init, cond, upda

    # basic_loop: expression;
    def visitBasic_loop(self, ctx:MiniGoParser.Basic_loopContext):
        return self.visit(ctx.expression())


    # for_statement: FOR (basic_loop | init_loop | range_loop) LCPAREN list_statement? RCPAREN COCOM;
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        listStmt = self.visit(ctx.list_statement()) if ctx.list_statement() else []
        if ctx.basic_loop():
            return ForBasic(self.visit(ctx.basic_loop()), Block(listStmt))
        elif ctx.init_loop():
            init, cond, upda = self.visit(ctx.init_loop())
            return ForStep(init, cond, upda, Block(listStmt))
        else:
            idx, value, arr = self.visit(ctx.range_loop())
            return ForEach(idx, value, arr, Block(listStmt))


    # break_statement: BREAK COCOM;
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return Break()


    # continue_statement: CONTINUE COCOM;
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return Continue()


    # call_statement: ((assignment_lhs DOT) | ) ID LPAREN (list_expression | ) RPAREN COCOM;
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        listExp = self.visit(ctx.list_expression()) if ctx.list_expression() else []
        if ctx.assignment_lhs():
            return MethCall(self.visit(ctx.assignment_lhs()), ctx.ID().getText(), listExp)
        else:
            return FuncCall(ctx.ID().getText(), listExp)


    # return_statement: RETURN (expression | ) COCOM;
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return Return(self.visit(ctx.expression()) if ctx.expression() else None)


    # struct_statement: ID all_type COCOM;
    def visitStruct_statement(self, ctx:MiniGoParser.Struct_statementContext):
        return (ctx.ID().getText(), self.visit(ctx.all_type()))
    
    #list_struct_statement: struct_statement list_struct_statement | struct_statement;
    def visitList_struct_statement(self, ctx:MiniGoParser.List_struct_statementContext):
        return [self.visit(ctx.struct_statement())] if ctx.getChildCount() == 1 else [self.visit(ctx.struct_statement())] + self.visit(ctx.list_struct_statement())


    # method_parameter: list_ID all_type;
    def visitMethod_parameter(self, ctx:MiniGoParser.Method_parameterContext):
        listID = self.visit(ctx.list_ID())
        return [self.visit(ctx.all_type()) for item in listID]


    # method_parameter_lit: method_parameter COMMA method_parameter_lit | method_parameter;
    def visitMethod_parameter_lit(self, ctx:MiniGoParser.Method_parameter_litContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.method_parameter())
        else:
            return self.visit(ctx.method_parameter()) + self.visit(ctx.method_parameter_lit())


    # method_statement: ID LPAREN (method_parameter_lit | ) RPAREN (all_type | ) COCOM;
    def visitMethod_statement(self, ctx:MiniGoParser.Method_statementContext):
        params = self.visit(ctx.method_parameter_lit()) if ctx.method_parameter_lit() else []
        return_type = self.visit(ctx.all_type()) if ctx.all_type() else VoidType()
        return Prototype(ctx.ID().getText(), params, return_type)
    
    # list_method_statement: method_statement list_method_statement | method_statement;
    def visitList_method_statement(self, ctx:MiniGoParser.List_method_statementContext):
        return [self.visit(ctx.method_statement())] if ctx.getChildCount() == 1 else [self.visit(ctx.method_statement())] + self.visit(ctx.list_method_statement())
    
