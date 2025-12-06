# Project Brief

## Project Name
Algorithmic Trading Platform (inspired by Part Time Larry)

## Overview
A full-stack algorithmic trading application that combines real-time market data, automated trading strategies, AI-powered research, and comprehensive backtesting capabilities. The platform integrates broker APIs (Interactive Brokers), provides real-time market scanning, implements proven trading strategies, and leverages local AI (Ollama) for market analysis and research.

## Core Requirements
- **Real-time Market Data**: Live quotes, streaming data, market scanners
- **Broker Integration**: Interactive Brokers API (ib_async) for trading execution
- **Chart Visualization**: TradingView charts with real-time updates
- **Strategy Engine**: Backtesting framework and automated strategy execution
- **Web Interface**: Full-stack web application for monitoring and control
- **AI Research Assistant**: Local Ollama integration for market analysis
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
- IBKR API integration and authentication
- Real-time data streaming architecture
- Database setup for historical data storage
- Basic web server with API endpoints

**Phase 2: Market Data & Visualization**
- TradingView chart integration
- Real-time quote display
- Market scanner for "stocks in play"
- Server-Sent Events (SSE) for live updates

**Phase 3: Strategy Engine**
- Backtesting framework (backtesting.py)
- Opening Range Breakout (ORB) strategy
- Strategy parameter optimization
- Performance metrics and reporting

**Phase 4: Web Application**
- React/Vue frontend dashboard
- Real-time monitoring interface
- Strategy configuration UI
- Portfolio tracking

**Phase 5: AI Integration**
- Ollama-powered research assistant
- Chart pattern analysis
- News sentiment analysis
- Automated earnings research

### Out of Scope (Future Phases)
- Live trading with real money (paper trading first)
- Options and derivatives trading
- Multi-broker support (start with IBKR only)
- Mobile application
- Advanced risk management systems
- High-frequency trading (HFT) infrastructure

## Success Criteria
- Successfully execute paper trades via IBKR API
- Backtest strategies with historical accuracy
- Real-time data displayed with <1 second latency
- AI assistant provides actionable market insights
- Clean collaboration workflow via GitHub
- Comprehensive documentation for all components

## Target Users
- Yourself and your development partner
- Future: Other algorithmic traders (if open-sourced)

## Technology Alignment
Following Part Time Larry's proven tech stack:
- **Backend**: Python, FastAPI/Flask
- **Broker API**: ib_async (Interactive Brokers)
- **Backtesting**: backtesting.py library
- **Frontend**: React/Vue.js with TradingView charts
- **Real-time**: Server-Sent Events (SSE), WebSockets
- **AI**: Ollama (local LLMs) for research
- **Database**: PostgreSQL or SQLite
- **Infrastructure**: Docker, Docker Compose
