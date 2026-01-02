import qrcode

# Taking UPI ID as an input
upi_id = input("Enter your UPI ID: ")

# Payement URI = upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# Defining Payment URL based on the UPI ID and the payement app
# You can modify these urls based on the payement apps you want to support

phonepe_url = f"upi://pay?pa={upi_id}&pn=Reciepient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Reciepient%20Name&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn=Reciepient%20Name&mc=1234"

# Create QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save the QR Code to image file (optional)
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_qr.png")

# Display the QR Codes (you may need to install PIL/Pillow Library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

