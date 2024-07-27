from flask import Flask, render_template_string
import random

app = Flask(__name__)

@app.route('/')
def generate_loto():
    # Génère une liste de nombres de 1 à 49
    numbers = list(range(1, 50))
    random.shuffle(numbers)
    selected_numbers = numbers[:10]

    # Modèle HTML pour afficher les numéros sélectionnés
    html_template = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Résultats du Loto</title>
    </head>
    <body>
        <h1>Les numéros de loto sélectionnés sont :</h1>
        <ul>
            {% for number in numbers %}
                <li>{{ number }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """

    return render_template_string(html_template, numbers=selected_numbers)

if __name__ == '__main__':
    app.run(debug=True)
