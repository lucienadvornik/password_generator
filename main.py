######################## PASSWORD GENERATOR - Requirements ######################## 
## 1. MAIN MENU
# -- Password generator --
# Choose option:
# 1. Generate password  
# 2. Exit the program 
# You chose:

# 1. --> Password Generator Procedure (below)
# 2. --> Farewell message: 'Bye!'
# 3. Entering wrong value --> 'Please enter a correct value'


# 2. PASSWORD GENERATION
# letters: a-z
# digits: 0-9
# special characters: !@#$%&*^|()_+

# Provide password lenght:
# Use uppercase letters? (y/n)
# Use digits? (y/n)
# Use special characters? (y/n)
# Your new password:

######################## PASSWORD GENERATOR - Solution ######################## 
import random # importing random madule for functions choice()

alpha_char = "abcdefghijklmnopqrstuvwxyz"
numerical_char = "0123456789"
special_char = "!@#$%&*^|()_+"


