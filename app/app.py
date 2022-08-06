#app.py was replaced by --init__.py to be called from manage.py
#kept both files and they have a small difference on create app

from flask import Flask, appcontext_popped, render_template
from flask_navigation import Navigation
#from flask_collect import Collect
from flask_bootstrap import Bootstrap

def create_app(config):
  app = Flask(__name__)
  #app = Flask('app')
  app.config.from_object(config)
  
  Bootstrap(app)
  Collect(app)

  @app.route('/')
  def home():
    return render_template('index.html')

  @app.route("/privacypolicy.html")
  def privacypolicy():
        return render_template('privacypolicy.html')

  @app.route("/jobs.html")
  def jobs():
        return render_template('jobs.html')    

  return app

if __name__ == "__main__":
   app.run(debug=True) 

 