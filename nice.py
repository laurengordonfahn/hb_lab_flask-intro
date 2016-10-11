from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page.<html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
    
    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1><a href= "/" >Hi There!</a></h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          Select a compliment:
          <select name = "compliment"> 
            <option value = 'awesome'> awesome </option>
            <option value = 'terrific'> terrific </option>
            <option value = 'fantastic'> fantastic </option>
            <option value = 'neato'> neato </option>
            <option value = 'fantabulous'>fantabulous </option>
            <option value = 'wowza'> wowza </option>
            <option value = 'oh-so-not-meh'>oh-so-not-meh </option>
            <option value = 'brilliant'> brilliant </option>
            <option value = 'ducky'> ducky </option>
            <option value = 'coolio'> coolio </option>
            <option value = 'incredible'>incredible </option>
            <option value = 'wonderful'> wonderful </option>
            <option value = 'smashing'> smashing </option>
            <option value = 'lovely'> lovely </option>
          </select>
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    chosen_compliment = request.args.get("compliment")
    compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, chosen_compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
