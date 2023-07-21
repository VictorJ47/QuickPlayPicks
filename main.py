from website import create_app

app = create_app()

if __name__ == '__main__': #runs website only when this file runs
    app.run(debug = True)