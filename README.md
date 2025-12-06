# ALPACA - Algorithmic Trading Platform 📈

> A full-stack, self-hosted algorithmic trading platform with Alpaca commission-free trading, AI-powered research, real-time market data, and automated strategy execution.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![Alpaca](https://img.shields.io/badge/Broker-Alpaca-gold.svg)](https://alpaca.markets)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.ai)

**Status**: 🚧 In Active Development (Phase 0 - Alpaca Integration)

---

## 🎯 Vision

Build a production-ready algorithmic trading platform that combines:
- 📊 **Real-time Market Data** - Alpaca WebSocket streaming & historical data
- 💰 **Commission-Free Trading** - Alpaca API for stocks and crypto
- 🤖 **Automated Strategies** - Opening Range Breakout (ORB) and custom algorithms
- 🧠 **AI-Powered Research** - Local LLM (Ollama) + Alpaca News API sentiment
- 📈 **Comprehensive Backtesting** - Validate strategies with Alpaca historical data
- 🌐 **Modern Web Interface** - Full-stack dashboard with TradingView charts

**Inspired by**: [Part Time Larry](https://www.youtube.com/@parttimelarry) (@parttimelarry)

---

## ✨ Why Alpaca?

### Advantages Over Traditional Brokers
- ✅ **Instant Access** - Sign up and get API keys immediately (no approval wait)
- ✅ **Commission-Free** - Zero transaction costs for stocks and crypto
- ✅ **Simple API** - RESTful design, much easier than IBKR TWS
- ✅ **Paper Trading** - Unlimited free paper trading forever
- ✅ **WebSocket Streaming** - Built-in real-time data
- ✅ **News API** - Sentiment analysis included
- ✅ **Fractional Shares** - Trade any dollar amount
- ✅ **Crypto Trading** - BTC, ETH, and more on same platform
- ✅ **Extended Hours** - Trade 4 AM - 8 PM ET
- ✅ **Modern Documentation** - Clear, beginner-friendly

---

## ✨ Key Features

### Current (Phase 0)
- ✅ Project documentation and architecture (Alpaca-focused)
- ✅ Git repository with proper structure
- ✅ Memory Bank for project continuity
- ✅ Development roadmap (.masterplan.md)
- ✅ Alpaca API integration planning

### Planned (Phases 1-5)
- 🔄 Alpaca Trading API integration (alpaca-trade-api)
- 🔄 Real-time market data via Alpaca WebSocket
- 🔄 TradingView chart integration with Alpaca data
- 🔄 Market scanner for "stocks in play"
- 🔄 Strategy backtesting with Alpaca historical data
- 🔄 Opening Range Breakout (ORB) strategy with bracket orders
- 🔄 AI research assistant (Ollama + Alpaca News API)
- 🔄 Full-stack web dashboard (React/Vue)
- 🔄 Portfolio tracking and analytics
- 🔄 News sentiment analysis
- 🔄 Crypto trading support

---

## 🚀 Quick Start

### Prerequisites

```bash
# System Requirements
- macOS/Linux (Windows via WSL)
- Python 3.10 or higher
- Node.js 18+
- Docker Desktop (optional)
- Alpaca account (free paper trading - instant signup!)
- 8GB+ RAM available
```

### Get Alpaca API Keys (30 seconds!)

1. Go to https://alpaca.markets
2. Sign up for free
3. Get instant access to paper trading
4. Copy your API keys from dashboard
5. No account approval needed - start building immediately!

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/GummyPirate2026/ALPACA.git
cd ALPACA

# 2. Set up Python environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env with your Alpaca API keys

# 5. Initialize database
python scripts/init_db.py

# 6. Start the backend (Phase 1+)
uvicorn src.main:app --reload

# 7. Start the frontend (Phase 4+)
cd frontend
npm install
npm run dev
```

### Using Docker (Recommended)

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

---

## 📁 Project Structure

```
ALPACA/
├── .masterplan.md              # Detailed development roadmap
├── memory-bank/                # Project documentation
│   ├── projectbrief.md        # Project overview and goals
│   ├── productContext.md      # User workflows and features
│   ├── systemPatterns.md      # Architecture and design patterns
│   ├── techContext.md         # Technology stack and setup
│   ├── activeContext.md       # Current work focus
│   └── progress.md            # Feature tracking
├── src/                        # Backend source code
│   ├── api/                   # FastAPI endpoints
│   ├── alpaca/                # Alpaca API integration
│   ├── strategies/            # Trading strategies
│   ├── data/                  # Database models
│   ├── ai/                    # Ollama integration
│   └── utils/                 # Shared utilities
├── tests/                     # Test suite
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── frontend/                  # React/Vue web app
├── scripts/                   # Utility scripts
├── docs/                      # Additional documentation
├── docker-compose.yml         # Docker services
└── requirements.txt           # Python dependencies
```

---

## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern async web framework
- **alpaca-trade-api** - Official Alpaca Python SDK
- **alpaca-py** - Next-gen Alpaca SDK (optional)
- **backtesting.py** - Strategy backtesting
- **pandas** - Data analysis
- **SQLAlchemy** - Database ORM
- **SQLite/PostgreSQL** - Database

### Frontend
- **React 18** (or Vue 3) - UI framework
- **TradingView** - Professional charting
- **Tailwind CSS** - Styling
- **Axios** - HTTP client

### AI & Data
- **Ollama** - Local LLM runtime
- **Llama 3.1 70B** - Language model
- **Alpaca Market Data API** - Real-time quotes & historical data
- **Alpaca News API** - News with sentiment scores

### DevOps
- **Docker** - Containerization
- **Git** - Version control
- **pytest** - Testing
- **GitHub Actions** - CI/CD (future)

---

## 📊 Development Phases

| Phase | Description | Duration | Status |
|-------|-------------|----------|--------|
| **0** | Project Setup & Alpaca Integration Planning | 1 week | 🟡 95% |
| **1** | Foundation & Alpaca API Connection | 2 weeks | ⚪ 0% |
| **2** | Market Data & Visualization | 2 weeks | ⚪ 0% |
| **3** | Strategy Engine & Backtesting | 3 weeks | ⚪ 0% |
| **4** | Full-Stack Web Application | 4 weeks | ⚪ 0% |
| **5** | AI Integration (Ollama + News API) | 2 weeks | ⚪ 0% |
| **6** | Advanced Features (Crypto, Alerts) | Ongoing | ⚪ 0% |

**Target**: MVP in 3-4 months

See [.masterplan.md](.masterplan.md) for detailed phase breakdown.

---

## 🎓 Learning Resources

### Essential Videos (Part Time Larry - Alpaca)
1. [Paper Trading with the Alpaca API (17:49)](https://www.youtube.com/@parttimelarry)
2. [Alpaca Market Data API Part 1 - Streaming with Python and Websockets (26:52)](https://www.youtube.com/@parttimelarry)
3. [TradingView webhooks with Alpaca, Python, and AWS Lambda (40:00)](https://www.youtube.com/@parttimelarry)
4. [Walk Forward Optimization with VectorBT and Alpaca (36:06)](https://www.youtube.com/@parttimelarry)
5. [Gap Trading with Alpaca News API & Sentiment Analysis (12:32)](https://www.youtube.com/@parttimelarry)
6. [Build Your Own Robinhood with React Native and Alpaca (9-part series)](https://www.youtube.com/@parttimelarry)

### Documentation
- [Alpaca Trading API Docs](https://alpaca.markets/docs/trading/)
- [Alpaca Market Data API Docs](https://alpaca.markets/docs/market-data/)
- [alpaca-trade-api Python SDK](https://github.com/alpacahq/alpaca-trade-api-python)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [backtesting.py Documentation](https://kernc.github.io/backtesting.py/)

---

## 🤝 Contributing

We welcome contributions! This is a learning project focused on algorithmic trading with Alpaca.

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
2. Check [Issues](https://github.com/GummyPirate2026/ALPACA/issues) for tasks
3. Fork the repository
4. Create a feature branch (`git checkout -b feature/alpaca-scanner`)
5. Commit your changes (`git commit -m 'feat: add alpaca market scanner'`)
6. Push to the branch (`git push origin feature/alpaca-scanner`)
7. Open a Pull Request

See [.masterplan.md](.masterplan.md) for the development roadmap.

---

## 📝 Documentation

### Core Documentation
- **[.masterplan.md](.masterplan.md)** - Complete development roadmap
- **[memory-bank/](memory-bank/)** - Project context and decisions
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Collaboration guidelines

### Memory Bank Files
- **projectbrief.md** - Project vision and scope
- **productContext.md** - User workflows and features
- **systemPatterns.md** - Architecture and design
- **techContext.md** - Technology and setup (Alpaca-specific)
- **activeContext.md** - Current development focus
- **progress.md** - Feature tracking

---

## 💡 Alpaca-Specific Features

### What Makes This Platform Special

**Commission-Free Trading**
- Zero cost per trade (stocks & crypto)
- No hidden fees
- Enables high-frequency testing

**Bracket Orders**
- Profit target + stop loss in one order
- Server-side execution (no connection needed)
- Automated risk management

**News Sentiment Analysis**
- Real-time news with -1 to +1 sentiment scores
- Filter by symbol or market-wide
- Combine with technical analysis

**Fractional Shares**
- Trade any dollar amount
- Better portfolio diversification
- Precise position sizing

**Crypto Trading**
- Same API for stocks and crypto
- BTC, ETH, and more
- 24/7 trading

**Extended Hours**
- Trade 4:00 AM - 8:00 PM ET
- Capture pre-market and after-hours moves
- More opportunities

---

## ⚠️ Disclaimer

**IMPORTANT**: This is an educational project for learning algorithmic trading with Alpaca.

- 📝 **Paper Trading First**: Start with Alpaca paper trading (simulated)
- ⚖️ **Not Financial Advice**: No trading recommendations provided
- 🎓 **Learning Purpose**: Focus is on software engineering and trading concepts
- 🛡️ **Use at Own Risk**: Trading involves substantial risk of loss
- 🔒 **Security**: Never commit API keys or credentials to git
- 💰 **No Real Money Initially**: Test thoroughly in paper trading first

---

## 📈 Project Status

**Current Phase**: 0 - Alpaca Integration Planning (95% complete)

### Recent Updates
- ✅ Pivoted from IBKR to Alpaca
- ✅ Updated all Memory Bank documentation for Alpaca
- ✅ Created Alpaca-specific architecture patterns
- ✅ Updated techContext.md with Alpaca integration patterns
- ✅ Created requirements.txt with alpaca-trade-api
- ✅ Configured .env.example for Alpaca API keys

### Next Steps
- [ ] Sign up for Alpaca paper trading account
- [ ] Test basic Alpaca API connection
- [ ] Create first Alpaca data retrieval script
- [ ] Set up database schema for Alpaca data
- [ ] Begin Phase 1: Full Alpaca integration

See [memory-bank/progress.md](memory-bank/progress.md) for detailed status.

---

## 🙏 Acknowledgments

- **[Part Time Larry](https://www.youtube.com/@parttimelarry)** - Inspiration and Alpaca tutorials
- **[Alpaca Markets](https://alpaca.markets)** - Commission-free trading API
- **Ollama Team** - Local LLM infrastructure
- **Open Source Community** - Amazing libraries and tools

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔗 Links

- **Repository**: [github.com/GummyPirate2026/ALPACA](https://github.com/GummyPirate2026/ALPACA)
- **Alpaca**: [alpaca.markets](https://alpaca.markets)
- **YouTube**: [Part Time Larry](https://www.youtube.com/@parttimelarry)
- **Documentation**: [memory-bank/](memory-bank/)
- **Roadmap**: [.masterplan.md](.masterplan.md)
- **Issues**: [GitHub Issues](https://github.com/GummyPirate2026/ALPACA/issues)

---

## 💬 Support

- 📚 Check the [memory-bank/](memory-bank/) documentation
- 🐛 Report bugs via [Issues](https://github.com/GummyPirate2026/ALPACA/issues)
- 💡 Suggest features via [Discussions](https://github.com/GummyPirate2026/ALPACA/discussions)
- 📖 Review [.masterplan.md](.masterplan.md) for project plans
- 🦙 Get Alpaca support at [alpaca.markets/support](https://alpaca.markets/support)

---

## 🚀 Getting Started Checklist

- [ ] Sign up at [alpaca.markets](https://alpaca.markets)
- [ ] Get paper trading API keys
- [ ] Clone this repository
- [ ] Set up Python environment
- [ ] Install dependencies
- [ ] Configure .env with Alpaca keys
- [ ] Test Alpaca connection
- [ ] Follow Phase 1 in .masterplan.md

---

**Built with ❤️ for algorithmic traders and developers**

**Powered by Alpaca 🦙**

_Last Updated: 2025-12-06_
