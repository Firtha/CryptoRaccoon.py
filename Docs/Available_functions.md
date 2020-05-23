## Scoreboard

- Get the score of a given user
    -

## User management method: 

- Register a user
    - verify if the user is already registered Y/N
        - Yes -> throw error -> "user is already registered"
        - No -> register the give username

- update a username
    - verify if the username exist 
        - Yes -> update the username (oldusername, newusername)
        - No -> throw an error (This username doesn't exist)

2 mains functions : 
    + register_user:
    + update_username:

    + 2 logical functions:
        - 'get_numb_of_registered_users' : return int => get the numbers of users already registered
        -'is_valid_username' : return bool => verify if a username already exist