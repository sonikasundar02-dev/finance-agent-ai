def aero_agent(distance, payload, wind_type, wind_speed):
    base_fuel_per_km = 5
    base_fuel = distance * base_fuel_per_km

    if "headwind" in wind_type:
        impact = 1 + (wind_speed / 100)
    elif "tailwind" in wind_type:
        impact = 1 - (wind_speed / 100)
    else:
        impact = 1

    fuel_burn = base_fuel * impact
    percent = (impact - 1) * 100

    return fuel_burn, percent


def emission_agent(fuel_burn, carbon_price):
    emissions = fuel_burn * 3.16
    carbon_cost = emissions * carbon_price

    return emissions, carbon_cost


def financial_agent(fuel_burn, fuel_price, carbon_cost, wind_type):
    fuel_cost = fuel_burn * fuel_price
    total_cost = fuel_cost + carbon_cost

    # Simple intelligence
    if "headwind" in wind_type:
        decision = "WAIT"
        savings = 0.1 * total_cost
        reason = "Headwind detected → higher fuel burn"
    else:
        decision = "DEPART NOW"
        savings = 0.05 * total_cost
        reason = "Favorable wind conditions"

    return decision, reason, savings, total_cost
