"""
User can manage their setting such as:
-Theme
-Language
-Notification

Also adding a function to add, update, delete, and view those user setting
"""

# Adding a new setting to test setting configuration
def add_setting(setting_list, key_value_tupple) -> str:
    # convert tuple into key-value pairs
    key, value = key_value_case(key_value_tupple)

    # checking if key has the same value on the setting list
    if key_exist(setting_list, key):
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    setting_list.update({f"{key}": f"{value}"}) 
    return f"Setting '{key}' added with value '{value}' successfully!"


# Updating a setting from the test setting configuration
def update_setting(setting_list, key_value_tupple) -> str:
    # convert tuple into key-value pairs
    key, value = key_value_case(key_value_tupple)

    # checking if key has the same value on the setting list
    if not key_exist(setting_list, key):
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."    
    
    # Updating the setting
    setting_list.update({f"{key}": f"{value}"}) 
    return f"Setting '{key}' updated to '{value}' successfully!"


# Deletting a setting from the setting configuration
def delete_setting(setting_list, key):
    key = key.lower().strip()

    # checking setting existence and delete if exist
    if not key_exist(setting_list, key):
        return f"Setting not found!"
    
    del setting_list[f"{key}"]
    return f"Setting '{key}' deleted successfully!"


# Displaying the configuration setting
def view_settings(setting_list):
    # list empty
    if not setting_list:
        return "No settings available."
    
    # display
    display = "Current User Settings:\n"
    for key, value in setting_list.items():
        display += f"{key.capitalize()}: {value}\n"
    
    return display


# Convert the key-value tupple case
def key_value_case(key_value_tupple):
    # convert key-value pairs letter case
    key, value = key_value_tupple
    key = key.lower().strip()
    value = value.lower().strip()
    # return new key-value tupple
    return (key, value)

# Checking if key value exist within dictionaries
def key_exist(setting_list, key):
    for setting in setting_list:
        if setting == key:
            return True

    return False


# Test_settings
test_settings = {
    "theme": "dark",
    "notification": "enabled",
    "volume": "high"
}

print(add_setting({'theme': 'light'}, ('THEME', 'dark')))
print(update_setting({'theme': 'light'}, ('theme', 'dark')))
print()
print(view_settings(test_settings))
