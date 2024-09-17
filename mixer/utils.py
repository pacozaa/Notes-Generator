def closest_divisible_number(X, Y):
    # Calculate the remainder when X is divided by Y
    remainder = X % Y
    
    # If the remainder is 0, X is already divisible by Y
    if remainder == 0:
        return X
    
    # Calculate the closest number less than or equal to X that is divisible by Y
    lower_closest = X - remainder
    
    return lower_closest