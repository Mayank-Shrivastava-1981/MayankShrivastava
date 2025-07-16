import { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [testCase, setTestCase] = useState('');
  const [testSteps, setTestSteps] = useState('');
  const [testData, setTestData] = useState('');
  const [selectedTool, setSelectedTool] = useState('Selenium');
  const [selectedLanguage, setSelectedLanguage] = useState('Java');
  const [generatedCode, setGeneratedCode] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [inputMode, setInputMode] = useState('text');
  const [url, setUrl] = useState('');
  const [xpaths, setXpaths] = useState([]); // added state for xpaths

  const handleInputModeChange = (mode) => setInputMode(mode);

  const fetchXpaths = async () => {
    try {
      let normalizedUrl = url.trim();
    if (!/^https?:\/\//i.test(normalizedUrl)) {
      normalizedUrl = 'https://' + normalizedUrl;
    }
      // Store xpaths on server
      console.log('Storing xpaths for URL:', url);
      //await axios.get(`${import.meta.env.VITE_BACKEND_URL}/extract-xpaths`, { params: { normalizedUrl } });

      const res = await axios.get(`${import.meta.env.VITE_BACKEND_URL}/extract-xpaths`, { params: { url: normalizedUrl,testCase: testCase } });
      const fetchedXpaths = res.data.xpaths || [];
      console.log('Fetched XPaths:', fetchedXpaths);
      setXpaths(fetchedXpaths);

      // Optionally append to testSteps
      {/*let appendedSteps = testSteps;
      fetchedXpaths.forEach((item, index) => {
        appendedSteps += `\nStep ${index + 1}: Fill ${item.tag}`;
        if (item.id) {
          appendedSteps += ` using id: ${item.id}`;
        } else if (item.name) {
          appendedSteps += ` using name: ${item.name}`;
        } else if (item.class && item.class.length > 0) {
          appendedSteps += ` using class: ${Array.isArray(item.class) ? item.class.join(' ') : item.class}`;
        } else {
          appendedSteps += ` using XPath: ${item.xpath}`;
        }
      });
      setTestSteps(appendedSteps.trim());*/}

      //alert('XPaths fetched and stored successfully!');
    } catch (e) {
      console.error(e);
      //alert('Error storing or fetching XPaths');
    }
  };

  const generateCode = async () => {
    
    setLoading(true);
    setError(null);
    setGeneratedCode('');
 
    await fetchXpaths();  // wait for xpaths fetched before proceeding

    
    try {
      const response = await axios({
        url: 'https://api.openai.com/v1/chat/completions',
        method: 'post',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${import.meta.env.VITE_OPENAI_API_KEY}`,
        },
        data: {
          model: 'gpt-3.5-turbo', // Use the latest 
         

           messages: [
              {
                role: 'system',
                content: `You are an expert QA automation engineer. Generate high-quality test automation code using ${selectedTool} and ${selectedLanguage}.`
              },
              
              {
              role: 'user',
              content: `Generate a code snippet in ${selectedLanguage} that performs the following task.

              Test case: "${testCase}"
              Data: "${testData}"
              Start URL: "${url}"

              Use only these elements relevant to the Test case:
              "${JSON.stringify(xpaths)}"

            Selector rules:
            - Prefer: By.name, By.id, or CSS selectors
            - Use XPath only if no other option is available

            STRICT OUTPUT INSTRUCTION: 
            Return only valid ${selectedLanguage} code with necessary imports. Do NOT include markdown, explanations, comments, or extra formatting.`
              }
          
          ],
          max_tokens: 300,
          temperature: 0, // Lower temperature for more deterministic output
       
        },
      });

      const generatedText = response.data.choices[0].message.content;
      console.log('Generated Code:', generatedText);
      // If the model returns multiple code blocks, only keep the first one
      const firstCode = generatedText.split(/```[\s\S]*?```/)[0].trim() || generatedText.trim();
      const cleanCode = firstCode
        .replace(/^[\s`]+/, '')
        .replace(/[\s`]+$/, '');
      setGeneratedCode(cleanCode);
    } catch (err) {
      console.error(err);
      setError('Error generating code. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const copyToClipboard = () => {
    navigator.clipboard.writeText(generatedCode)
      .then(() => alert('Code copied to clipboard!'))
      .catch(() => alert('Failed to copy code to clipboard.'));
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <h3>Smart Auto GenAI </h3>
      </header>

      <div className="main-content">
        <div className="input-section">
          {/* Tool and Language Dropdowns */}
          <h5>Select Tools and Language</h5> 
          <select value={selectedTool} onChange={(e) => setSelectedTool(e.target.value)} className="tool-dropdown">
            <option value="Selenium">Selenium</option>
            <option value="Katalon">Katalon</option>
            <option value="Cypress">Cypress</option>
            <option value="Appium">Appium</option>
          </select>

          <select value={selectedLanguage} onChange={(e) => setSelectedLanguage(e.target.value)} className="language-dropdown">
            <option value="Java">Java</option>
            <option value="Python">Python</option>
            <option value="JavaScript">JavaScript</option>
            <option value="C#">C#</option>
          </select>

          {/* Input Mode Buttons */}
          <div className="input-mode-buttons">
            <button className={`text-input-btn ${inputMode === 'text' ? 'active' : ''}`} onClick={() => handleInputModeChange('text')}>
              Text Input
            </button>
            <button className={`voice-input-btn ${inputMode === 'voice' ? 'active' : ''}`} onClick={() => handleInputModeChange('voice')}>
              Voice Input
            </button>
          </div>

          

          {/*Display fetched XPaths
          <ul className="xpath-list">
            {xpaths.map((item, idx) => (
              <li key={idx}>
                <strong>{item.tag}</strong>: {item.xpath} {item.placeholder && `(placeholder: ${item.placeholder})`}
              </li>
            ))}
          </ul> */}

          {/* Input Sections */}
          <div className="input-container">
            {inputMode === 'text' && (
              <>
              <h5>Describe Test Case</h5>
                <textarea
                  value={testCase}
                  onChange={(e) => setTestCase(e.target.value)}
                  placeholder="Describe the test case..."
                  className="test-case-input"
                ></textarea>
                {/* XPath URL Input and Fetch Button */}
                <h5>Enter URL</h5>
                <input
                  type="text"
                  value={url}
                  onChange={(e) => setUrl(e.target.value)}
                  placeholder="Enter URL"
                  className="url-input"
                />
                {/* <textarea
                  value={testSteps}
                  onChange={(e) => setTestSteps(e.target.value)}
                  placeholder="Describe the steps for the test case..."
                  className="test-steps-input"
                ></textarea> */}
                <h5>Provide Test Data</h5>
                <textarea
                  value={testData}
                  onChange={(e) => setTestData(e.target.value)}
                  placeholder="Provide any test data..."
                  className="test-data-input"
                ></textarea>
              </>
            )}

            {inputMode === 'voice' && (
              <div className="voice-input">
                <p>Voice input activated. (Voice recognition goes here)</p>
                <button className="record-btn">Start Recording</button>
                <textarea
                  value={testSteps}
                  onChange={(e) => setTestSteps(e.target.value)}
                  placeholder="Additional input for voice recording..."
                  className="additional-input"
                ></textarea>
              </div>
            )}
          </div>

          <button onClick={generateCode} disabled={loading} className="generate-btn">
            {loading ? 'Generating...' : 'Generate'}
          </button>
          {error && <p className="error-message">{error}</p>}
        </div>

        {/* Output Section */}
        <div className="output-section">
          <h2>Generated Code</h2>
          <div className="code-output">
            <pre>{generatedCode || 'The generated code will be displayed here'}</pre>
          </div>
          {generatedCode && (
            <button onClick={copyToClipboard} className="copy-btn">Copy</button>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
