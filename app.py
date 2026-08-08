from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    # templatesフォルダ内の index.html を表示する
    return render_template('index.html')

if __name__ == '__main__':
    # 24時間公開を見据えるため、ローカルテスト時はポート等を指定可能にしておく
    app.run(debug=True, host='0.0.0.0', port=5000)
