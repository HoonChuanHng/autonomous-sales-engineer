# Autonomous Sales Engineer

## Overview

This project is an AI-powered Autonomous Sales Engineer agent that generates complete product solutions from a high-level customer requirement.

It simulates a technical sales consultant that designs a full system (e.g., home office setup) by selecting items from a product catalog, applying constraints, ensuring budget compliance, and calculating total cost including logistics (shipping and tax).

Example:
"I need a minimalist home office under RM5000"

The system automatically:
- Extracts requirements
- Selects suitable products
- Applies budget constraints
- Calculates shipping and tax
- Generates a professional quotation

---

## Features

- Constraint-based product selection
- Budget-aware decision making
- Product type matching (desk, chair, light, monitor)
- Shipping and tax calculation
- Total Cost of Ownership (TCO) computation
- Autonomous agent workflow
- Automated quotation generation

---

## System Architecture

The agent is divided into four components:

### Planner Agent
- Parses user request
- Extracts budget, location, and required items

### Solver Agent
- Matches required product types from catalog
- Ensures budget constraints are not violated
- Selects optimal set of products

### Logistics Module
- Calculates shipping cost
- Calculates tax based on total item price

### Quote Generator
- Produces final structured quotation
- Includes item list, URLs, and final cost breakdown

---

## Product Catalog

The system uses a mock product catalog:

- Minimal Desk (RM800)
- Ergonomic Chair (RM600)
- LED Lamp (RM120)
- 27 inch Monitor (RM900)

Each product includes:
- Name
- Price
- Type
- URL

---

## System Requirements

- Python 3.10+
- No external dependencies required (standard library only)

---

## Installation & Usage

### Step 1: Clone repository
```bash
git clone <your-repository-link>
cd autonomous-sales-engineer
```
### Step 2: Run the program
```bash
python agent.py
```

## Example Output
AUTONOMOUS SALES ENGINEER QUOTE

- Minimal Desk
  Price: 800
  URL: https://ikea.com/desk
  Total Cost (with tax + shipping): XXXX

- Ergonomic Chair
  Price: 600
  URL: https://ikea.com/chair
  Total Cost (with tax + shipping): XXXX

- LED Lamp
  Price: 120
  URL: https://ikea.com/lamp
  Total Cost (with tax + shipping): XXXX

- 27 inch Monitor
  Price: 900
  URL: https://amazon.com/monitor
  Total Cost (with tax + shipping): XXXX

------------------------------
FINAL TOTAL COST: RMXXXX
------------------------------

Reasoning Summary:
- Retrieved items from product catalog
- Applied constraint-based filtering
- Calculated shipping and tax (TCO)
- Ensured total budget compliance
