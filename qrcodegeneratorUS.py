import qrcode

def generate_qrcode(content, file_name):
    """
    Generates a QR Code with the specified content and saves it as an image file.
    :param content: Text or URL to include in the QR Code.
    :param file_name: Name of the image file where the QR Code will be saved.
    """
    # QR Code settings
    qr = qrcode.QRCode(
        version=1,  # QR Code size control (1 to 40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each "box" in the QR Code
        border=4,  # Border size (minimum of 4)
    )
    qr.add_data(content)
    qr.make(fit=True)

    # Create the image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR Code to the specified file
    img.save(file_name)
    print(f"QR Code generated and saved as {file_name}.")

# Example usage
content = "https://www.python.org"  # Can be any text or URL
file_name = "qrcode_python.png"
generate_qrcode(content, file_name)
