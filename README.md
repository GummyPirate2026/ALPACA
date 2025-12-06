# Algorithmic Trading Platform 📈

> A full-stack, self-hosted algorithmic trading platform with AI-powered research, real-time market data, and automated strategy execution.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black.svg)](https://ollama.ai)

**Status**: 🚧 In Active Development (Phase 0 - Setup)

---

## 🎯 Vision

Build a production-ready algorithmic trading platform that combines:
- 📊 **Real-time Market Data** - Live quotes and streaming via Interactive Brokers
- 🤖 **Automated Strategies** - Opening Range Breakout (ORB) and custom algorithms
- 🧠 **AI-Powered Research** - Local LLM integration with Ollama
- 📈 **Comprehensive Backtesting** - Validate strategies with historical data
- 🌐 **Modern Web Interface** - Full-stack dashboard with TradingView charts

**Inspired by**: [Part Time Larry](https://www.youtube.com/@parttimelarry) (@parttimelarry)

---

## ✨ Key Features

### Current (Phase 0)
- ✅ Project documentation and architecture
- ✅ Git repository with proper structure
- ✅ Memory Bank for project continuity
- ✅ Development roadmap (.masterplan.md)

### Planned (Phases 1-5)
- 🔄 Interactive Brokers API integration (ib_async)
- 🔄 Real-time market data streaming (SSE)
- 🔄 TradingView chart integration
- 🔄 Market scanner for "stocks in play"
- 🔄 Strategy backtesting engine
- 🔄 Opening Range Breakout (ORB) strategy
- 🔄 AI research assistant (Ollama + Llama 3.1 70B)
- 🔄 Full-stack web dashboard (React/Vue)
- 🔄 Portfolio tracking and analytics

---

## 🚀 Quick Start

### Prerequisites

```bash
# System Requirements
- macOS/Linux (Windows via WSL)
- Python 3.10 or higher
- Node.js 18+
- Docker Desktop
- Interactive Brokers account (paper trading)
- 8GB+ RAM available
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/trading-app.git
cd trading-app

# 2. Set up Python environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env with your settings

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
trading-app/
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
│   ├── brokers/               # IBKR integration
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
- **ib_async** - Interactive Brokers API client
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
- **IBKR Market Data** - Real-time quotes

### DevOps
- **Docker** - Containerization
- **Git** - Version control
- **pytest** - Testing
- **GitHub Actions** - CI/CD (future)

---

## 📊 Development Phases

| Phase | Description | Duration | Status |
|-------|-------------|----------|--------|
| **0** | Project Setup & Infrastructure | 1 week | 🟡 70% |
| **1** | Foundation & IBKR Integration | 2 weeks | ⚪ 0% |
| **2** | Market Data & Visualization | 2 weeks | ⚪ 0% |
| **3** | Strategy Engine & Backtesting | 3 weeks | ⚪ 0% |
| **4** | Full-Stack Web Application | 4 weeks | ⚪ 0% |
| **5** | AI Integration (Ollama) | 2 weeks | ⚪ 0% |
| **6** | Advanced Features | Ongoing | ⚪ 0% |

**Target**: MVP in 3-4 months

See [.masterplan.md](.masterplan.md) for detailed phase breakdown.

---

## 🎓 Learning Resources

### Essential Videos (Part Time Larry)
1. [Interactive Brokers API with Python and ib_async](https://www.youtube.com/@parttimelarry)
2. [Full Stack IBKR API - TradingView Integration](https://www.youtube.com/@parttimelarry)
3. [ORB Strategy in Python with IBKR API](https://www.youtube.com/@parttimelarry)
4. [Real-Time Market Scanners](https://www.youtube.com/@parttimelarry)
5. [Backtesting.py Tutorial](https://www.youtube.com/@parttimelarry)

### Documentation
- [ib_async Documentation](https://ib-insync.readthedocs.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [backtesting.py Documentation](https://kernc.github.io/backtesting.py/)
- [Interactive Brokers API Guide](https://interactivebrokers.github.io/)

---

## 🤝 Contributing

We welcome contributions! This is a learning project focused on algorithmic trading.

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
2. Check [Issues](https://github.com/YOUR_USERNAME/trading-app/issues) for tasks
3. Fork the repository
4. Create a feature branch (`git checkout -b feature/amazing-feature`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
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
- **techContext.md** - Technology and setup
- **activeContext.md** - Current development focus
- **progress.md** - Feature tracking

---

## ⚠️ Disclaimer

**IMPORTANT**: This is an educational project for learning algorithmic trading concepts.

- 📝 **Paper Trading Only**: Start with paper trading (simulated)
- ⚖️ **Not Financial Advice**: No trading recommendations provided
- 🎓 **Learning Purpose**: Focus is on software engineering and trading concepts
- 🛡️ **Use at Own Risk**: Trading involves substantial risk of loss
- 🔒 **Security**: Never commit API keys or credentials to git

---

## 📈 Project Status

**Current Phase**: 0 - Project Setup (70% complete)

### Recent Updates
- ✅ Git repository initialized
- ✅ Memory Bank documentation complete
- ✅ .masterplan.md roadmap created
- ✅ Project structure defined
- ✅ Technology stack finalized

### Next Steps
- [ ] Complete README.md and CONTRIBUTING.md
- [ ] Set up GitHub repository
- [ ] Create project directories
- [ ] Install Python dependencies
- [ ] Begin Phase 1: IBKR integration

See [memory-bank/progress.md](memory-bank/progress.md) for detailed status.

---

## 🙏 Acknowledgments

- **[Part Time Larry](https://www.youtube.com/@parttimelarry)** - Inspiration and tutorials
- **Interactive Brokers** - Market data and execution platform
- **Ollama Team** - Local LLM infrastructure
- **Open Source Community** - Amazing libraries and tools

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔗 Links

- **YouTube**: [Part Time Larry](https://www.youtube.com/@parttimelarry)
- **Documentation**: [memory-bank/](memory-bank/)
- **Roadmap**: [.masterplan.md](.masterplan.md)
- **Issues**: [GitHub Issues](https://github.com/YOUR_USERNAME/trading-app/issues)
- **Discussions**: [GitHub Discussions](https://github.com/YOUR_USERNAME/trading-app/discussions)

---

## 💬 Support

- 📚 Check the [memory-bank/](memory-bank/) documentation
- 🐛 Report bugs via [Issues](https://github.com/YOUR_USERNAME/trading-app/issues)
- 💡 Suggest features via [Discussions](https://github.com/YOUR_USERNAME/trading-app/discussions)
- 📖 Review [.masterplan.md](.masterplan.md) for project plans

---

**Built with ❤️ for algorithmic traders and developers**

_Last Updated: 2025-12-06_
