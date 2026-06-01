email_address = input("Enter an email address (username@domain.com): ")

at_symbol_index = email_address.find('@')
dot_index = email_address.find('.', at_symbol_index)

username = email_address[:at_symbol_index]
domain_name = email_address[at_symbol_index + 1:dot_index]
extension = email_address[dot_index + 1:]

print("Username:", username)
print("Domain:", domain_name)
print("Extension:", extension)