from netmiko import ConnectHandler
cisco = {
    'device_type': 'cisco_ios',
    'host': 'EB71NSLB',
    'username': 'DM088934',
    'password': 'Winter@231095'
}
net_connect = ConnectHandler(**cisco)
output = net_connect.send_command('show ip int brief vrf all')
print (output)