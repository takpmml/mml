import expressions

class TAlways(expressions.BExpression):
    def __init__(self, expr):
        self.subexp = expr

    def __str__(self):
        return "\u25C6" + str(self.subexp)


print(TAlways(expressions.BVariable("y")))
