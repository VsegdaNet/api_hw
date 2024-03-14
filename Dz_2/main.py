from flask import Flask, redirect, render_template, request, url_for, make_response

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        log = ''
        name = request.form.get('name')
        if request.cookies.get('loggd'):
            log = request.cookies.get('loggd')

        res = make_response(f'logged: {log}, name: {name}')
        res.set_cookie(f"loggd, yes, name, {name}")
        print(name)
        return redirect(url_for('login'))
        
    
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login(): 
    if request.method == 'POST':
        return redirect(url_for('logout'))
    # name = request.cookies.get('name')
    print(request.cookies.get('name'))
    return render_template('login.html')

@app.route('/logout',methods=['GET', 'POST'])
def logout(): 
    if request.method == 'POST':
        return redirect(url_for('index'))
    res = make_response("<p>Вы больше не авторизованны</p>")
    res.set_cookie("loggd","")
    return render_template('logout.html')


if __name__ == "__main__":
    app.run(debug=True)