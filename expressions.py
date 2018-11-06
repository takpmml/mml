class BExpression:
    """Boolean expression"""
    def __str__(self):
        return None

    def eval(self, interp):
        return None


class BTrue(BExpression):
    def __str__(self):
        return "t"

    def eval(self, _):
        return True


class BFalse(BExpression):

    def __str__(self):
        return "f"

    def eval(self, _):
        return False


class BVariable(BExpression):
    """Boolena variable"""
    def __init__(self, var_name):
        assert isinstance(var_name, str)
        self.var_name = var_name

    def __str__(self):
        return self.var_name

    def eval(self, interp):
        return interp(self.var_name)


class BNeg(BExpression):
    """Negacja"""
    def __init__(self, expr):
        assert isinstance(expr, BExpression)
        self.subexpr = expr

    def eval(self, interp):
        return not self.subexpr.eval(interp)

    def __str__(self):
        return "neg ({0})".format(self.subexpr)


class BAnd(BExpression):
    def __init__(self, lexp, rexp):
        assert isinstance(lexp, BExpression)
        assert isinstance(rexp, BExpression)
        self.lexpr = lexp
        self.rexpr = rexp

    def eval(self, interp):
        if not self.lexpr.eval(interp):
            return False
        return self.rexpr.eval(interp)

    def __str__(self):
        return "({0} and {1})".format(self.lexpr, self.rexpr)


e = BAnd(BNeg(BVariable("x")), BVariable("y"))

print(e)
print(e.eval(lambda _: True))