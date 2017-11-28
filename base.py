from flask import Flask, session, render_template, request, flash, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():
    # return HTML
    # return "<h1>this is the home page!<h1>"
    return render_template('home-base.html')


@app.route('/members')
def show_all_members():
    # return "<h2>this is the page for all members</h2>"
    return render_template('member-all.html')


# https://goo.gl/Pc39w8 explains the following line
if __name__ == '__main__':

    # activates the debugger and the reloader during development
    # app.run(debug=True)
    app.run()

    # make the server publicly available on port 80
    # note that Ports below 1024 can be opened only by root
    # you need to use sudo for the following conmmand
    # app.run(host='0.0.0.0', port=80)
