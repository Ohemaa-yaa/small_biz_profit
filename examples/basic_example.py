import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from small_biz_profit import ProfitCalculator

business = ProfitCalculator(
    revenue=25000,
    cost_of_goods=19000,
    expenses=3000,
)

print("Gross Profit:", business.gross_profit())
print("Net Profit:", business.net_profit())
print("Profit Margin:", business.profit_margin(), "%")

