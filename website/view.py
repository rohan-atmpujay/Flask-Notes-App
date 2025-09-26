from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, db

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        
        if not note or len(note.strip()) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category='success')
    
    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    data = request.get_json()
    noteId = data.get('noteId')
    note = Note.query.get(noteId)

    if note and note.user_id == current_user.id:
        db.session.delete(note)
        db.session.commit()
        return jsonify({"success": True})

    return jsonify({"success": False}), 400
