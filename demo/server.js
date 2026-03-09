/**
 * AI Security Governance Demo - Express.js Proxy Server
 * ========================================================
 * 
 * SECURITY CONTEXT:
 * -----------------
 * This server acts as a secure proxy between the frontend and OpenRouter API.
 * The API key is kept server-side and NEVER exposed to the client.
 * This prevents API key theft via browser developer tools or network inspection.
 * 
 * WARNING: This is a LOCAL DEMONSTRATION server with NO authentication.
 * Do NOT deploy this to production without adding proper authentication!
 * 
 * @author AI Security Governance Demo
 * @version 1.0.0
 */

const express = require('express');
const fetch = require('node-fetch');
const cors = require('cors');
const path = require('path');

// Load environment variables from .env file
// SECURITY: API keys should NEVER be hardcoded in source code
require('dotenv').config({ path: path.resolve(__dirname, '../.env') });

// Initialize Express application
const app = express();

// ============================================================================
// MIDDLEWARE CONFIGURATION
// ============================================================================

// Enable CORS for local development
// SECURITY NOTE: In production, restrict this to specific origins
app.use(cors());

// Parse JSON request bodies
// This is required for POST requests with JSON payloads
app.use(express.json());

// Serve static files from the 'public' directory
// This includes index.html, app.js, and any other frontend assets
app.use(express.static(path.join(__dirname, 'public')));

// ============================================================================
// OPENROUTER API CONFIGURATION
// ============================================================================

// OpenRouter API endpoint for chat completions
const OPENROUTER_URL = 'https://openrouter.ai/api/v1/chat/completions';

// Retrieve API key from environment variables
// SECURITY: Never log or expose this key to the client
const API_KEY = process.env.OPENROUTER_API_KEY;

// Validate that the API key is present
// This provides clear feedback if the .env file is misconfigured
if (!API_KEY) {
    console.error('═══════════════════════════════════════════════════════════════');
    console.error('ERROR: OPENROUTER_API_KEY is not set!');
    console.error('');
    console.error('Please create a .env file in the repository root with:');
    console.error('  OPENROUTER_API_KEY=your_api_key_here');
    console.error('');
    console.error('You can get an API key from: https://openrouter.ai/keys');
    console.error('═══════════════════════════════════════════════════════════════');
}

// ============================================================================
// API ROUTES
// ============================================================================

/**
 * POST /api/chat
 * 
 * Proxy endpoint that forwards chat requests to OpenRouter API.
 * 
 * SECURITY CONTEXT:
 * - The frontend sends the chat payload (model, messages, etc.)
 * - This server adds the Authorization header with the API key
 * - The API key is never exposed to the client
 * 
 * REQUEST BODY:
 * {
 *   "model": "string",      // e.g., "openai/gpt-3.5-turbo"
 *   "messages": [           // Array of chat messages
 *     { "role": "system", "content": "..." },
 *     { "role": "user", "content": "..." }
 *   ],
 *   "temperature": number,  // Optional: creativity (0-2)
 *   "max_tokens": number    // Optional: response length limit
 * }
 * 
 * RESPONSE:
 * - On success: OpenRouter API response (status 200)
 * - On error: Error message with appropriate status code
 */
app.post('/api/chat', async (req, res) => {
    // Check if API key is configured before making requests
    if (!API_KEY) {
        return res.status(500).json({ 
            error: 'Server configuration error: API key not set',
            message: 'Please configure OPENROUTER_API_KEY in the .env file'
        });
    }

    try {
        // Extract the payload from the client request
        const payload = req.body;

        // Log request for debugging (without sensitive data)
        console.log(`[${new Date().toISOString()}] Chat request received`);
        console.log(`  Model: ${payload.model}`);
        console.log(`  Messages: ${payload.messages?.length || 0}`);

        // Forward the request to OpenRouter API
        // SECURITY: Only the server knows the API key
        const response = await fetch(OPENROUTER_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${API_KEY}`,
                // OpenRouter recommends setting these headers for tracking
                'HTTP-Referer': 'http://localhost:3000',
                'X-Title': 'AI Security Governance Demo'
            },
            body: JSON.stringify(payload)
        });

        // Parse the API response
        const data = await response.json();

        // Log response status for debugging
        if (response.ok) {
            console.log(`  Response: Success (${response.status})`);
        } else {
            console.log(`  Response: Error (${response.status})`);
            console.log(`  Error details:`, data);
        }

        // Forward the response to the client
        res.status(response.status).json(data);

    } catch (err) {
        // Handle network errors, timeouts, etc.
        console.error('Proxy error:', err.message);
        res.status(500).json({ 
            error: 'Failed to communicate with AI service',
            message: err.message 
        });
    }
});

/**
 * GET /api/health
 * 
 * Health check endpoint to verify the server is running.
 * Useful for debugging and monitoring.
 */
app.get('/api/health', (req, res) => {
    res.json({ 
        status: 'ok',
        apiKeyConfigured: !!API_KEY,
        timestamp: new Date().toISOString()
    });
});

// ============================================================================
// SERVER STARTUP
// ============================================================================

// Use PORT from environment or default to 3000
const port = process.env.PORT || 3000;

// Start the server
app.listen(port, () => {
    console.log('');
    console.log('═══════════════════════════════════════════════════════════════');
    console.log('  🛡️  AI Security Governance Demo Server');
    console.log('═══════════════════════════════════════════════════════════════');
    console.log(`  🚀 Server running at: http://localhost:${port}`);
    console.log(`  📊 Health check:      http://localhost:${port}/api/health`);
    console.log(`  🔑 API Key Status:    ${API_KEY ? '✓ Configured' : '✗ NOT SET'}`);
    console.log('═══════════════════════════════════════════════════════════════');
    console.log('');
    if (!API_KEY) {
        console.log('  ⚠️  WARNING: Set OPENROUTER_API_KEY in .env to enable chat');
        console.log('');
    }
});
