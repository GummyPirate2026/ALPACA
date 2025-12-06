# System Patterns

## System Architecture

### High-Level Architecture
```
┌─────────────────────────────────────────────────────────┐
│                    Web Browser                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Dashboard  │  │ TradingView  │  │  AI Chat     │  │
│  │   (React)    │  │   Charts     │  │  Interface   │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────┬───────────────────────────────────────────┘
              │ HTTP/SSE/WebSocket
┌─────────────▼───────────────────────────────────────────┐
│              FastAPI Backend (Python)                    │
│  ┌────────────┐  ┌────────────┐  ┌────────────────────┐│
│  │    API     │  │  Strategy  │  │   Alpaca Client    ││
│  │  Endpoints │  │   Engine   │  │   (alpaca-trade-   ││
│  │            │  │            │  │      api)          ││
│  └────────────┘  └────────────┘  └────────────────────┘│
│                                                          │
│  ┌────────────┐  ┌────────────┐  ┌────────────────────┐│
│  │   Ollama   │  │  Database  │  │   Market Data      ││
│  │  Client    │  │  Manager   │  │   Manager          ││
│  └────────────┘  └────────────┘  └────────────────────┘│
└─────────────┬───────────────────────────┬───────────────┘
              │                           │
    ┌─────────▼──────────┐    ┌──────────▼────────────┐
    │  Ollama (Local)    │    │  Alpaca API           │
    │  Llama 3.1 70B     │    │  - Trading API        │
    │  http://localhost  │    │  - Market Data API    │
    │      :11434        │    │  - News API           │
    └────────────────────┘    │  - WebSocket Streams  │
                              └───────────────────────┘
```

### Component Relationships

#### 1. **Alpaca Integration Layer**
```
AlpacaClient
    ├── TradingAPI (REST)
    │   ├── get_account()
    │   ├── submit_order()
    │   ├── list_positions()
    │   └── cancel_order()
    │
    ├── MarketDataAPI (REST)
    │   ├── get_bars()
    │   ├── get_latest_quote()
    │   ├── get_snapshot()
    │   └── get_news()
    │
    └── StreamingAPI (WebSocket)
        ├── subscribe_trades()
        ├── subscribe_quotes()
        ├── subscribe_bars()
        └── subscribe_news()
```

#### 2. **Strategy Engine**
```
StrategyEngine
    ├── Strategy Base Class
    ├── Backtesting Framework
    ├── Signal Generator
    ├── Risk Manager
    └── Order Manager
        └── Uses AlpacaClient for execution
```

#### 3. **Data Pipeline**
```
Alpaca WebSocket → StreamHandler → Database
                        ↓
                   Strategy Engine
                        ↓
                   Order Manager
                        ↓
                   Alpaca Trading API
```

## Key Technical Decisions

### 1. **Alpaca as Primary Broker**
**Decision**: Use Alpaca Trading API instead of Interactive Brokers
**Rationale**:
- Simpler REST-based API (vs TWS/Gateway complexity)
- Instant paper trading access (no account approval)
- Commission-free trading
- Official Python SDK (alpaca-trade-api)
- Built-in WebSocket streaming
- News API with sentiment
- Better for learning

**Implementation**:
```python
from alpaca_trade_api import REST, Stream

# Initialize clients
trading_api = REST(
    key_id=ALPACA_API_KEY,
    secret_key=ALPACA_SECRET_KEY,
    base_url='https://paper-api.alpaca.markets'
)

stream = Stream(
    key_id=ALPACA_API_KEY,
    secret_key=ALPACA_SECRET_KEY,
    base_url='https://paper-api.alpaca.markets'
)
```

### 2. **WebSocket for Real-Time Data**
**Decision**: Use Alpaca WebSocket API for streaming data
**Rationale**:
- Built into Alpaca API
- Lower latency than polling
- Real-time trade, quote, and bar updates
- Handles reconnection automatically

**Implementation Pattern**:
```python
@stream.on_trade
async def on_trade(trade):
    # Process trade data
    await process_trade(trade)

@stream.on_quote  
async def on_quote(quote):
    # Process quote data
    await process_quote(quote)

# Subscribe to symbols
stream.subscribe_trades(['AAPL', 'TSLA', 'SPY'])
stream.subscribe_quotes(['AAPL', 'TSLA', 'SPY'])

# Run stream
stream.run()
```

### 3. **Bracket Orders for Risk Management**
**Decision**: Use Alpaca bracket orders for automated exits
**Rationale**:
- Profit target and stop loss in one order
- Server-side execution (no connection needed)
- Reduces emotional decision making
- Simplifies risk management code

