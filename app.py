from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

# Konfigurasi session Flask
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'your_secret_key'
Session(app)

title = "G++ Based on Calculator v2"

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    # Inisialisasi variabel dalam session jika belum ada
    if 'right1' not in session:
        session['right1'] = 1
        session['right2'] = 1
        session['left1'] = 1
        session['left2'] = 1
        
    


    # Ambil nilai dari session
    right1 = session['right1']
    right2 = session['right2']
    left1 = session['left1']
    left2 = session['left2']

    if request.method == 'POST':    
        if 'reset' in request.form:
            # Reset semua nilai ke kondisi awal
            session['right1'] = 1
            session['right2'] = 1
            session['left1'] = 1
            session['left2'] = 1
            return render_template('index.html', title=title, right1=1, right2=1, left1=1, left2=1)
        
    
        # Ambil input dari form
        plus1 = int(request.form.get('plus1', 0) or 0)
        plus2 = int(request.form.get('plus2', 0) or 0)
        
        hand1 = request.form.get('hand1', "").lower()
        hand2 = request.form.get('hand2', "").lower()
        
        yhhand1 = request.form.get('yhhand1', "").lower()
        yhhand2 = request.form.get('yhhand2', "").lower()
        
        right1 = int(request.form.get('right1', session['right1']) or session['right1'])
        left1 = int(request.form.get('left1', session['left1']) or session['left1'])
        right2 = int(request.form.get('right2', session['right2']) or session['right2'])
        left2 = int(request.form.get('left2', session['left2']) or session['left2'])
        
        print("plus1:", plus1, "plus2:", plus2)  # Debug: Cek nilai input

        print("Session values:", session)
        print("Form inputs:", request.form)
        

            
        # Player 1 memberikan ke Player 2
        # kosong
        if plus1 is None or plus1 == '':
            return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
        
        # right right
        if plus1 == 1 and hand1 == "right" and yhhand1 == "right":
            if right1 != 0:  # Pastikan ada nilai untuk diberikan
                right2 += 1
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
        if plus1 == 2 and hand1 == "right" and yhhand1 == "right":
            if right1 > 1:  # Pastikan ada nilai untuk diberikan
                right2 += 2
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
        if plus1 == 3 and hand1 == "right" and yhhand1 == "right":
            if right1 > 2:  # Pastikan ada nilai untuk diberikan
                right2 += 3
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
                
        if plus1 == 4 and hand1 == "right" and yhhand1 == "right":
            if right1 > 3:  # Pastikan ada nilai untuk diberikan
                right2 += 4
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            


            
        # left right
        
        if plus1 == 1 and hand1 == "left" and yhhand1 == "right":
            if right1 > 0:  # Pastikan ada nilai untuk diberikan
                left2 += 1
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
        if plus1 == 2 and hand1 == "left" and yhhand1 == "right":
            if right1 > 1:  # Pastikan ada nilai untuk diberikan
                left2 += 2
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
        if plus1 == 3 and hand1 == "left" and yhhand1 == "right":
            if right1 > 2:  # Pastikan ada nilai untuk diberikan
                left2 += 3
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
                
        if plus1 == 4 and hand1 == "left" and yhhand1 == "right":
            if right1 > 3:  # Pastikan ada nilai untuk diberikan
                left2 += 4
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
        

            
        # right left
        
        if plus1 == 1 and hand1 == "right" and yhhand1 == "left":
            if left1 > 0:  # Pastikan ada nilai untuk diberikan
                right2 += 1
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
        if plus1 == 2 and hand1 == "right" and yhhand1 == "left":
            if left1 > 1:  # Pastikan ada nilai untuk diberikan
                right2 += 2
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
        if plus1 == 3 and hand1 == "right" and yhhand1 == "left":
            if left1 > 2:  # Pastikan ada nilai untuk diberikan
                right2 += 3
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
                
        if plus1 == 4 and hand1 == "right" and yhhand1 == "left":
            if left1 > 3:  # Pastikan ada nilai untuk diberikan
                right2 += 4
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
            # left left
        
        if plus1 == 1 and hand1 == "left" and yhhand1 == "left":
            if left1 > 0:  # Pastikan ada nilai untuk diberikan
                left2 += 1
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
        if plus1 == 2 and hand1 == "left" and yhhand1 == "left":
            if left1 > 1:  # Pastikan ada nilai untuk diberikan
                left2 += 2
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
        if plus1 == 3 and hand1 == "left" and yhhand1 == "left":
            if left1 > 2:  # Pastikan ada nilai untuk diberikan
                left2 += 3
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
                
        if plus1 == 4 and hand1 == "left" and yhhand1 == "left":
            if left1 > 3:  # Pastikan ada nilai untuk diberikan
                left2 += 4
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)



        # Player 2 memberikan ke Player 1
        # kosong
        if plus2 is None or plus2 == '':
            return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)


        
        # right right
        if plus2 == 1 and hand2 == "right" and yhhand2 == "right":
            if right2 > 0:  # Pastikan ada nilai untuk diberikan
                right1 += 1
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
        if plus2 == 2 and hand2 == "right" and yhhand2 == "right":
            if right2 > 1:  # Pastikan ada nilai untuk diberikan
                right1 += 2
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
        if plus2 == 3 and hand2 == "right" and yhhand2 == "right":
            if right2 > 2:  # Pastikan ada nilai untuk diberikan
                right1 += 3
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
                
        if plus2 == 4 and hand2 == "right" and yhhand2 == "right":
            if right2 > 3:  # Pastikan ada nilai untuk diberikan
                right1 += 4
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
            
        # left right
        
        if plus2 == 1 and hand2 == "left" and yhhand2 == "right":
            if right2 > 0:  # Pastikan ada nilai untuk diberikan
                left1 += 1
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
        if plus2 == 2 and hand2 == "left" and yhhand2 == "right":
            if right2 > 1:  # Pastikan ada nilai untuk diberikan
                left1 += 2
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
        if plus2 == 3 and hand2 == "left" and yhhand2 == "right":
            if right2 > 2:  # Pastikan ada nilai untuk diberikan
                left1 += 3
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
                
        if plus2 == 4 and hand2 == "left" and yhhand2 == "right":
            if right2 > 3:  # Pastikan ada nilai untuk diberikan
                left1 += 4
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
            
        # right left
        
        if plus2 == '1' and hand2 == "right" and yhhand2 == "left":
            if left2 > 0:  # Pastikan ada nilai untuk diberikan
                right1 += 1
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
        if plus2 == '2' and hand2 == "right" and yhhand2 == "left":
            if left2 > 1:  # Pastikan ada nilai untuk diberikan
                right1 += 2
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
        if plus2 == '3' and hand2 == "right" and yhhand2 == "left":
            if left2 > 2:  # Pastikan ada nilai untuk diberikan
                right1 += 3
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
                
        if plus2 == '4' and hand2 == "right" and yhhand2 == "left":
            if left2 > 3:  # Pastikan ada nilai untuk diberikan
                right1 += 4
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
            # left left
        
        if plus2 == '1' and hand2 == "left" and yhhand2 == "left":
            if left2 > 0:  # Pastikan ada nilai untuk diberikan
                left1 += 1
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
        if plus2 == '2' and hand2 == "left" and yhhand2 == "left":
            if left2 > 1:  # Pastikan ada nilai untuk diberikan
                left1 += 2
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
        if plus2 == '3' and hand2 == "left" and yhhand2 == "left":
            if left2 > 2:  # Pastikan ada nilai untuk diberikan
                left1 += 3
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
                
        if plus2 == '4' and hand2 == "left" and yhhand2 == "left":
            if left2 > 3:  # Pastikan ada nilai untuk diberikan
                left1 += 4
            else :
                return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
            
        if right1 > 4:
            right1 = 0
            session['right1'] = right1  # Simpan ke session
        
        if left1 > 4:
            left1 = 0
            session['left1'] = left1  # Simpan ke session

        if right2 > 4:
            right2 = 0
            session['right2'] = right2  # Simpan ke session
            
        if left2 > 4:
            left2 = 0
            session['left2'] = left2  # Simpan ke session

        # Simpan kembali nilai variabel ke session
        session['right1'] = right1
        session['right2'] = right2
        session['left1'] = left1
        session['left2'] = left2
        
    return render_template('index.html', title=title, right1=right1, right2=right2, left1=left1, left2=left2)
