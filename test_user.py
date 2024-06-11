from user import User

# Add a user
user.add_user("admin", ".")

# Retrieve a user
user_data = user.get_user("John Mwangi")
print(user_data)  # Output: (1, 'john_doe', 'password123')
