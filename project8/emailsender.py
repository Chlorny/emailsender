import smtplib

email = input("sender email: ")

receiver_email = input("receiver email: ")

subject = input("subject:")
message = input("message: ")

text = f"subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, "your code" )

server.sendmail(email, receiver_email, text)

print("email has been sent to" + receiver_email)