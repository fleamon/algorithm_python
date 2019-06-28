#!/usr/bin/env python
# -*- encoding: utf-8


def solve(meal_cost, tip_percent, tax_percent):
    res = 0
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    res = meal_cost + tip + tax
    print int(round(res))


if __name__ == '__main__':
    # meal_cost = float(raw_input())
    meal_cost = 12.00

    # tip_percent = int(raw_input())
    tip_percent = 20

    # tax_percent = int(raw_input())
    tax_percent = 8

    solve(meal_cost, tip_percent, tax_percent)
