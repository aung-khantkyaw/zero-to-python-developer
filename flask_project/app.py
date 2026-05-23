# from flask import Flask, request, jsonify

# import psycopg2
# from psycopg2.extras import RealDictCursor

# import os
# from dotenv import load_dotenv

# load_dotenv()

# app = Flask(__name__)

# DATABASE_URL = os.getenv("DATABASE_URL")

# def get_db_connection():
#   conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
#   return conn

# def init_db():
#   conn = get_db_connection()
#   cur = conn.cursor()
#   cur.execute('''
#     CREATE TABLE IF NOT EXISTS notes (
#         id SERIAL PRIMARY KEY,
#         title VARCHAR(255) NOT NULL,
#         content TEXT,
#         created_at TIMESTAMP  DEFAULT  CURRENT_TIMESTAMP          
#     )
#   ''')
#   conn.commit()
#   cur.close()
#   conn.close()

# init_db()

# @app.route('/notes', methods=['POST'])
# def create_note():
#   data = request.get_json()
#   title = data.get('title')
#   content = data.get('content')

#   if not title:
#     return jsonify({ "error" : "Title is required" }), 400
  
#   conn = get_db_connection()
#   cur = conn.cursor()
#   cur.execute(
#     'INSERT INTO notes (title, content) VALUES (%s, %s) RETURNING *',
#     (title, content)
#   )
#   new_note = cur.fetchone()
#   conn.commit()
#   cur.close()
#   conn.close()

#   return jsonify(new_note), 201

# @app.get('/notes')
# def get_notes():
#   conn = get_db_connection()
#   cur = conn.cursor()
#   cur.execute('SELECT * FROM notes ORDER BY created_at DESC')
#   notes = cur.fetchall()
#   cur.close()
#   conn.close()

#   return jsonify(notes), 200

# @app.get('/notes/<int:note_id>')
# def get_note(note_id):
#   conn = get_db_connection()
#   cur = conn.cursor()
#   cur.execute('SELECT * FROM notes WHERE id = %s', (note_id,))
#   note = cur.fetchone()
#   cur.close()
#   conn.close()

#   if note is None:
#     return jsonify({ "error" : "Note not found" }), 404

#   return jsonify(note), 200

# @app.route('/notes/<int:note_id>', methods=['PUT'])
# def update_note(note_id):
#     data = request.get_json()
#     title = data.get('title')
#     content = data.get('content')
    
#     if not title:
#         return jsonify({ "error" : "Title is required" }), 400
    
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute(
#         'UPDATE notes SET title = %s, content = %s WHERE id = %s RETURNING *',
#         (title, content, note_id)
#     )
#     updated_note = cur.fetchone()
#     conn.commit()
#     cur.close()
#     conn.close()
    
#     if updated_note is None:
#         return jsonify({ "error" : "Note not found" }), 404
    
#     return jsonify(updated_note), 200

# @app.route('/notes/<int:note_id>', methods=['DELETE'])
# def delete_note(note_id):
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute('DELETE FROM notes WHERE id = %s RETURNING *', (note_id,))
#     deleted_note = cur.fetchone()
#     conn.commit()
#     cur.close()
#     conn.close()
    
#     if deleted_note is None:
#         return jsonify({ "error" : "Note not found" }), 404
    
#     return jsonify({ "message" : "Note deleted successfully" }), 200



from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Note(db.Model):
  __tablename__ = 'notes'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), nullable=False)
  content = db.Column(db.Text, nullable=True)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)

  def to_dict(self):
    return{
      'id': self.id,
      'title': self.title,
      'content': self.content,
      'created_at': self.created_at.isoformat()
    }
  
with app.app_context():
  db.create_all()

# Frontend Route

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    title = request.form.get('title')
    content = request.form.get('content')
    if title:
      note = Note(title=title, content=content)
      db.session.add(note)
      db.session.commit()
    return redirect(url_for('index'))

  notes = Note.query.order_by(Note.created_at.desc()).all()
  return render_template('index.html', notes=notes)

@app.route('/note_edit/<:iintd>', methods=['GET', 'POST'])
def note_detail(id):
  note = Note.query.get_or_404(id, description=f"Note with id {id} not found.")
  
  if request.method == 'POST':
    note.title = request.form.get('title')
    note.content = request.form.get('content')
    db.session.commit()
    return redirect(url_for('index'))
    
  return render_template('edit.html', note=note)

@app.route('/note_delete/<int:id>', methods=['POST'])
def note_delete(id):
  note = Note.query.get_or_404(id, description=f"Note with id {id} not found.")
  db.session.delete(note)
  db.session.commit()
  return redirect(url_for('index'))

# API Endpoints

@app.route('/notes', methods=['GET'])
def get_notes():
  page = request.args.get('page', 1, type=int)
  per_page = request.args.get('per_page', 10, type=int)

  notes = Note.query.order_by(Note.created_at.asc()).paginate(
    page=page, per_page=per_page, error_out=False
  )
  # return jsonify([note.to_dict() for note in notes]), 200

  return jsonify({
    'notes': [note.to_dict() for note in notes.items],
    'total': notes.total,
    'pages': notes.pages,
    'current_page': notes.page
  }), 200

@app.route('/notes/<int:id>', methods=['GET'])
def get_note(id):
  note = Note.query.get_or_404(id, description=f"Note with id {id} not found.")
  return jsonify(note.to_dict()), 200

@app.route('/notes', methods=['POST'])
def create_note():
  data = request.get_json()
  title = data.get('title')
  content = data.get('content')

  if not title:
    return jsonify({ "error" : "Title is required" }), 400

  note = Note(title=title, content=content)
  db.session.add(note)
  db.session.commit()

  return jsonify(note.to_dict()), 201

@app.route('/notes/<int:id>', methods=['PUT'])
def update_note(id):
  note = Note.query.get_or_404(id, description=f"Note with id {id} not found.")
  data = request.get_json()
  title = data.get('title')
  content = data.get('content')

  if not title:
    return jsonify({ "error" : "Title is required" }), 400

  note.title = title
  note.content = content
  db.session.commit()

  return jsonify(note.to_dict()), 200

@app.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
  note = Note.query.get_or_404(id, description=f"Note with id {id} not found.")
  db.session.delete(note)
  db.session.commit()

  return jsonify({ "message" : "Note deleted successfully" }), 200

if __name__ == '__main__':
  app.run(debug=True)