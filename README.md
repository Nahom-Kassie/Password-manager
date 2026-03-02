🔐 Python CSV Password Vault
A lightweight command-line utility for managing and storing digital credentials locally using structured CSV storage.

Key Features
Master Password Security: Protects the vault with a master key and a 5-attempt lockout mechanism to prevent unauthorized access.

Persistent Storage: Utilizes the csv module to store data in a human-readable password.csv file.

Smart Search: The view() function allows for targeted retrieval of passwords based on specific usernames and platforms.

Full Audit Report: Includes a reporting feature to list every account currently stored in the database.

Dynamic Updates: Users can update their master password during an active session.