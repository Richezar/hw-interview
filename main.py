class Stack():
    def __init__(self, stack):
        self.stack = stack

    def is_empty(self):
        return False if len(self.stack) > 0 else True

    def push(self, i):
        self.stack.append(i)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_balanced_brackets(self):
        opening_brackets = ['(', '{', '[']
        closing_brackets = [')', '}', ']']
        bracket_stack = []
        for bracket in self.stack:
            if bracket in opening_brackets:
                bracket_stack.append(bracket)
            elif bracket in closing_brackets:
                if len(bracket_stack) == 0:
                    return f'{self.stack} - несбалансированная последовательность'
                popped_bracket = bracket_stack.pop()
                if popped_bracket == '(' and bracket == ')':
                    continue
                if popped_bracket == '{' and bracket == '}':
                    continue
                if popped_bracket == '[' and bracket == ']':
                    continue
                return f'{self.stack} - несбалансированная последовательность'
        if len(bracket_stack) != 0:
            return f'{self.stack} - несбалансированная последовательность'
        return f'{self.stack} - сбалансированная последовательность'


if __name__ == '__main__':
    check_balance = Stack("(((([{}]))))")
    print(check_balance.is_balanced_brackets())
    check_balance_2 = Stack("[([])((([[[]]])))]{()}")
    print(check_balance_2.is_balanced_brackets())
    check_balance_3 = Stack("{{[()]}}")
    print(check_balance_3.is_balanced_brackets())
    check_balance_4 = Stack("}{}")
    print(check_balance_4.is_balanced_brackets())
    check_balance_5 = Stack("{{[(])]}}")
    print(check_balance_5.is_balanced_brackets())
    check_balance_6 = Stack("[[{())}]")
    print(check_balance_6.is_balanced_brackets())