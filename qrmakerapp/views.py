from django.shortcuts import render
from .forms import CustomForm  # Import your form from forms.py
import qrcode
from PIL import Image


def helloworld(request):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            custom_data = form.cleaned_data['custom_field']
            # Process the custom input data
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border=4)
            qr.add_data(custom_data)
            qr.make(fit=True)
            img= qr.make_image(fill_color="black",back_color="#f4f4f4")
            image_path = 'qrmakerapp/static/img/qrcode.png'
            # Save the QR code image to the static directory
            with open(image_path, 'wb') as qr_file:
                img.save(qr_file)
                # Redirect or render success page
            return render(request, 'home.html', {'form': form})
    else:
        form = CustomForm()
    
    return render(request, 'home.html', {'form': form})
