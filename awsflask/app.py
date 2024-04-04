from flask import Flask,render_template,Blueprint,request,redirect,url_for,send_file,send_from_directory
from flask_bootstrap import Bootstrap
from pytube import YouTube
import ssl
import os
import random

prevdir = os.getcwd() # 取得當前資料夾目錄

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template("index.html")

downlodaData = list()
@app.route('/page/downloadMp3.html', methods=["POST","GET"])
def downloadYoutubeMp3():
    ssl._create_default_https_context = ssl._create_stdlib_context    
    if request.method == 'POST':
        url = request.form['yturl']
        yt = YouTube(url)
        filename = f"{yt.author}_{yt.title}"
        downloadroot = request.form['downloadroot']  #r"C:\Users\j0989\OneDrive\桌面\下載1110"
        yt.streams.filter().get_audio_only().download(filename=f'{downloadroot}\{filename}.mp3')
        downlodaData.append([len(downlodaData),filename,url,yt.thumbnail_url])
        
        return render_template("/page/downloadMp3.html",downlodaData=downlodaData)
    else:
        return render_template("/page/downloadMp3.html",downlodaData=downlodaData)

eatData=["便當","滷肉飯","自助餐","乾麵","牛肉麵"
            ,"老麥","義大利麵","三明治","披薩"
            ,"咖哩飯","御飯糰","關東煮","烏龍麵","壽司"
            ,"微波食品","麵包","泡麵","小火鍋","蔬食料理"
            ]
@app.route('/page/eatWhat.html', methods=["POST","GET"])
def eatWhat():
    Ans=""
    if request.method == 'POST':
        Ans=eatData[random.randint(0,len(eatData))]
    return render_template("/page/eatWhat.html",Ans=Ans)



if __name__ == '__main__':
    from waitress import serve
    serve(app,host="0.0.0.0",port=8880)
    # app.run(host="0.0.0.0",port=8880 ,threaded=True)
