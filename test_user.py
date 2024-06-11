from app import user

# Add a user
user.add_user("John Mwangi", "password123")

# Retrieve a user
user_data = user.get_user("John Mwangi")
print(user_data)  # Output: (1, 'john_doe', 'password123')
