# Make ways Ten Rupee Coins
#Define Functions
def get_combinations(target_amount):
#Get 10 Rupee Combination
    for ten in range(int(target_amount/10) + 1):
#Get 5 Rupee Combination
        for five in range(int((target_amount - 10*ten)/5) + 1):
#Get 2 Rupee Combination
            for two in range(int((target_amount - 10*ten - 5*five)/2) + 1):

                if 10*ten + 5*five + 2*two == target_amount:

                    print(f" {ten} x 10 rupee notes, {five} x 5 rupee notes, {two} x 2 rupee notes") 



get_combinations(10) 