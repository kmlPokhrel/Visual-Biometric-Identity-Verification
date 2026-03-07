from flask import Flask
from app.views import views_bp

app = Flask(__name__)

# Register the blueprint containing all your routes
app.register_blueprint(views_bp)

if __name__ == "__main__":
    app.run(debug=True)