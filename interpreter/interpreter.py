from .values import Number


class Interpreter:
    def __init__(self, x: float = 0):
        self.x = x

    # A tricky way to evaluate appropriate class methods for each node type without if/elif statements
    def visit(self, node):
        # e.g AddNode -> 'visit_AddNode'
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name)
        return method(node)

    @staticmethod
    def visit_NumberNode(node):
        return Number(node.value)

    def visit_XNode(self):
        return Number(self.x)

    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_SubtractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except ZeroDivisionError:
            raise Exception("Maths error!")

    def visit_PlusNode(self, node):
        return self.visit(node.node)

    def visit_MinusNode(self, node):
        return Number(-self.visit(node.node).value)

    def visit_PowerNode(self, node):
        return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value)
