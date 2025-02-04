import qrcode

img = qrcode.make('https://kavithaharsha.netlify.app/')
img.save('mycode.png')