def p_declaracion_variable_funcion(p): 
    '''declaracion_variable_funcion : tipo ID PUNTOCOMA
                                    | tipo ID IGUAL expresion PUNTOCOMA
                                    | CONST tipo ID PUNTOCOMA
                                    | CONST tipo ID IGUAL expresion PUNTOCOMA
                                    | tipo ID APAREN parametros CPAREN bloque'''
    # se obtienen las líneas y columnas con lineno y lexpos para que el Semantico pueda reportar errores exactos
    if len(p) == 4: 
        p[0] = ('decl_var_simple', p[1], p[2], p.lineno(2), p.lexpos(2))
    elif len(p) == 6: 
        p[0] = ('decl_var_comp', p[1], p[2], p[4], p.lineno(2), p.lexpos(2))
    #producciones para const
    elif len(p) == 5 and p[1] == 'const': 
        p[0] = ('decl_const_simple', p[2], p[3], p.lineno(3), p.lexpos(3))
    elif len(p) == 7: 
        p[0] = ('decl_const_comp', p[2], p[3], p[5], p.lineno(3), p.lexpos(3))
    #
    elif len(p) == 7 and p[1] != 'const': 
        p[0] = ('decl_var_func', p[1], p[2], p[4], p[6], p.lineno(2), p.lexpos(2))
