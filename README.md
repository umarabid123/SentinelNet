# SentinelNet

SentinelNet is an AI-powered router monitoring tool that leverages the LLaMa 3:1B model and blockchain technology to detect network anomalies and notify users in real-time. It includes a Python backend for data collection, AI analysis, and blockchain notifications, as well as a React.js frontend for monitoring and visualization.

---

## Project Structure
```
project-root/
├── backend/
│   ├── app/
│   │   ├── data_collection.py       # Script to collect network traffic data
│   │   ├── preprocessing.py         # Data aggregation and formatting logic
│   │   ├── ai_analysis.py           # AI model integration and anomaly detection
│   │   ├── blockchain_notifications.py # Blockchain notification handling
│   ├── venv/                        # Virtual environment for Python dependencies
│   ├── requirements.txt             # Backend dependencies
│   ├── server.py                    # Backend server script
├── frontend/
│   ├── public/                      # Static assets
│   ├── src/                         # React app source code
│   │   ├── components/              # UI components (e.g., NotificationTable)
│   │   ├── pages/                   # App pages
│   │   └── App.js                   # Main React component
│   ├── package.json                 # Frontend dependencies
├── .gitignore                       # Git ignore file
├── README.md                        # Project documentation
```

---


## Getting Started

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the backend server:
   ```bash
   python server.py
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the React app:
   ```bash
   npm start
   ```

---

## Features
- **Real-Time Monitoring:** Tracks router network activity and detects anomalies.
- **AI-Powered Analysis:** Uses LLaMa 3:1B to identify security threats and malfunctions.
- **Blockchain Notifications:** Sends detailed alerts to a blockchain network for secure logging.
- **User Dashboard:** A React-based interface to view and analyze notifications.

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes and submit a pull request.

---

## License
This project is licensed under the MIT License.
