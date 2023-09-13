from flask import Flask, render_template, url_for

def create_app() :

    app = Flask(__name__)

    @app.route("/")
    def index() :

        projects = [
            {
                "title": "Portafolio Web",
                "img": "img/header.jpg",
                "desc": "Una pequeña descripción del proyecto y las tecnologías que se ocuparon para su desarrollo",
                "skills": ["HTML", "CSS", "JavaScript", "Flask"],
                "repo": "link-del-repositorio",
                "demo": "link-de-la-demo"
            },
            {
                "title": "Otro trabajo",
                "img": "img/header.jpg",
                "desc": "Otro ejemplo de otro trabajo xd",
                "skills": ["Bootstrap", "Django", "MySQL"],
                "repo": "link-del-repositorio",
                "demo": "link-de-la-demo"
            },
            {
                "title": "Otro trabajo mas xddd",
                "img": "img/header.jpg",
                "desc": "Aqui ya no se que poner",
                "skills": ["lenguaje", "dee", "programming"],
                "repo": "link-del-repositorio",
                "demo": "link-de-la-demo"
            }
        ]

        return render_template("index.html",
                               projects = projects)
    return app



