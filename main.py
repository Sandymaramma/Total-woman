from Simple_Flask_App.__init__ import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
