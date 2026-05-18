from flask import Flask, request, jsonify

import psycopg2
from psycopg2.extras import RealDictCursor

import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
  conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
  return conn

def init_db():
  conn = get_db_connection()
  cur = conn.cursor()
  cur.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        content TEXT,
        created_at TIMESTAMP  DEFAULT  CURRENT_TIMESTAMP          
    )
  ''')
  conn.commit()
  cur.close()
  conn.close()

init_db()

@app.route('/notes', methods=['POST'])
def create_note():
  data = request.get_json()
  title = data.get('title')
  content = data.get('content')

  if not title:
    return jsonify({ "error" : "Title is required" }), 400
  
  conn = get_db_connection()
  cur = conn.cursor()
  cur.execute(
    'INSERT INTO notes (title, content) VALUES (%s, %s) RETURNING *',
    (title, content)
  )
  new_note = cur.fetchone()
  conn.commit()
  cur.close()
  conn.close()

  return jsonify(new_note), 201

@app.get('/notes')
def get_notes():
  conn = get_db_connection()
  cur = conn.cursor()
  cur.execute('SELECT * FROM notes ORDER BY created_at DESC')
  notes = cur.fetchall()
  cur.close()
  conn.close()

  return jsonify(notes), 200

@app.get('/notes/<int:note_id>')
def get_note(note_id):
  conn = get_db_connection()
  cur = conn.cursor()
  cur.execute('SELECT * FROM notes WHERE id = %s', (note_id,))
  note = cur.fetchone()
  cur.close()
  conn.close()

  if note is None:
    return jsonify({ "error" : "Note not found" }), 404

  return jsonify(note), 200

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    
    if not title:
        return jsonify({ "error" : "Title is required" }), 400
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'UPDATE notes SET title = %s, content = %s WHERE id = %s RETURNING *',
        (title, content, note_id)
    )
    updated_note = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    
    if updated_note is None:
        return jsonify({ "error" : "Note not found" }), 404
    
    return jsonify(updated_note), 200

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM notes WHERE id = %s RETURNING *', (note_id,))
    deleted_note = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    
    if deleted_note is None:
        return jsonify({ "error" : "Note not found" }), 404
    
    return jsonify({ "message" : "Note deleted successfully" }), 200