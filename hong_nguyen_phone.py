def get_units():
    """
    Ask the user for the number of units used.
    
    Returns:
    An integer representing the number of units used
    """
    return int(input("Enter number of units used: "))

def calculate_cost(units, base_cost, base_limit, cost_per_additional_unit):
    """
    Calculate the cost for a phone plan.
    
    Parameters:
    units -- the number of units used
    base_cost -- the base cost of the plan
    base_limit -- the number of units included in the base cost
    cost_per_additional_unit -- the cost per unit when exceeding the base limit
    
    Returns:
    The total cost for the plan
    """
    # Start with the base cost
    total_cost = base_cost
    
    # Add cost for additional units if any
    if units > base_limit:
        additional_units = units - base_limit
        additional_cost = additional_units * cost_per_additional_unit
        total_cost += additional_cost
    
    return total_cost

def main():
    # Get the number of units from the user
    units = get_units()
    
    # Check if the unit value is valid
    if units < 0:
        print("You cannot have negative units.")
        return
    
    # Plan 1: $9.38 base cost for 65 units, 4.5 cents per additional unit
    plan1_cost = calculate_cost(units, 9.38, 65, 0.045)
    
    # Plan 2: $8.57 base cost for 50 units, 5.2 cents per additional unit
    plan2_cost = calculate_cost(units, 8.57, 50, 0.052)
    
    # Display the costs with proper formatting
    print(f"Cost for plan 1: ${plan1_cost:.2f}")
    print(f"Cost for plan 2: ${plan2_cost:.2f}")
    
    # Determine which plan is less expensive
    if plan1_cost < plan2_cost:
        print("Plan 1 is cheaper.")
    else:
        print("Plan 2 is cheaper.")

main()