from LAL.app import app
from flask_cors import CORS
if __name__=='__main__':
    CORS(app)
    app.run(port=5002,debug=True)