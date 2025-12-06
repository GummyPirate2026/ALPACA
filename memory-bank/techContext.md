# Tech Context

## Technologies Used

### Backend Stack
- **Python 3.10+** - Primary programming language
- **FastAPI** - Modern async web framework (alternative: Flask)
- **ib_async** - Interactive Brokers API client library
- **backtesting.py** - Python backtesting framework
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computations
- **SQLAlchemy** - Database ORM
- **uvicorn** - ASGI server for FastAPI

### Frontend Stack
- **React 18** (or Vue 3) - UI framework
- **TradingView Charting Library** - Professional charting
- **Axios** - HTTP client
- **Tailwind CSS** - Utility-first CSS framework
- **Vite** - Build tool and dev server

### AI & Machine Learning
- **Ollama** - Local LLM runtime (already installed)
- **Llama 3.1 70B** - Primary language model
- **langchain** (optional) - LLM orchestration framework

### Data & Database
- **SQLite** - Development database
- **PostgreSQL** (future) - Production database
- **Redis** (optional) - Caching layer

### DevOps & Tools
- **Docker** - Container platform (already installed)
- **Docker Compose** - Multi-container orchestration
- **Git** - Version control
- **pytest** - Testing framework
- **black** - Code formatter
- **flake8** - Linting tool

### APIs & Data Sources
- **Interactive Brokers TWS/Gateway** - Broker API
- **IBKR Market Data** - Real-time & historical data
- **Alpha Vantage** (optional) - Alternative market data
- **Yahoo Finance** (optional) - Free historical data

## Development Setup

### Prerequisites
```bash
# System Requirements
- macOS (current: Apple Silicon)
- Python 3.10 or higher
- Node.js 18+ (for frontend)
- Docker Desktop (already installed)
- Interactive Brokers account (paper trading)
- 8GB+ RAM available (48GB total)
```

### Installation Steps

#### 1. Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/trading-app.git
cd trading-app
```

#### 2. Python Environment Setup
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

#### 3. IBKR TWS Setup
```bash
# Download TWS or IB Gateway from Interactive Brokers
# Configure for paper trading
# Enable API connections (port 7497 for TWS, 4002 for Gateway)
```

#### 4. Environment Configuration
```bash
# Copy environment template
cp .env.example .env

# Edit .env with your settings
# IBKR_HOST=127.0.0.1
# IBKR_PORT=7497
# IBKR_CLIENT_ID=1
# DATABASE_URL=sqlite:///./trading.db
# OLLAMA_URL=http://localhost:11434
```

#### 5. Database Initialization
```bash
# Run migrations
python scripts/init_db.py
```

#### 6. Frontend Setup (if separate repo)
```bash
cd frontend
npm install
npm run dev
```

#### 7. Start Services
```bash
# Option 1: Docker Compose (recommended)
docker-compose up -d

# Option 2: Manual start
python src/main.py  # Backend
cd frontend && npm run dev  # Frontend
```

### Current Environment
- **Host Machine**: MacBook Pro (48GB RAM, Apple Silicon)
- **Ollama**: Running at http://localhost:11434
- **Docker**: Version 29.1.2
- **Python**: (version to be confirmed)
- **Node.js**: (to be installed)

## Technical Constraints

### Performance Constraints
- **Market Data Rate**: IBKR has rate limits
  - Maximum 50 simultaneous market data subscriptions
  - Maximum 60 API requests per second
- **Local LLM**: Llama 3.1 70B requires ~40GB RAM when loaded
- **Database**: SQLite has limited concurrent write capability

### API Limitations
- **IBKR Paper Trading**: 
  - Simulated fills may not match real market
  - Some order types have different behavior
  - Market data is delayed by 15 minutes unless subscribed
- **Ollama**:
  - Local processing only (no cloud backup)
  - Response time depends on model size
  - Token limit per request

### Development Constraints
- **Browser Compatibility**: Modern browsers only (Chrome, Firefox, Safari)
- **Real-time Updates**: Dependent on stable internet connection
- **Time Zone**: Market hours are Eastern Time (ET)

## Dependencies

### Python Requirements (requirements.txt)
```txt
# Core Framework
fastapi==0.109.0
uvicorn[standard]==0.27.0
python-dotenv==1.0.0

# Interactive Brokers
ib-insync==0.9.86

# Data & Analysis
pandas==2.2.0
numpy==1.26.3
backtesting==0.3.3

# Database
sqlalchemy==2.0.25
alembic==1.13.1

# Async & Utilities
aiohttp==3.9.1
python-dateutil==2.8.2

# AI Integration
requests==2.31.0

# Testing
pytest==8.0.0
pytest-asyncio==0.23.4
pytest-cov==4.1.0

