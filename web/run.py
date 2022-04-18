import os

from dotenv import load_dotenv
from market import app

load_dotenv()
# Run this command to run the application in DEBUG mode.
# docker run -p 6060:6060 -e DEBUG=1 <image-name>

# Checks if the run.py file has executed directly and not imported
if __name__ == "__main__":

    app.run(host="0.0.0.0", port=6060, debug=os.environ.get("DEBUG", 1))