**Implementation**:
```python
api.submit_order(
    symbol='AAPL',
    qty=100,
    side='buy',
    type='market',
    time_in_force='day',
    order_class='bracket',
    take_profit=dict(limit_price=150.00),
    stop_loss=dict(stop_price=140.00)
)
```

### 4. **Paper Trading First**
**Decision**: All development and testing on paper trading
**Rationale**:
- Zero financial risk
- Unlimited paper trading with Alpaca
- Test strategies thoroughly
- Same API as live trading

**Configuration**:
```python
# Paper trading
base_url = 'https://paper-api.alpaca.markets'

# Live trading (future)
# base_url = 'https://api.alpaca.markets'
```

### 5. **FastAPI for Async Performance**
**Decision**: Use FastAPI instead of Flask
**Rationale**:
- Native async/await support
- Better for WebSocket handling
- Automatic API documentation
- Type hints and validation
- High performance

### 6. **SQLite for Development**
**Decision**: Start with SQLite, migrate to PostgreSQL later
**Rationale**:
- Zero configuration
- Good enough for development
- Easy to version control
- Can migrate later when needed

### 7. **Ollama for Local AI**
**Decision**: Use Ollama with Llama 3.1 70B locally
**Rationale**:
- Complete privacy
- No API costs
- Already installed
- Sufficient quality
- Works offline

## Design Patterns

### 1. **Repository Pattern (Data Access)**
```python
class AlpacaRepository:
    def __init__(self, api_client: REST):
        self.api = api_client
    
    async def get_account(self) -> Account:
        return self.api.get_account()
    
    async def get_positions(self) -> List[Position]:
        return self.api.list_positions()
    
    async def submit_order(self, order: Order) -> OrderResponse:
        return self.api.submit_order(**order.dict())
```

### 2. **Strategy Pattern (Trading Strategies)**
```python
class Strategy(ABC):
    @abstractmethod
    def generate_signal(self, data: pd.DataFrame) -> Signal:
        pass

class ORBStrategy(Strategy):
    def generate_signal(self, data: pd.DataFrame) -> Signal:
        # Opening Range Breakout logic
        or_high = data.iloc[:15]['high'].max()
        or_low = data.iloc[:15]['low'].min()
        current_price = data.iloc[-1]['close']
        
        if current_price > or_high:
            return Signal(action='BUY', price=current_price)
        elif current_price < or_low:
            return Signal(action='SELL', price=current_price)
        
        return Signal(action='HOLD')
```

### 3. **Observer Pattern (Market Data)**
```python
class MarketDataObserver(ABC):
    @abstractmethod
    async def on_trade(self, trade: Trade):
        pass
    
    @abstractmethod
    async def on_quote(self, quote: Quote):
        pass

class StrategyObserver(MarketDataObserver):
    async def on_trade(self, trade: Trade):
        signal = self.strategy.generate_signal(trade)
        if signal.action == 'BUY':
            await self.order_manager.place_order(signal)
```

### 4. **Factory Pattern (Order Creation)**
```python
class OrderFactory:
    @staticmethod
    def create_bracket_order(
        symbol: str,
        qty: int,
        entry_price: float,
        profit_target: float,
        stop_loss: float
    ) -> Dict:
        return {
            'symbol': symbol,
            'qty': qty,
            'side': 'buy',
            'type': 'limit',
            'limit_price': entry_price,
            'time_in_force': 'day',
            'order_class': 'bracket',
            'take_profit': {'limit_price': profit_target},
            'stop_loss': {'stop_price': stop_loss}
        }
```

### 5. **Singleton Pattern (Alpaca Client)**
```python
class AlpacaClient:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.api = REST(
                key_id=ALPACA_API_KEY,
                secret_key=ALPACA_SECRET_KEY,
                base_url='https://paper-api.alpaca.markets'
            )
        return cls._instance
```

## Critical Implementation Paths

### Path 1: Real-Time Market Data Flow
```
1. Alpaca WebSocket connects
   ↓
2. Subscribe to symbols
   ↓
3. Receive trade/quote updates
   ↓
4. Validate and normalize data
   ↓
5. Store in database
   ↓
6. Notify strategy engine
   ↓
7. Update frontend via SSE
```

### Path 2: Order Execution Flow
```
1. Strategy generates signal
   ↓
2. Risk manager validates
   ↓
3. Position sizer calculates qty
   ↓
4. Order factory creates bracket order
   ↓
5. Submit to Alpaca API
   ↓
6. Log order details
   ↓
7. Monitor via Alpaca updates
   ↓
8. Handle fills/rejections
```

### Path 3: Backtesting Flow
```
1. Load Alpaca historical data
   ↓
2. Initialize strategy
   ↓
3. Iterate through bars
   ↓
4. Generate signals
   ↓
5. Simulate execution
   ↓
6. Track performance
   ↓
7. Calculate metrics
   ↓
8. Display results
```

