# Project Brief

## Project Name
ALPACA - Algorithmic Trading Platform (inspired by Part Time Larry)

## Overview
A full-stack algorithmic trading application that combines real-time market data, automated trading strategies, AI-powered research, and comprehensive backtesting capabilities. The platform integrates the Alpaca Trading API for commission-free stock and crypto trading, provides real-time market scanning, implements proven trading strategies, and leverages local AI (Ollama) for market analysis and research.

## Core Requirements
- **Real-time Market Data**: Alpaca Market Data API with WebSocket streaming
- **Broker Integration**: Alpaca Trading API for paper and live trading
- **Chart Visualization**: TradingView charts with real-time updates
- **Strategy Engine**: Backtesting framework and automated strategy execution
- **Web Interface**: Full-stack web application for monitoring and control
- **AI Research Assistant**: Local Ollama integration for market analysis
- **News Integration**: Alpaca News API for sentiment analysis
- **Collaborative Development**: GitHub-based workflow for team development

## Goals
- Build a production-ready algorithmic trading platform
- Learn quantitative trading concepts and implementation
- Implement proven strategies (ORB, market scanning, etc.)
- Create reusable trading infrastructure for future strategies
- Maintain privacy with self-hosted AI and local execution
- Enable collaborative development with clear documentation

## Scope

### In Scope (MVP)
**Phase 1: Foundation**
- Alpaca API integration and authentication (paper trading)
- Real-time data streaming with Alpaca WebSockets
- Database setup for historical data storage
- Basic web server with API endpoints

**Phase 2: Market Data & Visualization**
- Alpaca Market Data API integration
- TradingView chart integration
- Real-time quote display via WebSocket
- Market scanner for "stocks in play"
- News API integration for sentiment

**Phase 3: Strategy Engine**
- Backtesting framework with Alpaca data
- Opening Range Breakout (ORB) strategy
- Bracket orders for risk management
- Strategy parameter optimization
- Performance metrics and reporting

**Phase 4: Web Application**
- React/Vue frontend dashboard
- Real-time monitoring interface
- Strategy configuration UI
- Portfolio tracking
- P&L visualization

**Phase 5: AI Integration**
- Ollama-powered research assistant
- Chart pattern analysis
- News sentiment analysis with Alpaca News API
- Automated earnings research
- Trade signal generation

**Phase 6: Advanced Features**
- Crypto trading support
- Fractional shares
- Extended hours trading
- TradingView webhook integration
- Cloud deployment (AWS Lambda, Google Cloud Functions)

### Out of Scope (Initial Release)
- Live trading with real money (paper trading first)
- Options trading (Alpaca options coming soon)
- Futures and FX (not yet available on Alpaca)
- Multi-broker support (Alpaca only)
- Mobile application
- High-frequency trading (HFT) infrastructure

## Success Criteria
- Successfully execute paper trades via Alpaca API
- Backtest strategies with historical accuracy
- Real-time data displayed with <1 second latency via WebSocket
- AI assistant provides actionable market insights
- News sentiment analysis functional
- Clean collaboration workflow via GitHub
- Comprehensive documentation for all components
- Commission-free trading operational

## Target Users
- Yourself and your development partner
- Future: Other algorithmic traders (if open-sourced)
- Retail traders seeking commission-free automation
- Developers learning algorithmic trading

## Technology Alignment
Following Part Time Larry's proven Alpaca tech stack:
- **Backend**: Python, FastAPI/Flask
- **Broker API**: alpaca-trade-api (official Python SDK)
- **Market Data**: Alpaca Market Data API (WebSocket + REST)
- **Backtesting**: backtesting.py library with Alpaca data
- **Frontend**: React/Vue.js with TradingView charts
- **Real-time**: Alpaca WebSockets, Server-Sent Events (SSE)
- **AI**: Ollama (local LLMs) for research
- **News**: Alpaca News API for sentiment analysis
- **Database**: PostgreSQL or SQLite with TimescaleDB (for time-series)
- **Infrastructure**: Docker, Docker Compose
- **Cloud**: AWS Lambda, Google Cloud Functions (optional)
