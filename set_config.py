# Importing a library
from netmiko import ConnectHandler

# Create a dictionary representing the device
device = {
    'device_type': 'cisco_xe',
    'host':   '10.10.20.48',
    'username': 'developer',
    'password': 'C1sco12345',
    'port' : 22
}


# Execute configuration change commands (will automatically enter into config mode)
config_commands = [
    'interface loopback10',
    'no shut'
]

# Establish an SSH connection to the device by passing in the device dictionary
net_connect = ConnectHandler(**device)


# send_command for commands in exec mode
output = net_connect.send_command('show ip int br')


# send_config_set for commands in config mode
#output = net_connect.send_config_set(config_commands)

# Print output commands
print(output)
