def repeat_caller(callers, k):
    '''
    Checks if repeat callers have occurred within 'k' positions
    If there is repeat callers within 'k' positions, then return True
    Otherwise False
    '''
    seen = {}

    for position, caller in enumerate(callers):
        if caller in seen and position - seen[caller] <= k:
            return True
        
        seen[caller] = position

    return False

