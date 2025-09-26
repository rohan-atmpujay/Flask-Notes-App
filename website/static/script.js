function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.success) {
            const noteElement = document.getElementById("note-" + noteId);
            if (noteElement) {
                noteElement.remove();
            }
        } else {
            alert("Failed to delete note.");
        }
    });
}
