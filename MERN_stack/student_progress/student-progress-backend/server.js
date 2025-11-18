const express = require('express');
const cors = require('cors');
const { MongoClient, ObjectId } = require('mongodb');

const app = express();
app.use(cors());
app.use(express.json());

const uri = 'mongodb://localhost:27017';
const client = new MongoClient(uri);

let studentsCollection;

// Connect to MongoDB and get the students collection
async function connectDB() {
  try {
    await client.connect();
    const db = client.db('studentprogress');
    studentsCollection = db.collection('students');
    console.log('Connected to MongoDB');
  } catch (error) {
    console.error('Failed to connect to MongoDB', error);
  }
}
connectDB();

// Get all students
app.get('/students', async (req, res) => {
  try {
    const students = await studentsCollection.find().toArray();
    res.json(students);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

// Add a new student
app.post('/students', async (req, res) => {
  try {
    const newStudent = req.body;
    const result = await studentsCollection.insertOne(newStudent);
    res.status(201).json({ insertedId: result.insertedId });
  } catch (error) {
    res.status(500).send(error.message);
  }
});

// Update a student by ID
app.put('/students/:id', async (req, res) => {
  try {
    const id = req.params.id;
    const updates = req.body;

    // Validate ObjectId
    if (!ObjectId.isValid(id)) {
      return res.status(400).send('Invalid student ID');
    }

    const result = await studentsCollection.updateOne(
      { _id: new ObjectId(id) },
      { $set: updates }
    );

    if (result.matchedCount === 0) {
      return res.status(404).send('Student not found');
    }

    res.send('Student updated successfully');
  } catch (error) {
    res.status(500).send(error.message);
  }
});

// Start the server
const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
