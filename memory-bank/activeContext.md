# Active Context

## Current Work Focus
**Phase 0: Project Initialization & Setup**

Setting up the foundational infrastructure for the algorithmic trading platform. Currently establishing the project structure, documentation, and collaboration framework inspired by Part Time Larry's tutorials.

## Recent Changes
- ✅ Initialized Git repository
- ✅ Created comprehensive Memory Bank documentation structure
- ✅ Set up .gitignore for Python, trading data, and API keys
- ✅ Defined system architecture following Part Time Larry's patterns
- ✅ Documented technology stack and development setup
- ⏳ Creating .masterplan.md for development roadmap
- ⏳ Setting up GitHub collaboration files

## Next Steps
- [ ] Create .masterplan.md with detailed phase breakdown
- [ ] Set up README.md with project overview and setup instructions
- [ ] Create CONTRIBUTING.md for collaboration guidelines
- [ ] Create .env.example template
- [ ] Set up project directory structure (src/, tests/, frontend/, etc.)
- [ ] Create requirements.txt with initial dependencies
- [ ] Initialize Python virtual environment
- [ ] Install Interactive Brokers TWS/Gateway (paper trading)
- [ ] Test IBKR API connection with simple script
- [ ] Set up GitHub repository and push initial commit

## Active Decisions and Considerations

### 1. **Backend Framework Choice**
**Current Lean**: FastAPI
- Modern async support crucial for real-time data
- Automatic API documentation
- Better for SSE streaming
- Part Time Larry uses it in recent videos

**Decision Point**: Confirm with team after basic prototype

### 2. **Frontend Framework**
**Options**: React vs Vue
- React has more TradingView integration examples
- Vue might be simpler for quick iterations
- Should align with team's existing knowledge

**Decision Point**: Decide before Phase 4 (Web Interface)

### 3. **Database Choice**
**Current Plan**: SQLite for development
- Zero configuration
- Easy to version control (small DB)
- Can migrate to PostgreSQL later

**Migration Point**: When concurrent write issues appear

### 4. **IBKR Account Setup**
**Required**: Paper trading account
- Need to apply if not already have one
- TWS vs IB Gateway (Gateway is headless, better for automation)
- Must enable API access in account settings

**Decision Point**: Before Phase 1 implementation

### 5. **TradingView Charting Library**
**Licensing**: TradingView library requires commercial license for production
- Can use during development
- Need to evaluate licensing costs before production
- Alternative: Build custom charting with Plotly/D3.js

**Decision Point**: Before Phase 2 completion

## Important Patterns and Preferences

### Code Organization
```
trading-app/
├── src/
│   ├── api/          # FastAPI endpoints
│   ├── brokers/      # IBKR integration
│   ├── strategies/   # Trading strategies
│   ├── data/         # Data models and database
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

### Git Workflow
- `main` branch: Production-ready code
- `develop` branch: Active development
- `feature/*` branches: New features
- `bugfix/*` branches: Bug fixes
- Pull requests required for main branch
- Descriptive commit messages

### Development Practices
- **Test-Driven Development**: Write tests before implementation
- **Type Hints**: Use Python type annotations
- **Documentation**: Docstrings for all functions
- **Code Review**: All PRs reviewed by collaborator
- **Incremental Commits**: Small, focused commits

### API Design Principles
- RESTful endpoints for CRUD operations
- SSE for real-time market data streams
- WebSockets for bidirectional features (future)
- Consistent error responses
- API versioning (/api/v1/)

## Learnings and Project Insights

### From Part Time Larry Content

**1. IBKR Integration Best Practices**
- Use ib_async for cleaner async code
- Always handle disconnections gracefully
- Maintain single connection instance
- Implement proper error handling for order rejections

**2. Real-Time Data Handling**
- Server-Sent Events simpler than WebSockets for one-way data
- Browser has built-in SSE reconnection
- Keep data payloads small for responsiveness
- Use caching to reduce API calls

**3. TradingView Integration**
- Custom datafeed implementation required
- UDF (Universal Data Format) is standard
- Historical data must support multiple timeframes
- Real-time updates via JavaScript callbacks

**4. Strategy Development**
- Keep strategies simple and testable
- Separate strategy logic from execution
- Use backtesting.py for validation
- Always paper trade before live execution

**5. Market Scanners**
- Pre-market volume and gap analysis crucial
- Multiple criteria reduce false positives
- Update frequency: every 1-5 seconds
- Store scanner results for analysis

### Technical Insights

**1. Async Python Patterns**
- FastAPI's async endpoints for non-blocking operations
- ib_async handles IBKR connection asynchronously
- Use asyncio.gather() for parallel operations
- Beware of blocking operations in async contexts

**2. Database Design**
- Normalize data for storage efficiency
- Denormalize for query performance
- Index heavily queried fields (timestamp, symbol)
- Partition large tables by date

**3. AI Integration Strategy**
- Local Ollama avoids external API costs
- Llama 3.1 70B provides good analysis quality
- Structure prompts for consistent outputs
- Cache repeated queries to save processing time

**4. Development Speed vs Quality**
- MVP first: Get basic functionality working
- Iterate: Add features based on actual usage
- Test automation: Saves time in long run
- Documentation: Write it while building, not after

### Risk Management Considerations

**1. Paper Trading First**
- Never test new strategies with real money
- Paper trading has limitations (fill guarantees)
- Track paper vs live performance differences

**2. Position Sizing**
- Start with small sizes
- Implement max position limits
- Account for portfolio heat (total risk exposure)

**3. Error Handling**
- All order operations must have error handling
- Log all errors for review
- Implement circuit breakers for repeated failures

**4. Data Quality**
- Validate all incoming market data
- Handle missing or delayed data gracefully
- Store raw data for debugging

## Current Blockers
None at the moment. All infrastructure decisions are clear and setup can proceed.

## Team Collaboration Notes

### Roles (Tentative)
- **You**: Full-stack development, strategy implementation
- **Partner**: TBD (based on their strengths)

### Communication
- Use GitHub Issues for feature requests and bugs
- Use GitHub Projects board for task tracking
- Regular sync meetings (frequency TBD)
- Document decisions in Memory Bank

### Work Distribution Strategy
- Divide by components (frontend/backend)
- Or divide by features (complete feature ownership)
- Pair programming for complex components
- Code review for all contributions

## Project Momentum Tracker

**Week 1 Goals** (Current):
- ✅ Project initialization
- ✅ Documentation structure
- ⏳ GitHub setup
- ⏳ Development environment setup
- ⏳ Basic IBKR connection test

**Week 2 Goals** (Upcoming):
- [ ] Complete Phase 1: Foundation
- [ ] IBKR API integration working
- [ ] Database schema defined
- [ ] Basic REST API endpoints
- [ ] First successful market data retrieval

**Month 1 Goals**:
- [ ] Phases 1-2 complete
- [ ] Real-time market data streaming
- [ ] TradingView charts displaying data
- [ ] Basic market scanner functional
- [ ] First strategy framework created
