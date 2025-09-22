import os
import time
from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app) # Enable Cross-Origin Resource Sharing

def get_db_connection():
    """Establishes a connection to the PostgreSQL database."""
    while True:
        try:
            conn = psycopg2.connect(
                host="db", # The service name of the database in docker-compose.yml
                dbname=os.environ.get("POSTGRES_DB"),
                user=os.environ.get("POSTGRES_USER"),
                password=os.environ.get("POSTGRES_PASSWORD"),
                port=5432
            )
            return conn
        except psycopg2.OperationalError as e:
            print(f"Could not connect to database, retrying... Error: {e}")
            time.sleep(1)

@app.route('/poll', methods=['GET'])
def get_poll_data():
    """Returns the current poll options and their vote counts."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT option_key, votes FROM poll_votes ORDER BY id;")
    poll_data = {key: votes for key, votes in cur.fetchall()}
    cur.close()
    conn.close()
    return jsonify(poll_data)

@app.route('/vote', methods=['POST'])
def vote():
    """Increments the vote count for a given option."""
    data = request.get_json()
    vote_option = data.get('vote')
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE poll_votes SET votes = votes + 1 WHERE option_key = %s;", (vote_option,))
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({"status": "success", "message": f"Voted for {vote_option}"})

if __name__ == "__main__":
    # Create the table and initialize data on first run
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS poll_votes (
            id SERIAL PRIMARY KEY,
            option_key VARCHAR(50) UNIQUE NOT NULL,
            votes INTEGER NOT NULL DEFAULT 0
        );
    """)
    cur.execute("INSERT INTO poll_votes (option_key) VALUES ('python'), ('javascript'), ('go'), ('rust') ON CONFLICT (option_key) DO NOTHING;")
    conn.commit()
    cur.close()
    conn.close()
    
    app.run(host='0.0.0.0', port=5001)
