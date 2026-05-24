PRODUCT_CATALOG = [
    {"name": "Minimal Desk", "price": 800, "type": "desk", "url": "https://ikea.com/desk"},
    {"name": "Ergonomic Chair", "price": 600, "type": "chair", "url": "https://ikea.com/chair"},
    {"name": "LED Lamp", "price": 120, "type": "light", "url": "https://ikea.com/lamp"},
    {"name": "27 inch Monitor", "price": 900, "type": "monitor", "url": "https://amazon.com/monitor"},
]

def planner(request):
    return {
        "budget": 5000,
        "location": "Malaysia",
        "needs": ["desk", "chair", "light", "monitor"]
    }

def logistics(price, location):
    shipping = 100
    tax = price * 0.08
    return shipping, tax

def solver(plan):
    selected = []
    total = 0

    for item in PRODUCT_CATALOG:
        if item["type"] in plan["needs"]:
            shipping, tax = logistics(item["price"], plan["location"])
            cost = item["price"] + shipping + tax

            if total + cost <= plan["budget"]:
                selected.append((item, cost))
                total += cost

    return selected, total

def generate_quote(items, total):
    print("\n==============================")
    print(" AUTONOMOUS SALES ENGINEER QUOTE")
    print("==============================\n")

    for item, cost in items:
        print("- Name:", item["name"])
        print("  Price:", item["price"])
        print("  URL:", item["url"])
        print("  Total Cost (with tax+shipping):", round(cost, 2))
        print()

    print("------------------------------")
    print("FINAL TOTAL COST:", round(total, 2))
    print("------------------------------")

    print("\nReasoning Summary:")
    print("- Retrieved items from catalog")
    print("- Applied constraint filtering")
    print("- Included shipping and tax (TCO)")
    print("- Ensured budget compliance")

def main():
    user_request = "I need a minimalist home office under RM5000"

    plan = planner(user_request)
    items, total = solver(plan)
    generate_quote(items, total)

if __name__ == "__main__":
    main()