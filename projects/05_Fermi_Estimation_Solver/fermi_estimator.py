# ==========================================
# MODULE 1: CHICAGO PIANO TUNERS PROBLEM
# ==========================================

def calculate_piano_tuners(population, household_size, piano_pct, tunings_per_year, work_days, tunings_per_day):
    INSTITUTIONAL_PIANOS = 20000  # Estimated number of pianos in institutions (schools, churches, etc.)
    # 1. Total households
    households = population / household_size
    # 2. Pianos owned (% from households & est. 20,000 pianos from institutions) 
    total_pianos = households * (piano_pct / 100) + INSTITUTIONAL_PIANOS
    # 3. Total jobs per year
    total_tunings_needed = total_pianos * tunings_per_year
    # 4. Total jobs one tuner can do
    jobs_per_tuner = work_days * tunings_per_day
    
    # Avoid zero division if user plugs in wild values
    if jobs_per_tuner == 0: return 0
    
    # 5. Final tuners needed
    estimated_tuners = total_tunings_needed / jobs_per_tuner
    return int(estimated_tuners)

def run_piano_simulation():
    # Base defaults matching late 20th century Chicago bounds
    population = 3000000
    household_size = 3.0
    piano_pct = 5.0
    tunings_per_year = 1.0
    work_days = 200
    tunings_per_day = 3
    
    while True:
        estimated_tuners = calculate_piano_tuners(
            population, household_size, piano_pct, tunings_per_year, work_days, tunings_per_day
        )
        
        print("\n" + "="*50)
        print(" CHICAGO PIANO TUNERS ESTIMATOR:")
        print(f" 1. City Population:         {population:,} people")
        print(f" 2. Avg Household Size:      {household_size} people")
        print(f" 3. Households with Piano:   {piano_pct}%")
        print(f" 4. Tunings per Piano / Year: {tunings_per_year}")
        print(f" 5. Work Days per Year:      {work_days} days")
        print(f" 6. Tunings per Tuner / Day:  {tunings_per_day}")
        print("-"*50)
        print(f" Estimated Tuners Needed:    {estimated_tuners} professionals")
        print("="*50 + "\n")
        
        print("Enter (1-6) to adjust a variable, or '0' to return to Main Menu.")
        choice = input("Choice: ").strip()
        
        if choice == '0':
            break
        elif choice in ['1', '2', '3', '4', '5', '6']:
            try:
                new_val = float(input("Enter new positive value: "))
                if new_val <= 0:
                    print("Value must be positive.")
                    continue
                if choice == '1': population = int(new_val)
                elif choice == '2': household_size = new_val
                elif choice == '3': piano_pct = min(new_val, 100.0)
                elif choice == '4': tunings_per_year = new_val
                elif choice == '5': work_days = int(new_val)
                elif choice == '6': tunings_per_day = int(new_val)
            except ValueError:
                print("Invalid input format.")
        else:
            print("Invalid selection.")


# ==================================================
# MODULE 2: WEST BENGAL HARMONIUM TUNERS PROBLEM
# ==================================================

def calculate_harmonium_tuners(population, household_size, harmonium_pct, tunings_per_year, work_days, tunings_per_day):
    # 1. Total households
    households = population / household_size
    # 2. Harmoniums owned (% from households & 25% load factor for institutions)
    total_harmoniums = households * (harmonium_pct / 100) * 1.25
    # 3. Total jobs per year
    total_tunings_needed = total_harmoniums * tunings_per_year
    # 4. Total jobs one tuner can do
    jobs_per_tuner = work_days * tunings_per_day
    
    # Avoid zero division if user plugs in wild values
    if jobs_per_tuner == 0: return 0
    
    # 5. Final tuners needed
    estimated_tuners = total_tunings_needed / jobs_per_tuner
    return int(estimated_tuners)

