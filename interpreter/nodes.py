class NumberNode:
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f"{self.value}"


class XNode:
    def __repr__(self):
        return "x"


class AddNode:
    def __init__(self, node_a: any, node_b: any):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"


class SubtractNode:
    def __init__(self, node_a: any, node_b: any):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"


class MultiplyNode:
    def __init__(self, node_a: any, node_b: any):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"


class DivideNode:
    def __init__(self, node_a: any, node_b: any):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"


class PowerNode:
    def __init__(self, node_a: any, node_b: any):
        self.node_a = node_a
        self.node_b = node_b

    def __repr__(self):
        return f"({self.node_a}^{self.node_b})"


class PlusNode:
    def __init__(self, node: any):
        self.node = node

    def __repr__(self):
        return f"(+{self.node})"


class MinusNode:
    def __init__(self, node: any):
        self.node = node

    def __repr__(self):
        return f"(-{self.node})"

