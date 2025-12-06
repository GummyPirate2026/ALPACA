# System Patterns

## System Architecture

### High-Level Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                        Web Dashboard                        │
│              (React/Vue + TradingView Charts)               │
└────────────────┬────────────────────────────────────────────┘
                 │ HTTP/SSE
┌────────────────┴────────────────────────────────────────────┐
│                    Backend API Server                       │
│                   (FastAPI/Flask)                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │  REST API    │  │  SSE Stream  │  │  WebSocket   │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
└────┬────────────────┬─────────────────┬────────────────────┘
     │                │                 │
     ▼                ▼                 ▼
┌─────────┐    ┌──────────┐      ┌──────────────┐
│Database │    │ib_async  │      │  Ollama AI   │
│(SQLite/ │    │ (IBKR)   │      │   (Local)    │
│Postgres)│    └──────────┘      └──────────────┘
└─────────┘          │
                     ▼
              ┌─────────────┐
              │   TWS/IB    │
              │  Gateway    │
              └─────────────┘
```

### Component Architecture

**1. Data Layer**
- Historical data storage (OHLCV, ticks)
- Strategy parameters and configurations
- Trade history and performance metrics
- User settings and watchlists

**2. Market Data Service**
- Real-time quote subscription management
- Market scanner logic
- Data normalization and validation
- Caching layer for frequently accessed data

**3. Strategy Engine**
- Strategy class framework
- Backtesting engine (backtesting.py)
- Signal generation
- Position management
- Risk calculations

**4. Broker Interface**
- IBKR API wrapper (ib_async)
- Order management system (OMS)
- Position tracking
- Account information

**5. AI Service**
- Ollama API integration
- Chart analysis
- News sentiment processing
- Market research automation

**6. Web Application**
- Frontend SPA (Single Page Application)
- Real-time data visualization
- User authentication (future)
- Strategy configuration UI

## Key Technical Decisions

### 1. **Broker API: ib_async vs TWS API**
**Decision**: Use ib_async library
**Rationale**:
- Pythonic async/await interface
- Better error handling
- Active maintenance
- Proven by Part Time Larry
- Cleaner code than raw TWS API

### 2. **Backend Framework: FastAPI vs Flask**
**Decision**: FastAPI (recommended)
**Rationale**:
- Native async support for real-time data
- Automatic API documentation
- Type hints and validation
- Better performance for streaming
- Modern Python best practices

**Alternative**: Flask (simpler, well-documented)

### 3. **Database: PostgreSQL vs SQLite**
**Decision**: Start with SQLite, migrate to PostgreSQL if needed
**Rationale**:
- SQLite: Zero configuration, perfect for development
- PostgreSQL: Better for production, concurrent access
- Easy migration path

### 4. **Frontend: React vs Vue**
**Decision**: React (tentative)
**Rationale**:
- Larger ecosystem
- TradingView examples more common
- Better documentation
- Team preference should decide

### 5. **Real-time Communication: SSE vs WebSockets**
**Decision**: Server-Sent Events (SSE) for market data
**Rationale**:
- Simpler than WebSockets
- Unidirectional (server→client) is sufficient
- Auto-reconnection built-in
- Following Part Time Larry's approach

**Use WebSockets for**: Bidirectional features (future)

### 6. **Containerization Strategy**
**Decision**: Docker Compose for development
**Rationale**:
- Already have Docker setup
- Easy environment replication
- Isolates services (web, API, database)
- Simple for collaborator setup

## Design Patterns in Use

### 1. **Repository Pattern** (Data Access)
```python
class TradeRepository:
    """Abstracts database operations"""
    def get_trades_by_strategy(self, strategy_id)
    def save_trade(self, trade)
    def get_performance_metrics(self, date_range)
```

### 2. **Strategy Pattern** (Trading Algorithms)
```python
class Strategy(ABC):
    """Base class for all trading strategies"""
    @abstractmethod
    def generate_signal(self, data) -> Signal
    
    @abstractmethod
    def calculate_position_size(self, account, signal) -> int
```

### 3. **Observer Pattern** (Market Data)
```python
class MarketDataObserver:
    """Subscribes to market data updates"""
    def on_bar_update(self, bar)
    def on_tick(self, tick)
