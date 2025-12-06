# Active Context

## Current Work Focus
**Phase 0: Complete - Ready for Phase 1**

Successfully pivoted the algorithmic trading platform from Interactive Brokers to Alpaca. All documentation, architecture, and technology stack have been updated to leverage Alpaca's commission-free trading API, WebSocket streaming, and News API. The project is now ready to begin Phase 1: Alpaca API integration and development.

## Recent Changes
- ✅ Successfully deployed initial project to GitHub (GummyPirate2026/ALPACA)
- ✅ Created comprehensive Memory Bank documentation structure
- ✅ Initialized Git repository with proper .gitignore
- ✅ Set up Docker Compose for Open WebUI + Ollama
- ✅ **Completed pivot from IBKR to Alpaca API**
- ✅ Updated all 6 Memory Bank files for Alpaca integration
- ✅ Created requirements.txt with alpaca-trade-api SDK
- ✅ Updated .env.example with Alpaca API key configuration
- ✅ Updated README.md with comprehensive Alpaca features
- ✅ Committed and pushed all changes to GitHub (commit 61d3e7a)

## Next Steps
- [ ] Sign up for Alpaca paper trading account at alpaca.markets
- [ ] Get API keys from Alpaca dashboard (instant access)
- [ ] Set up Python virtual environment
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Configure .env with Alpaca API keys
- [ ] Test basic Alpaca API connection
- [ ] Create first data retrieval script
- [ ] Begin Phase 1: Full Alpaca API integration

## Active Decisions and Considerations

### 1. **Broker Choice: Alpaca vs IBKR**
**Decision**: Switched to Alpaca
**Reasoning**: 
- Simpler API (REST-based vs TWS/Gateway)
- Instant paper trading access (no account approval)
- Commission-free trading
- Better Python SDK (alpaca-trade-api)
- More Part Time Larry tutorials (20+ videos)
- Built-in WebSocket streaming
- News API for sentiment analysis
- Easier for beginners

**Trade-offs Accepted**:
- No futures, options (yet)
- No international markets
- Less advanced order types
- Higher latency than IBKR (not HFT-suitable)

### 2. **Alpaca SDK: alpaca-trade-api vs alpaca-py**
**Current Plan**: Use alpaca-trade-api initially
- More mature and stable
- Better documentation
- More examples from Part Time Larry
- Can migrate to alpaca-py later

**Migration Point**: After Phase 3 (if needed)

### 3. **Market Data: Free (IEX) vs Paid (SIP)**
**Current Plan**: Start with free IEX data
- Sufficient for development and backtesting
- No cost barrier to entry
- Slight delay acceptable for learning

**Upgrade Point**: Before live trading or if latency critical

### 4. **Database Choice**
**Current Plan**: SQLite for development
- Zero configuration
- Easy to version control (small DB)
- Consider TimescaleDB (PostgreSQL extension) for time-series data

**Migration Point**: When concurrent write issues appear

### 5. **Project Name: ALPACA**
**Decision**: Perfect match for the broker!
- Repository already named correctly
- Clear indication of broker integration
- Easy to remember and communicate

## Important Patterns and Preferences

### Code Organization (Alpaca-Specific)
```
trading-app/
├── src/
│   ├── api/          # FastAPI endpoints
│   ├── alpaca/       # Alpaca API integration
│   ├── strategies/   # Trading strategies
│   ├── data/         # Database models
│   ├── ai/           # Ollama integration
│   └── utils/        # Shared utilities
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── frontend/         # React/Vue app
├── scripts/          # Utility scripts
├── docs/             # Additional documentation
└── memory-bank/      # Project documentation
```

### Alpaca API Patterns
```python
# Connection pattern
from alpaca_trade_api import REST

api = REST(
    key_id=ALPACA_API_KEY,
    secret_key=ALPACA_SECRET_KEY,
    base_url='https://paper-api.alpaca.markets'
)

# WebSocket streaming pattern
from alpaca_trade_api.stream import Stream

stream = Stream(key_id=KEY, secret_key=SECRET)

@stream.on_trade
async def on_trade(data):
    process_trade(data)
```

### Git Workflow (Alpaca Branch Strategy)
- `main` branch: Production-ready code
- `develop` branch: Active Alpaca development
- `feature/alpaca-*` branches: Alpaca-specific features
- `feature/*` branches: General features
- Pull requests required for main branch
- Descriptive commit messages with Alpaca context

### Development Practices
- **Test with Paper Trading First**: Always use paper API
- **WebSocket Connection Management**: Handle disconnects gracefully
- **Rate Limit Awareness**: Monitor Alpaca API rate limits
- **Market Hours**: Respect trading hours (9:30 AM - 4:00 PM ET)
- **Type Hints**: Use Python type annotations
- **Documentation**: Document Alpaca-specific quirks
- **Code Review**: All PRs reviewed by collaborator

## Learnings and Project Insights

### From Part Time Larry Alpaca Content

