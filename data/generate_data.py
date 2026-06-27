import csv, random
from datetime import datetime, timedelta
from pathlib import Path
from faker import Faker

Faker.seed(42); random.seed(42); fake = Faker()
START, END = datetime(2024, 1, 1), datetime(2026, 4, 1)
REGIONS = ["North America", "Europe", "Asia Pacific", "Latin America", "MEA"]
PRODUCTS = ["Starter", "Growth", "Scale", "Enterprise"]

with (Path(__file__).parent / "sample_kpi_data.csv").open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["order_id", "order_date", "region", "product", "customer", "units", "unit_price", "revenue"])
    for i in range(1, 50_001):
        d = START + timedelta(days=random.randint(0, (END - START).days))
        product = random.choices(PRODUCTS, weights=[35, 30, 25, 10])[0]
        units = random.randint(1, 12)
        unit_price = round({"Starter": 49, "Growth": 199, "Scale": 499, "Enterprise": 1499}[product] * random.uniform(0.85, 1.15), 2)
        w.writerow([f"ORD-{i:06d}", d.strftime("%Y-%m-%d"), random.choice(REGIONS), product, fake.company(), units, unit_price, round(units * unit_price, 2)])