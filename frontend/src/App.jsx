import { useState } from 'react'
import axios from 'axios'

function App() {
  const [question, setQuestion] = useState('')
  const [response, setResponse] = useState('')
  const [loading, setLoading] = useState(false)

  const handleAsk = async () => {
    setLoading(true)
    try {
      const res = await axios.post('/api/ask', { question })
      setResponse(res.data.answer)
    } catch (err) {
      setResponse('Error: Could not get response.')
    }
    setLoading(false)
  }

  return (
    <div className="app-container">
      <h1>Knowledge Intelligence Platform</h1>
      <div className="card">
        <textarea 
          value={question} 
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask a question about your documents..."
        />
        <button onClick={handleAsk} disabled={loading}>
          {loading ? 'Thinking...' : 'Ask AI'}
        </button>
      </div>
      {response && (
        <div className="response">
          <h3>Response:</h3>
          <p>{response}</p>
        </div>
      )}
    </div>
  )
}

export default App
