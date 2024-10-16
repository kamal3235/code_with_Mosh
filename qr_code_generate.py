import qrcode


data = input('Enter the text or URL: ').strip()  # remove whitespace
filename = input('Enter the filename: ').strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f'QR code saved as {filename}')


# let now run the program
# Enter the text or URL:   >>address of the website<<
# Enter the Filename: say>> kamal.jpg
# it will show>> QR code saved as {filename}
# Now go to the code folder and find the file, you see the QR code
# scan the QR code, it will take you to the desired website
