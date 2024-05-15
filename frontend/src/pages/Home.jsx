import { useState, useEffect } from "react";
import api from "../api";
import Note from "../components/Note"

function Home() {
    const [notes, setNotes] = useState([]);
    const [content, setContent] = useState("");
    const [title, setTitle] = useState("");


    useEffect(() => {
        getNotes();
    }, []);

    const getNotes = () => {
        api
            .get("http://127.0.0.1:8000/api/notes/")
            .then((res) => res.data)
            .then((data) => {
                setNotes(data);
                console.log(data);
            })
            .catch((err) => alert(err));
    };


    const deleteNote = (id) => {
        api
            .delete(`http://127.0.0.1:8000/api/notes/${id}`)
            .then((res) => {
                if (res.status === 204) console.log(id + " Notes deleted");
                else alert("Failed to delete note.");
                getNotes();
            })
            .catch((error) => alert(error));
    };

    const createNote = (e) => {
        e.preventDefault();
        api
            .post("http://127.0.0.1:8000/api/notes/", { content, title })
            .then((res) => {
                if (res.status === 200) console.log("Note Has been created")
                else console.log("Failed to make note.");
                getNotes();
            })
            .catch((err) => alert(err));
    };

    return (
        <div>
            <div>
                <h2>Notes</h2>
                {notes.map((note) => (
                    <Note note={note} onDelete={deleteNote} key={note.id} />
                ))}
            </div>
            <div id="create-note-form">
            <h2>Create a Note</h2>
            <form onSubmit={createNote}>
                <label htmlFor="title">Title:</label>
                <br />
                <input
                    type="text"
                    id="title"
                    name="title"
                    required
                    onChange={(e) => setTitle(e.target.value)}
                    value={title}
                />
                <label htmlFor="content">Content:</label>
                <br />
                <textarea
                    id="content"
                    name="content"
                    required
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                ></textarea>
                <br />
                <input type="submit" value="Submit"></input>
            </form>
            </div>
        </div>
    );
}

export default Home;