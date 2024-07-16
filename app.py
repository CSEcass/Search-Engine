from flask import Flask,render_template,request,url_for
import random 

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>hello world</h1> \n <p>this is a paragraph</p>'

@app.route('/1')
def linkpage():
    return render_template('File.html')


@app.route('/gifs')
def gifs():
    myGifs = [
        'https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWM1NDcxN3BsNnhvcGJmd3hkZ2EyaW1taTByem5wMW9hanFlamY5bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/rO6ksLrUA4ppMhTrTy/giphy.gif'
        'https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2w1amtocXlpZjJheXhzOTB4Ym02eXRxN3IyMHU3czEzaGlwdTRicSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LNi7dYTkb2UVC2aFeW/giphy.gif'
        'https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzcwaDd0bzk4OGY5dHA3cWt4a245djJscTI1cnF1YjgxbDB1OTJuOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HRcrkku2LooE89h4hy/giphy.gif'
    ]
    randomGif = random.choice(myGifs)
    return render_template('File.html', random=randomGif, randomBool=False, myGifs=myGifs)

@app.route('/input', methods=['GET','POST'])
def input():
    imgData = {
        'Dogs' : ['https://i.natgeofe.com/n/4f5aaece-3300-41a4-b2a8-ed2708a0a27c/domestic-dog_thumb_3x2.jpg',
                 'https://thumbor.forbes.com/thumbor/fit-in/900x510/https://www.forbes.com/advisor/wp-content/uploads/2023/07/top-20-small-dog-breeds.jpeg.jpg',
                 'https://www.akc.org/wp-content/uploads/2018/05/Three-Australian-Shepherd-puppies-sitting-in-a-field.jpg'
                 ],
        'Snails' : ['https://cdn.hswstatic.com/gif/snail-shell.jpg',
                    'https://images.saymedia-content.com/.image/t_share/MTk3NjU5MTcyNTc2MjQwOTQx/gardeners-may-kill-snails-but-some-people-eat-them.jpg'],
        'Dots' : ['https://as1.ftcdn.net/v2/jpg/05/01/68/80/1000_F_501688015_gPbBAf7F5EM33YEKbqfyMbqT1Gaa0zn3.jpg',
                  'https://i.pinimg.com/564x/e9/5c/03/e95c038308906782fb6b0e605de9cb1b.jpg',
                  'https://static.vecteezy.com/system/resources/thumbnails/011/080/544/small/dotted-halftone-seamless-pattern-vector.jpg',
                  ]
    }

    if request.method == 'POST':
        query = request.form['query']
        if query not in imgData:
            return "no data found for " + query
        return render_template('input.html', imgData=imgData[query])
    
    return render_template('input.html', url=url_for('input'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)