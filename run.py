from market import app
from dotenv import load_dotenv

load_dotenv()
#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':

    app.run(debug=True, host='localhost', port=6060)