import expressions


class TAlways(expressions.BExpression):
    def __init__(self, expr):
        self.subexp = expr

    def __str__(self):
        return "\u2666" + str(self.subexp)


class TEventually(expressions.BExpression):
    def __init__(self, expr):
        self.subexp = expr

    def __str__(self):
        return "\u25A1" + str(self.subexp)


print(TAlways(expressions.BVariable("y")))
print(TEventually(expressions.BVariable("y")))
