import instaloader

# List of usernames to fetch follower counts for
usernames = ["kranthi_vlogger", "hiteshchoudharyofficial", "pawankalyan"]

# Create an instance of Instaloader class
loader = instaloader.Instaloader()

# Iterate through the list of usernames
for username in usernames:
    try:
        # Load the profile using its username
        profile = instaloader.Profile.from_username(loader.context, username)

        # Print the username and follower count
        print(f"Username: {username}, Followers: {profile.followers}")
    except Exception as e:
        print(f"Error fetching follower count for {username}: {e}")
