# Model UN Hub
This overall project is a hub that can be used for Model UN conferences. This specific project is the server to accompany the UI found [here](https://github.com/Marinara-Sauce/mun-hub-ui).

# Features
As stated above, this project is the API and Database for the UI. This project uses Python, implementing the FastAPI library and SQLAcademy. This is made to be a "plug in play" solution, where users can simply run the program without the need to start and configure any database servers. By simply running the app, the program will create a new file which serves as the database.

# Running the Program
## Running Locally
Firstly, the program must have a database to connect to. The API uses Postgres. You can launch a pre-configured container with `docker-compose up db -d`.

To run the program locally, ensure you have Python 3.9 or greater installed. Then, run `pip install -r requirements.txt` to download the dependencies. Once the depenencies are installed, run the command `uvicorn main:app` to host the server. The server will run on port 8000 by default.

## Running Containerized
This is the best way to run the project. Ensure docker and docker-compose is installed, then simply run `docker-compose up --build -d` to start the server and the database.