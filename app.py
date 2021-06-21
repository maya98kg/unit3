from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "Flowers don't growl"
    
    text = """It is a warm day and you are in the woods, getting some fresh air. All of a sudden, a man jumps out of the bushes.
    He starts telling you that he was picking flowers and he heard a growl. """

    choices = [
        ('listen',"Talk to him"),
        ('run_away',"Run away as fast as you can!!!")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices,picture_url="woods.jpg")



@app.route("/inside")
def listen():
    title = "You stay to hear the rest of the story..."
    
    text = """... and as he is talking, you notice that he has one hand in his pocket. You try to focus on his words, but 
    a bad feeling rises in your stomach. The only thing you hear from him is: 'You never know what day is going to be your last.'"""

    choices = [
        ('freeze',"You freeze"),
        ('run_away',"Try to escape from him")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices, picture_url="man.jpg")

@app.route("/escape")
def run_away():
    title = "You run away!"
    
    text = """You bolt away from the woods to safety.  You hear growls in the distance."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices,picture_url="survived.jpg")



@app.route("/stairs")
def freeze():
    title = "Look out!"
    
    text = """As you try to find the courage to escape him, you look at the pocket of his jacket and recognize the shape
    of a knife...
    Ooops... It is too late now."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices,picture_url="end.jpg")