```

### 4. **Factory Pattern** (Strategy Creation)
```python
class StrategyFactory:
    """Creates strategy instances based on configuration"""
    def create_strategy(self, strategy_type, params) -> Strategy
```

### 5. **Singleton Pattern** (Broker Connection)
```python
class BrokerConnection:
    """Ensures single connection to IBKR API"""
    _instance = None
```

### 6. **Facade Pattern** (API Simplification)
```python
class TradingAPI:
    """Simplified interface to complex subsystems"""
    def get_market_scan(self) -> List[Stock]
    def place_order(self, symbol, quantity, order_type)
    def get_positions() -> List[Position]
```

## Component Relationships

### Data Flow: Real-Time Quotes
```
IBKR TWS/Gateway → ib_async client → Data Service → 
SSE Stream → Frontend → TradingView Chart
```

### Data Flow: Strategy Execution
```
Market Data → Strategy Engine → Signal Generation →
Risk Check → Order Management → IBKR API → Execution
```

### Data Flow: Backtesting
```
Historical Data (DB) → backtesting.py → Strategy Logic →
Performance Metrics → Results UI
```

### Data Flow: AI Research
```
User Query → Backend API → Ollama Service →
LLM Processing → Formatted Response → Frontend Display
```

## Critical Implementation Paths

### Path 1: From Market Open to First Trade
1. System starts, connects to IBKR TWS
2. Market data subscriptions activated
3. Scanner identifies setup (e.g., gap up stock)
4. Strategy receives data, generates signal
5. Risk management validates trade
6. Order placed via IBKR API
7. Execution confirmed
8. Position tracked in database

### Path 2: Real-Time Chart Update
1. IBKR sends tick/bar data
2. ib_async processes and normalizes
3. Data service caches and broadcasts
4. SSE pushes to connected clients
5. Frontend receives update
6. TradingView chart re-renders

### Path 3: Backtesting Workflow
1. User configures strategy and date range
2. Historical data loaded from database
3. backtesting.py iterates through bars
4. Strategy generates signals at each bar
5. Simulated orders executed with slippage
6. Performance metrics calculated
7. Equity curve and statistics displayed

### Path 4: AI Research Query
1. User asks: "What's the ORB setup for today?"
2. Request sent to backend API
3. System gathers: market scan data, pre-market movers
4. Data formatted for LLM context
5. Ollama processes with Llama 3.1 70B
6. Response formatted with actionable insights
7. Displayed in chat interface

## Error Handling Strategy

### 1. **Connection Failures**
- Automatic retry with exponential backoff
- Fallback to cached data when available
- Clear user notifications

### 2. **Order Rejections**
- Log detailed error information
- Notify user with reason
- Automatic cancellation of dependent orders

### 3. **Data Quality Issues**
- Validate all market data
- Flag suspicious values
- Skip bars with missing data in backtests

### 4. **System Overload**
- Rate limiting on API endpoints
- Queue system for order execution
- Graceful degradation of non-critical features

## Security Considerations

### 1. **API Key Management**
- Store in environment variables
- Never commit to git (.env in .gitignore)
- Rotate keys periodically

### 2. **Broker Authentication**
- Secure TWS connection
- Use dedicated paper trading account
- Limited permissions on API keys

### 3. **Local AI Privacy**
- All LLM processing local (Ollama)
- No market data sent to external APIs
- Strategy logic remains private

### 4. **Data Protection**
- Encrypt sensitive database fields (future)
- Secure session management (future)
- HTTPS for web interface (production)

## Performance Optimization

### 1. **Data Caching**
- In-memory cache for active quotes
- Redis for distributed caching (future)
- Database query optimization

### 2. **Async Operations**
- Non-blocking market data processing
- Concurrent strategy execution
- Parallel backtesting

### 3. **Database Indexing**
- Index on timestamp, symbol
- Optimize queries with EXPLAIN
- Partition large tables (future)

### 4. **Frontend Optimization**
- Lazy loading of chart data
- Virtualized lists for large datasets
- Debounced user inputs
