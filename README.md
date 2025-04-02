# FastAPI Game Assets API

## 1. Project Setup

### Prerequisites

- Python 3.11+
- MongoDB Atlas (or local MongoDB)
- Git

### Environment Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/Il-gabbu505/Database
   cd Database

   ```

2. Create and Activate a virtual environment
   python -m venv env
   env\Scripts\activate # Windows

3. Install Dependencies
   pip install -r requirements.txt

### Project Structure

Databases/
│── env/ # Virtual environment (ignored in Git)

│── main.py # FastAPI main app
│── requirements.txt # Project dependencies
│── README.md # Project documentation
│── .gitignore # Ignore unnecessary files

### API Documentation

The following application provides endpoints for managing game assets (audio and sprties) and players scores. It allows for uploading sprite images, audio files, and recording player scores in a database.

#### URL

- Development: http://127.0.0.1:8000
- Production: https://fastapidatabaseproject.vercel.app/

#### Endpoints

Endpoints: /upload_sprite /upload_audio /player_score
Method: POST

These endpoints allows users to upload sprites, audios and player score in the game.

Endpoints: /sprites /audio /scores
Method: GET

These endpoints allows users to retrieve sprites, audios and player score in the game.

Database Interaction:

- The endpoint saves the uploaded file to the storage location
- Creates a new record in the "sprites" and "audio" table with the file metadata.
- Stores: the players score and gets sorted by the highest score, the filename (ex audio files) etc and retieves it using GET
