

class HistoryManager:
    def __init__(self):
        self.history = []

    def add_operation(self, operation):
        self.history.append(operation)

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []

    def get_formatted_history(self):
        formatted_history = []
        for idx, operation in enumerate(self.history, start=1):
            expression = operation.get("expression: ", "")
            result = operation.get("result = ", "")
            formatted_operation = f"Operation {idx}: {expression},  Result = {result}"
            formatted_history.append(formatted_operation)
        return formatted_history
