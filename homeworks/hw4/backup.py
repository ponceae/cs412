def construct_rocket_recursive(sections, desired_length):
    memo = [-1] * (desired_length + 1)
    memo[0] = 0
    
    def helper(length):
        if memo[length] != -1:
            return memo[length]
        else:
            min_sections = float('inf')
            for section in sections:
                if length >= section:
                    num_sections = 1 + helper(length - section)
                    min_sections = min(min_sections, num_sections)
            memo[length] = min_sections
            return min_sections
    
    min_sections = helper(desired_length)
    
    return min_sections