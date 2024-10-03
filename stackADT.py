class Stack:
    def _init_(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None  

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
def perform_stack_operations():
    stack = Stack()
    output = []
    while True:
        operation = input("\nEnter operation: ").strip()
        
        if operation.lower() == 'exit':
            break
        elif operation.startswith("push"):
            _, value = operation.split()
            stack.push(int(value))
            print(f"Pushed {value} onto the stack.")
        elif operation == "pop":
            popped_value = stack.pop()
            if popped_value is not None:
                print(f"Popped {popped_value} from the stack.")
            else:
                print("Stack is empty. Nothing to pop.")
        elif operation == "peek":
            top_value = stack.peek()
            if top_value is not None:
                output.append(top_value)
                print(f"Top value is: {top_value}")
            else:
                print("Stack is empty. Nothing to peek.")
        else:
            print("Invalid operation. Please try again.")
    print("\nOutput of peek operations:", output)
perform_stack_operations()
