def delta_neutral(df):
    '''
    Delta near zero is better
    ShareValue
    Put value
    Call value
    '''
    call = [0, 1]
    put = [-1, 0]

    Hedge example
    portifolio = 200 shares. price = $100. delta = 1
    put_option_value = 110  =>  delta = -0.42. Cost=$0.91
    if price == 112:
        cost = $0.28
        delta = -0.16

    our delta = 2*1 = 2
    5*(put_option_value) =  => 5*-0.42 = -2.10
    final_delta = 2-2.1 = -0.1

    Situations:
    - Increase: 
        putoption_loss = $0.63 * 100 * 5 = 315
        shares = 200 * (112 - 110) = 400
        profit = 400 - 315 = 85
    - Falls:
        put_option_value = 2.14. delta = -0.73
        shares = 200*(98-100) = -400
        profit = 215
    # Straddle (Good for day trading)

    # Strangles

# Theta (time day)
# Gama





