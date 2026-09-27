class ProfitCalculator:
    def __init__(self, revenue, cost_of_goods, expenses):
        self.revenue = revenue
        self.cost_of_goods = cost_of_goods
        self.expenses = expenses

    def gross_profit(self):
        return self.revenue - self.cost_of_goods

    def net_profit(self):
        return self.gross_profit() - self.expenses

    def profit_margin(self):
        if self.revenue == 0:
            return 0

        return (self.net_profit() / self.revenue) * 100

        