# Code Quality
black==24.1.1
flake8==7.0.0
mypy==1.8.0
```

### Frontend Dependencies (package.json)
```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "axios": "^1.6.5",
    "react-router-dom": "^6.21.3"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.1",
    "vite": "^5.0.11",
    "tailwindcss": "^3.4.1",
    "autoprefixer": "^10.4.17",
    "postcss": "^8.4.33"
  }
}
```

## Tool Usage Patterns

### Development Workflow
```bash
# 1. Create feature branch
git checkout -b feature/market-scanner

# 2. Start development environment
docker-compose up -d

# 3. Run backend in development mode (hot reload)
uvicorn src.main:app --reload

# 4. Run frontend in development mode
cd frontend && npm run dev

# 5. Run tests
pytest tests/

# 6. Format code
black src/ tests/

# 7. Commit changes
git add .
git commit -m "Add market scanner feature"
git push origin feature/market-scanner
```

### Testing Commands
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_strategy.py

# Run with coverage
pytest --cov=src --cov-report=html

# Run integration tests only
pytest tests/integration/
```

### Database Management
```bash
# Create migration
alembic revision --autogenerate -m "Add trades table"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1

# View migration history
alembic history
```

### Docker Commands
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f [service_name]

# Restart service
docker-compose restart [service_name]

# Stop all services
docker-compose down

# Rebuild after code changes
docker-compose up -d --build
```

### Ollama Integration
```bash
# Check Ollama status
curl http://localhost:11434/api/tags

# Generate completion
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.1:70b",
  "prompt": "Analyze this trading pattern:",
  "stream": false
}'

# List available models
ollama list
```

## Integration Patterns

### IBKR Connection Pattern
```python
from ib_async import IB, Stock

# Initialize connection
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

# Request market data
contract = Stock('AAPL', 'SMART', 'USD')
ticker = ib.reqMktData(contract)

# Event handler
def on_pending_tickers(tickers):
    for ticker in tickers:
        print(f"{ticker.contract.symbol}: {ticker.last}")

ib.pendingTickersEvent += on_pending_tickers
```

### TradingView Integration Pattern
```javascript
// Frontend - TradingView widget
const widget = new TradingView.widget({
  container_id: "tv_chart_container",
  datafeed: new Datafeeds.UDFCompatibleDatafeed(
    "http://localhost:8000/api/tradingview"
  ),
  symbol: "AAPL",
  interval: "1",
  library_path: "/charting_library/",
});
```

### Ollama API Pattern
```python
import requests

def ask_ollama(prompt: str, model: str = "llama3.1:70b") -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]
```

### SSE Streaming Pattern
```python
from fastapi.responses import StreamingResponse

async def market_data_stream():
    while True:
        data = await get_market_data()
        yield f"data: {json.dumps(data)}\n\n"

@app.get("/stream/quotes")
async def stream_quotes():
    return StreamingResponse(
        market_data_stream(),
        media_type="text/event-stream"
    )
```

## Configuration Management

### Environment Variables (.env)
```bash
# Application
APP_ENV=development
DEBUG=true
LOG_LEVEL=INFO

# Interactive Brokers
IBKR_HOST=127.0.0.1
IBKR_PORT=7497
IBKR_CLIENT_ID=1
IBKR_ACCOUNT=DU123456

# Database
DATABASE_URL=sqlite:///./data/trading.db

# Ollama
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama3.1:70b

# API Settings
API_HOST=0.0.0.0
API_PORT=8000

# Frontend
VITE_API_URL=http://localhost:8000
```

## Monitoring & Logging

### Logging Strategy
```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/trading.log'),
        logging.StreamHandler()
    ]
)

# Use in code
logger = logging.getLogger(__name__)
logger.info("Strategy signal generated", extra={
    "symbol": "AAPL",
    "signal": "BUY"
})
```

### Performance Monitoring
- API response times
- Database query performance
- Market data latency
- Order execution time
- Memory usage tracking

## Troubleshooting Guide

### Common Issues

**1. IBKR Connection Failed**
- Check TWS/Gateway is running
- Verify port number (7497 or 4002)
- Enable API in TWS settings
- Check firewall settings

**2. Ollama Not Responding**
- Verify Ollama app is running
- Check model is downloaded: `ollama list`
- Test with: `curl http://localhost:11434/api/tags`

**3. Database Lock Errors**
- SQLite limitation with concurrent writes
- Consider PostgreSQL for production
- Implement connection pooling

**4. Frontend Can't Connect to Backend**
- Check CORS settings in FastAPI
- Verify API_URL in .env
- Check backend is running: `curl http://localhost:8000/health`
