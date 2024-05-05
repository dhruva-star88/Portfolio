import qrcode

image = qrcode.make("https://homepy-wc3lgal7qnjhnawdoxqz5i.streamlit.app/")

image.save("qr.png")