### Path 4: AI Research Flow
```
1. User asks question
   ↓
2. Fetch relevant data (Alpaca API)
   ↓
3. Format prompt
   ↓
4. Send to Ollama
   ↓
5. Process response
   ↓
6. Format for display
   ↓
7. Show to user
```

## Error Handling Patterns

### 1. **Alpaca API Errors**
```python
from alpaca_trade_api.rest import APIError

try:
    order = api.submit_order(...)
except APIError as e:
    if e.status_code == 403:
        logger.error("Insufficient buying power")
    elif e.status_code == 422:
        logger.error("Invalid order parameters")
    else:
        logger.error(f"API error: {e}")
```

### 2. **WebSocket Reconnection**
```python
class AlpacaStreamHandler:
    async def handle_disconnect(self):
        attempt = 1
        while attempt <= MAX_RETRIES:
            try:
                await self.reconnect()
                logger.info("Reconnected successfully")
                break
            except Exception as e:
                wait_time = min(2 ** attempt, 60)
                logger.warning(f"Reconnect attempt {attempt} failed, "
                              f"waiting {wait_time}s")
                await asyncio.sleep(wait_time)
                attempt += 1
```

### 3. **Market Hours Handling**
```python
def check_market_hours():
    clock = api.get_clock()
    
    if not clock.is_open:
        next_open = clock.next_open
        logger.info(f"Market closed, opens at {next_open}")
        return False
    
    return True
```

## Performance Patterns

### 1. **Async Data Processing**
```python
async def process_bars_batch(symbols: List[str]):
    tasks = [fetch_bars(symbol) for symbol in symbols]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results
```

### 2. **Caching Strategy**
```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_symbol_info(symbol: str):
    return api.get_asset(symbol)
```

### 3. **Database Connection Pooling**
```python
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10
)
```

## Security Patterns

### 1. **API Key Management**
```python
from dotenv import load_dotenv
import os

load_dotenv()

ALPACA_API_KEY = os.getenv('ALPACA_API_KEY')
ALPACA_SECRET_KEY = os.getenv('ALPACA_SECRET_KEY')

# Never log secrets
logger.info(f"Using API key: {ALPACA_API_KEY[:8]}...")
```

### 2. **Input Validation**
```python
from pydantic import BaseModel, validator

class OrderRequest(BaseModel):
    symbol: str
    qty: int
    side: str
    
    @validator('side')
    def validate_side(cls, v):
        if v not in ['buy', 'sell']:
            raise ValueError('side must be buy or sell')
        return v
    
    @validator('qty')
    def validate_qty(cls, v):
        if v <= 0:
            raise ValueError('qty must be positive')
        return v
```

## Testing Patterns

### 1. **Alpaca API Mocking**
```python
from unittest.mock import Mock, patch

@patch('alpaca_trade_api.REST')
def test_order_submission(mock_api):
    mock_api.submit_order.return_value = Mock(id='order123')
    
    result = order_manager.place_order('AAPL', 100, 'buy')
    
    assert result.id == 'order123'
    mock_api.submit_order.assert_called_once()
```

### 2. **Strategy Backtesting**
```python
def test_orb_strategy():
    # Load test data from Alpaca
    bars = api.get_bars('AAPL', '1Min', start='2024-01-01')
    
    strategy = ORBStrategy(opening_range=15)
    signals = strategy.backtest(bars)
    
    assert len(signals) > 0
    assert all(s.action in ['BUY', 'SELL', 'HOLD'] for s in signals)
```

## Alpaca-Specific Best Practices

### 1. **Use Bracket Orders**
Always include stop loss and profit target:
```python
api.submit_order(
    symbol='AAPL',
    qty=100,
    side='buy',
    type='market',
    time_in_force='day',
    order_class='bracket',
    take_profit={'limit_price': profit_target},
    stop_loss={'stop_price': stop_loss}
)
```

### 2. **Check Buying Power**
Before placing orders:
```python
account = api.get_account()
if float(account.buying_power) < required_capital:
    logger.warning("Insufficient buying power")
    return False
```

### 3. **Handle Market Hours**
```python
clock = api.get_clock()
if not clock.is_open:
    logger.info("Market is closed")
    return
```

### 4. **Monitor Rate Limits**
```python
# Alpaca limits: ~200 requests/minute
time.sleep(0.3)  # Between API calls if looping
```

### 5. **Use News API for Sentiment**
```python
news = api.get_news(symbol='AAPL', limit=10)
for article in news:
    sentiment = article.sentiment  # -1 to +1
    logger.info(f"{article.headline}: {sentiment}")
```
