from werkzeug.security import generate_password_hash, check_password_hash

print(generate_password_hash('eAlpha@123'))

stri = 'pbkdf2:sha256:150000$TatfzYoK$0f6588120124f54274ff3e3a1ea36c446f326ca0a57ca75351a82d00f2ce4eea'

print(check_password_hash(stri,'eAlpha@123'))