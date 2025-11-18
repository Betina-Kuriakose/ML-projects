import React, { useEffect, useState } from 'react';
import {
  BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer,
} from 'recharts';

function App() {
  const [students, setStudents] = useState([]);
  const [newStudent, setNewStudent] = useState({
    name: '',
    age: '',
    class: '',
    marks: { math: '', science: '', english: '' },
  });
  const [updateAge, setUpdateAge] = useState({ id: '', age: '' });

  const apiUrl = 'http://localhost:5000';

  // Fetch students from backend
  const fetchStudents = async () => {
    const res = await fetch(`${apiUrl}/students`);
    const data = await res.json();
    setStudents(data);
  };

  useEffect(() => {
    fetchStudents();
  }, []);

  // Calculate CGPA = average marks / 10 (simple example)
  const calculateCgpa = (marks) => {
    if (!marks) return 0;
    const values = Object.values(marks).map(Number);
    if (values.some(isNaN)) return 0;
    const avg = values.reduce((a, b) => a + b, 0) / values.length;
    return (avg / 10).toFixed(2);
  };

  // Handle new student form input change
  const handleNewStudentChange = e => {
    const { name, value } = e.target;
    if (['math', 'science', 'english'].includes(name)) {
      setNewStudent(prev => ({
        ...prev,
        marks: { ...prev.marks, [name]: value },
      }));
    } else {
      setNewStudent(prev => ({
        ...prev,
        [name]: value,
      }));
    }
  };

  // Add new student
  const handleAddStudent = async e => {
    e.preventDefault();

    // Validate fields
    if (!newStudent.name || !newStudent.age || !newStudent.class) {
      alert('Please fill name, age, and class');
      return;
    }
    if (
      !newStudent.marks.math || !newStudent.marks.science || !newStudent.marks.english
    ) {
      alert('Please fill marks for all subjects');
      return;
    }

    const studentToSend = {
      name: newStudent.name,
      age: parseInt(newStudent.age),
      class: newStudent.class,
      marks: {
        math: Number(newStudent.marks.math),
        science: Number(newStudent.marks.science),
        english: Number(newStudent.marks.english),
      },
    };

    await fetch(`${apiUrl}/students`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(studentToSend),
    });
    setNewStudent({ name: '', age: '', class: '', marks: { math: '', science: '', english: '' } });
    fetchStudents();
  };

  // Handle update age form input
  const handleUpdateAgeChange = e => {
    setUpdateAge({ ...updateAge, [e.target.name]: e.target.value });
  };

  // Update student age
  const handleUpdateStudent = async e => {
    e.preventDefault();
    if (!updateAge.id || !updateAge.age) {
      alert('Please fill both fields');
      return;
    }

    await fetch(`${apiUrl}/students/${updateAge.id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ age: parseInt(updateAge.age) }),
    });
    setUpdateAge({ id: '', age: '' });
    fetchStudents();
  };

  return (
    <div style={{ padding: 20, maxWidth: 700, margin: 'auto' }}>
      <h1>Student Progress Tracker</h1>

      <h2>Students List</h2>
      <ul>
        {students.map(s => (
          <li key={s._id}>
            <strong>{s.name}</strong> — Age: {s.age} — Class: {s.class} — CGPA: {calculateCgpa(s.marks)}
          </li>
        ))}
      </ul>

      <h2>Add New Student</h2>
      <form onSubmit={handleAddStudent}>
        <input
          name="name"
          placeholder="Name"
          value={newStudent.name}
          onChange={handleNewStudentChange}
        />
        <input
          name="age"
          type="number"
          placeholder="Age"
          value={newStudent.age}
          onChange={handleNewStudentChange}
        />
        <input
          name="class"
          placeholder="Class"
          value={newStudent.class}
          onChange={handleNewStudentChange}
        />
        <input
          name="math"
          type="number"
          placeholder="Math Marks"
          value={newStudent.marks.math}
          onChange={handleNewStudentChange}
          min="0"
          max="100"
        />
        <input
          name="science"
          type="number"
          placeholder="Science Marks"
          value={newStudent.marks.science}
          onChange={handleNewStudentChange}
          min="0"
          max="100"
        />
        <input
          name="english"
          type="number"
          placeholder="English Marks"
          value={newStudent.marks.english}
          onChange={handleNewStudentChange}
          min="0"
          max="100"
        />
        <button type="submit">Add Student</button>
      </form>

      <h2>Update Student Age</h2>
      <form onSubmit={handleUpdateStudent}>
        <input
          name="id"
          placeholder="Student ID"
          value={updateAge.id}
          onChange={handleUpdateAgeChange}
        />
        <input
          name="age"
          type="number"
          placeholder="New Age"
          value={updateAge.age}
          onChange={handleUpdateAgeChange}
        />
        <button type="submit">Update Age</button>
      </form>

      <h2>Marks Visualization</h2>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={students} margin={{ top: 5, right: 20, left: 10, bottom: 5 }}>
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="marks.math" fill="#8884d8" name="Math" />
          <Bar dataKey="marks.science" fill="#82ca9d" name="Science" />
          <Bar dataKey="marks.english" fill="#ffc658" name="English" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default App;
