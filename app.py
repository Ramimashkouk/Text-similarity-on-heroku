import os
from flask import Flask, render_template, request
from TextSimModule import text_similarity
from time import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        text1 = request.form['text1']
        text2 = request.form['text2']
        if text1 == '' or text2 == '':
            return render_template('index.html', message='Please enter both texts')

        start_time = time()

        documents = [text1, text2]
        x= text_similarity(documents)

        passed_time = (time() - start_time)
    
        return(f'''<html>
                        <body>
                            <p>The cosine similarity is {x}%</p>
                            <p>The passed time is {passed_time} seconds</p>
                            <p><a href="/">Click here to compare again</a>
                        </body>
                    </html>''')



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