def run_harmonium_simulation():
    # Base defaults matching current (2026) West Bengal bounds
    population = 100600000
    household_size = 4.5
    harmonium_pct = 5.0
    tunings_per_year = 0.36 # Weighted average: 80% of harmoniums (private) tuned once every 5 years, 20% (institutional) tuned once every year
    work_days = 250
    tunings_per_day = 6
    
    while True:
        estimated_tuners = calculate_harmonium_tuners(
            population, household_size, harmonium_pct, tunings_per_year, work_days, tunings_per_day
        )
        
        print("\n" + "="*50)
        print(" WEST BENGAL HARMONIUM TUNERS ESTIMATOR:")
        print(f" 1. State Population:         {population:,} people")
        print(f" 2. Avg Household Size:      {household_size} people")
        print(f" 3. Households with Harmonium:   {harmonium_pct}%")
        print(f" 4. Tunings per Harmonium / Year: {tunings_per_year}")
        print(f" 5. Work Days per Year:      {work_days} days")
        print(f" 6. Tunings per Tuner / Day:  {tunings_per_day}")
        print("-"*50)
        print(f" Estimated Tuners Needed:    {estimated_tuners} professionals")
        print("="*50 + "\n")
        
        print("Enter (1-6) to adjust a variable, or '0' to return to Main Menu.")
        choice = input("Choice: ").strip()
        
        if choice == '0':
            break
        elif choice in ['1', '2', '3', '4', '5', '6']:
            try:
                new_val = float(input("Enter new positive value: "))
                if new_val <= 0:
                    print("Value must be positive.")
                    continue
                if choice == '1': population = int(new_val)
                elif choice == '2': household_size = new_val
                elif choice == '3': harmonium_pct = min(new_val, 100.0)
                elif choice == '4': tunings_per_year = new_val
                elif choice == '5': work_days = int(new_val)
                elif choice == '6': tunings_per_day = int(new_val)
            except ValueError:
                print("Invalid input format.")
        else:
            print("Invalid selection.")


# ==========================================
# MODULE 3: WORLD'S TEXT PROBLEM
# ==========================================

def calculate_text_stack(population, phone_pct, texts_per_day, chars_per_text, sheets_per_cm):
    KM_TO_THE_MOON = 384000
    DAYS_PER_YEAR = 365
    CHARS_PER_PAGE = 3000
    active_users = population * (phone_pct / 100)
    texts_per_year = active_users * texts_per_day * DAYS_PER_YEAR
    total_chars = texts_per_year * chars_per_text
    total_pages = total_chars / CHARS_PER_PAGE

    cm_height = total_pages / sheets_per_cm
    meters_height = cm_height / 100
    km_height = meters_height / 1000
    pct_to_moon = (km_height / KM_TO_THE_MOON) * 100
    
    return km_height, pct_to_moon

def run_text_simulation():
    # Base defaults
    population = 8000000000
    phone_pct = 75.0
    texts_per_day = 50
    chars_per_text = 50
    sheets_per_cm = 100
    
    while True:
        km_height, pct_to_moon = calculate_text_stack(
            population, phone_pct, texts_per_day, chars_per_text, sheets_per_cm
        )
        
        print("\n" + "="*50)
        print(" WORLD'S TEXT ESTIMATOR:")
        print(f" 1. Global Population:       {population:,} people")
        print(f" 2. Has Mobile Phone:        {phone_pct}%")
        print(f" 3. Avg Texts Sent/Day:      {texts_per_day}")
        print(f" 4. Avg Characters/Text:     {chars_per_text}")
        print(f" 5. Paper Density (per cm):  {sheets_per_cm} sheets")
        print("-"*50)
        print(f" Total Stack Height:         {km_height:,.2f} km")
        print(f" Distance to Moon Achieved:  {pct_to_moon:.2f}%")
        print("="*50 + "\n")
        
        print("Enter (1-5) to adjust a variable, or '0' to return to Main Menu.")
        choice = input("Choice: ").strip()
        
        if choice == '0':
            break
        elif choice in ['1', '2', '3', '4', '5']:
            try:
                new_val = float(input("Enter new positive value: "))
                if new_val <= 0:
                    print("Value must be positive.")
                    continue
                if choice == '1': population = int(new_val)
                elif choice == '2': phone_pct = min(new_val, 100.0)
                elif choice == '3': texts_per_day = int(new_val)
                elif choice == '4': chars_per_text = int(new_val)
                elif choice == '5': sheets_per_cm = int(new_val)
            except ValueError:
                print("Invalid input format.")
        else:
            print("Invalid selection.")            



# ==========================================
# MAIN EXECUTION ROUTER
# ==========================================

def main():
    while True:
        print("\n" + "#"*40)
        print("   THE MULTI-FERMI ESTIMATION ENGINE   ")
        print("#"*40)
        print("Select a problem simulation to run:")
        print("1. The Chicago Piano Tuners Population")
        print("2. The West Bengal Harmonium Tuners Population")
        print("3. The World's Text Stack to the Moon")    
        print("0. Exit Engine")
        print("#"*40)
        
        menu_choice = input("Select option: ").strip()
        
        if menu_choice == '1':
            run_piano_simulation()
        elif menu_choice == '2':
            run_harmonium_simulation()
        elif menu_choice == '3':
            run_text_simulation()
        elif menu_choice == '0':
            print("\nShutting down calculation engine. Goodbye!")
            break
        else:
            print("\n[!] Please select a valid menu option (1, 2, 3, or 0).")

if __name__ == "__main__":
    main()            


