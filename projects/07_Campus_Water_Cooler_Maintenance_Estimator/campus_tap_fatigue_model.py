"""
===================================================================
 RKMVCC RAHARA WATER COOLER TAP MAINTENANCE ESTIMATOR
 A Standalone Real World Fermi Estimation Tool
===================================================================
 Context:
  - 1,200 Campus Population (Students, Staff, Faculty)
  - 10 Water Coolers (20 Push-Cock Taps Total)
  - 80% Boarder Student Base (using coolers as primary water source)
  - Concentrated UG Foot-Traffic (75% load on 5 UG coolers)
  - Monday VIP/Guest Delegation Surge Load
===================================================================
"""


def calculate_tap_fatigue(
    pop_total=1200,
    boarder_pct=0.80,
    ug_traffic_split=0.75,
    total_taps=20,
    ug_taps=10,
    rated_lifespan=20000,
    academic_days=250,
):
    """
    Calculates annual mechanical tap replacements and lifespan by zone.
    """
    # 1. Non-student population baseline
    # (105 Regular Faculty/Staff + 4 Monastic Profs + 4 Visiting Prof Equivalents)
    non_students = 113
    students = max(0, pop_total - non_students)

    # 2. Student breakdown
    boarders = students * boarder_pct
    day_scholars = students * (1.0 - boarder_pct)

    # 3. Daily Water Volume (Liters)
    # Boarders: 3L/day (filling bottles for hostel rooms)
    # Day Scholars & Staff: 1L/day
    daily_liters = (boarders * 3.0) + (day_scholars * 1.0) + (non_students * 1.0)

    # 4. Convert to Annual Press Actions (1 Liter = 1 long-press fill)
    annual_student_presses = daily_liters * academic_days

    # 5. VIP Monday Surge Load
    # Avg 8 visitors * 1.0 Liter * 35 active Mondays/year
    annual_vip_presses = 8 * 1.0 * 35

    total_annual_presses = annual_student_presses + annual_vip_presses

    # 6. Foot-Traffic Skew (UG Building vs Rest of Campus)
    ug_presses = total_annual_presses * ug_traffic_split
    other_presses = total_annual_presses * (1.0 - ug_traffic_split)

    other_taps = max(1, total_taps - ug_taps)

    # Cycles per individual tap in each zone
    ug_cycles_per_tap = ug_presses / ug_taps
    other_cycles_per_tap = other_presses / other_taps

    # 7. Failures and Lifespan
    ug_failures = (ug_cycles_per_tap / rated_lifespan) * ug_taps
    other_failures = (other_cycles_per_tap / rated_lifespan) * other_taps

    ug_lifespan_months = (
        12.0 / (ug_cycles_per_tap / rated_lifespan)
        if ug_cycles_per_tap > 0
        else 0
    )
    other_lifespan_months = (
        12.0 / (other_cycles_per_tap / rated_lifespan)
        if other_cycles_per_tap > 0
        else 0
    )

    return {
        "ug_failures": ug_failures,
        "other_failures": other_failures,
        "total_failures": ug_failures + other_failures,
        "ug_lifespan_months": ug_lifespan_months,
        "other_lifespan_months": other_lifespan_months,
        "daily_liters": daily_liters,
        "total_presses": total_annual_presses,
    }


def update_variables_batch(params, labels):
    """Allows step-by-step update of all variables."""
    print("\n--- BULK UPDATE (Press ENTER to keep current value) ---")
    for key, label in labels.items():
        curr = params[key]
        user_in = input(f" {label} [Current: {curr}]: ").strip()
        if user_in:
            try:
                parsed = float(user_in)
                params[key] = int(parsed) if isinstance(curr, int) else parsed
            except ValueError:
                print("  [!] Invalid number. Preserving current value.")


def update_variables_targeted(choice_str, params, labels):
    """Allows updating targeted variables by numbers (e.g. '1, 3')."""
    param_keys = list(params.keys())
    indices = []

    for item in choice_str.split(","):
        item = item.strip()
        if item.isdigit() and 1 <= int(item) <= len(param_keys):
            indices.append(int(item))

    if not indices:
        print("\n[!] Invalid selection. Type numbers like '1, 3' or 'all'.")
        return

    print("\n--- UPDATE SELECTED VARIABLES ---")
    for idx in indices:
        key = param_keys[idx - 1]
        curr = params[key]
        user_in = input(f" {labels[key]} [Current: {curr}]: ").strip()
        if user_in:
            try:
                parsed = float(user_in)
                params[key] = int(parsed) if isinstance(curr, int) else parsed
            except ValueError:
                print("  [!] Invalid number. Preserving current value.")


def main():
    # Parameters & defaults
    params = {
        "pop_total": 1200,
        "boarder_pct": 0.80,
        "ug_traffic_split": 0.75,
        "total_taps": 20,
        "ug_taps": 10,
        "rated_lifespan": 20000,
        "academic_days": 250,
    }

    labels = {
        "pop_total": "Total Campus Population",
        "boarder_pct": "Boarder Student Ratio (0.80 = 80%)",
        "ug_traffic_split": "UG Building Traffic Ratio (0.75 = 75%)",
        "total_taps": "Total Campus Taps (Coolers x 2)",
        "ug_taps": "UG Building Taps (5 Coolers x 2)",
        "rated_lifespan": "Mechanical Tap Cycle Lifespan",
        "academic_days": "Operating Academic Days / Year",
    }

    while True:
        # Unpack params dictionary directly into the calculation function
        res = calculate_tap_fatigue(**params)

        print("\n" + "=" * 60)
        print(" RKMVCC RAHARA WATER COOLER TAP MAINTENANCE ESTIMATOR")
        print("=" * 60)
        for idx, (key, label) in enumerate(labels.items(), 1):
            val = params[key]
            formatted = f"{val:,}" if isinstance(val, int) else f"{val}"
            print(f" {idx}. {label:<38}: {formatted}")

        print("-" * 60)
        print(" SIMULATION RESULTS & BREAKDOWN:")
        print(f"  * Daily Water Dispensed       : {res['daily_liters']:,.0f} Liters/day")
        print(f"  * Total Annual Tap Press Actions: {res['total_presses']:,.0f} cycles")
        print(
            f"  * UG Building Tap Failures    : {res['ug_failures']:.1f} / yr "
            f"(~{res['ug_lifespan_months']:.1f} mo lifespan)"
        )
        print(
            f"  * Rest of Campus Tap Failures : {res['other_failures']:.1f} / yr "
            f"(~{res['other_lifespan_months']:.1f} mo lifespan)"
        )
        print(f"  --> TOTAL REPLACEMENTS NEEDED : {res['total_failures']:.1f} taps/year")
        print("=" * 60)

        print("\nOPTIONS:")
        print("  - Type 'all' to update ALL variables.")
        print("  - Type numbers (e.g., '1, 3') to update specific variables.")
        print("  - Type '0' or 'exit' to quit.")

        user_choice = input("\nYour choice: ").strip().lower()

        if user_choice in ["0", "exit", "quit"]:
            print("\nExiting simulation. Good luck with the project!\n")
            break
        elif user_choice == "all":
            update_variables_batch(params, labels)
        else:
            update_variables_targeted(user_choice, params, labels)


if __name__ == "__main__":
    main()