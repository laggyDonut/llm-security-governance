const express = require('express');
const fetch = require('node-fetch');
const cors = require('cors');
require('dotenv').config();
const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const app = express();
app.use(cors());
app.use(express.json());

const db = new sqlite3.Database('./database.db', (err) => {
    if (err) {
        console.error(err.message);
    }
    console.log('Connected to the SQLite database.');
});

db.serialize(() => {
    db.run(`CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )`, (err) => {
        if (err) {
            console.error(err.message);
        }
    });

    const saltRounds = 10;
    const adminPassword = 'admin';

    bcrypt.hash(adminPassword, saltRounds, (err, hash) => {
        if (err) {
            console.error(err);
            return;
        }
        const sql = `INSERT OR IGNORE INTO user (username, password) VALUES (?, ?)`;
        db.run(sql, ['admin', hash], (err) => {
            if (err) {
                console.error(err.message);
            }
        });
    });
});

app.post('/login', (req, res) => {
    const { username, password } = req.body;
    const sql = `SELECT * FROM user WHERE username = ?`;

    db.get(sql, [username], (err, row) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        if (row) {
            bcrypt.compare(password, row.password, (err, result) => {
                if (result) {
                    const token = jwt.sign({ username: row.username }, process.env.JWT_SECRET || 'your_jwt_secret', { expiresIn: '2m' });
                    res.json({ token });
                } else {
                    res.status(401).json({ error: 'Invalid credentials' });
                }
            });
        } else {
            res.status(401).json({ error: 'Invalid credentials' });
        }
    });
});


const OPENROUTER_URL = 'https://openrouter.ai/api/v1/chat/completions';
const API_KEY = process.env.OPENROUTER_API_KEY;

if (!API_KEY) {
  console.warn('Warning: OPENROUTER_API_KEY is not set. Set it in .env or environment variables.');
}

app.post('/api/chat', async (req, res) => {
  try {
    const payload = req.body;

    const response = await fetch(OPENROUTER_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${API_KEY}`
      },
      body: JSON.stringify(payload)
    });

    const data = await response.json();
    res.status(response.status).json(data);
  } catch (err) {
    console.error('Proxy error:', err);
    res.status(500).json({ error: 'Server error' });
  }
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Server running on port ${port}`));
