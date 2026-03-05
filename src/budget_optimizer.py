# Budget Optimizer Module

class BudgetOptimizer:
    def __init__(self, budget, expenses):
        self.budget = budget
        self.expenses = expenses

    def optimize(self):
        # Simple optimization logic for budget allocation
        optimized_expenses = {}
        total_expense = sum(self.expenses.values())

        if total_expense <= self.budget:
            return self.expenses
        else:
            for item, cost in self.expenses.items():
                if cost <= self.budget:
                    optimized_expenses[item] = cost
                    self.budget -= cost
            return optimized_expenses

    def remaining_budget(self):
        return self.budget

# Example Usage
# optimizer = BudgetOptimizer(1000, {'food': 200, 'transport': 150, 'accommodation': 300})
# print(optimizer.optimize())
# print(optimizer.remaining_budget())