**1. Alpaca API Best Practices**
- Use paper trading URL: `https://paper-api.alpaca.markets`
- Keep API keys in environment variables
- Handle WebSocket reconnection automatically
- Use bracket orders for risk management
- Monitor account buying power before orders

**2. Real-Time Data Handling with Alpaca**
- WebSocket provides trade, quote, and bar updates
- Subscribe only to needed symbols (avoid rate limits)
- IEX data is free but slightly delayed
- SIP data costs but is real-time and consolidated
- Handle market closed periods gracefully

**3. Alpaca News API Integration**
- Real-time news with sentiment scores
- Filter by symbol for targeted news
- Sentiment: -1 (bearish) to +1 (bullish)
- Combine with technical analysis for better signals

**4. Strategy Development with Alpaca**
- Backtesting works well with Alpaca historical data
- Paper trading fills are simulated (may differ from live)
- Use bracket orders (entry + profit target + stop loss)
- Test during market hours for realistic behavior
- Monitor slippage in paper vs live

**5. Alpaca Advantages**
- Instant API access (no waiting for approval)
- Commission-free (no trading costs)
- Fractional shares supported
- Extended hours trading available
- Crypto trading integrated (BTC, ETH, etc.)
- News API included

### Technical Insights

**1. Alpaca WebSocket Patterns**
- Separate connections for trading and data
- Automatic reconnection with exponential backoff
- Subscribe/unsubscribe dynamically
- Handle authentication errors gracefully

**2. Database Design for Trading**
- Store raw Alpaca bar data
- Normalize for multiple timeframes
- Index on timestamp and symbol
- Consider partitioning by date

**3. Alpaca + Ollama Integration Strategy**
- Use Ollama to analyze news sentiment
- Generate trading ideas from market scans
- Explain strategy decisions
- Summarize market conditions
- No external API costs!

**4. Development Speed with Alpaca**
- Faster setup than IBKR (no TWS install)
- Better documentation and examples
- Simpler authentication (just API keys)
- More beginner-friendly error messages

### Risk Management with Alpaca

**1. Paper Trading First**
- Test all strategies in paper trading
- Verify order execution logic
- Monitor for unexpected behavior
- Track performance metrics

**2. Bracket Orders**
- Always include profit target
- Always include stop loss
- Let Alpaca handle exit automatically
- Reduces emotional decision making

**3. Position Sizing**
- Check account buying power
- Implement max position limits
- Account for portfolio heat (total risk exposure)
- Start small, scale up gradually

**4. Data Quality**
- Validate all incoming market data
- Handle missing or delayed data
- Store raw data for debugging
- Monitor WebSocket connection health

## Current Blockers
None at the moment. Alpaca pivot is progressing smoothly. All infrastructure decisions are clear.

## Team Collaboration Notes

### Roles (Tentative)
- **You**: Full-stack development, Alpaca integration
- **Partner**: TBD (based on their strengths and interests)

### Communication
- Use GitHub Issues for feature requests and bugs
- Use GitHub Projects board for task tracking
- Regular sync meetings (frequency TBD)
- Document Alpaca-specific decisions in Memory Bank

### Work Distribution Strategy
- Divide by components (frontend/backend)
- Or divide by features (complete feature ownership)
- Pair programming for complex Alpaca integrations
- Code review for all contributions

## Project Momentum Tracker

**Week 1 Goals** (Current):
- ✅ Project initialization
- ✅ Documentation structure
- ✅ GitHub setup
- ⏳ Pivot to Alpaca
- ⏳ Update all documentation
- ⏳ Create requirements.txt

**Week 2 Goals** (Upcoming):
- [ ] Sign up for Alpaca paper trading
- [ ] Test basic Alpaca API connection
- [ ] Set up Python environment with Alpaca SDK
- [ ] Create first Alpaca data retrieval script
- [ ] Set up database schema for Alpaca data

**Month 1 Goals**:
- [ ] Phases 0-2 complete
- [ ] Real-time Alpaca data streaming functional
- [ ] TradingView charts displaying Alpaca data
- [ ] Basic market scanner operational
- [ ] First strategy framework created
- [ ] Paper trades successfully executed

## Alpaca-Specific Notes

### Account Setup
- Sign up at: https://alpaca.markets
- Get paper trading API keys instantly
- No account approval needed
- Test connection immediately

### Key URLs
- **Paper Trading API**: https://paper-api.alpaca.markets
- **Live Trading API**: https://api.alpaca.markets (future)
- **Documentation**: https://alpaca.markets/docs/
- **Status Page**: https://alpaca.markets/status
- **Dashboard**: https://app.alpaca.markets

### Rate Limits
- Free tier: 200 WebSocket messages/minute
- REST API: Generally 200 requests/minute
- Monitor usage to avoid throttling

### Data Feed Options
- **IEX** (free): Slightly delayed, good for development
- **SIP** (paid): Real-time consolidated tape
- Choose based on use case and budget
