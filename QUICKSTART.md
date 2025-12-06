# ALPACA Quick Start Guide

## Step 1: Get Your Alpaca API Keys (30 seconds!)

### Sign Up for Alpaca Paper Trading

1. **Go to**: https://alpaca.markets
2. **Click**: "Get Started" or "Sign Up"
3. **Fill in**: Email, password, basic info
4. **Verify**: Email address
5. **Done!** You now have instant access to paper trading

### Get Your API Keys

1. **Login** to https://app.alpaca.markets
2. **Click** on your profile icon (top right)
3. **Go to**: "Paper Trading" in the sidebar
4. **Click**: "Generate" or "View" API Keys
5. **Copy**: 
   - API Key ID
   - Secret Key

> ⚠️ **Important**: Keep your Secret Key safe! Never share it or commit it to git.

## Step 2: Configure Your Environment

### Create .env File

```bash
# In your project directory
cp .env.example .env
```

### Add Your API Keys

Open `.env` in your editor and update:

```bash
# Replace with YOUR actual keys
ALPACA_API_KEY=PK... your key here
ALPACA_SECRET_KEY=... your secret here
ALPACA_BASE_URL=https://paper-api.alpaca.markets
```

**Example**:
```bash
ALPACA_API_KEY=PKABCDEFG123456789
ALPACA_SECRET_KEY=abcdefghijklmnop1234567890
ALPACA_BASE_URL=https://paper-api.alpaca.markets
```

## Step 3: Set Up Python Environment

### Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# Or on Windows:
# venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Test Your Connection

### Run the Test Script

```bash
python scripts/test_alpaca_connection.py
```

### Expected Output

```
🦙 Testing Alpaca API Connection...
✅ Successfully connected to Alpaca!

Account Info:
  Account ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  Account Type: PAPER
  Status: ACTIVE
  Buying Power: $100,000.00
  Cash: $100,000.00
  Portfolio Value: $100,000.00

✅ Alpaca connection test passed!
```

## Step 5: Verify Everything Works

### Quick Checklist

- [ ] Signed up at alpaca.markets
- [ ] Got API keys from dashboard
- [ ] Created .env file with keys
- [ ] Activated virtual environment
- [ ] Installed dependencies
- [ ] Ran test script successfully
- [ ] Saw account info displayed

## Common Issues

### Issue: "pip: command not found"

**Solution**: Try `pip3` instead of `pip`

```bash
pip3 install -r requirements.txt
```

### Issue: "ModuleNotFoundError: No module named 'alpaca_trade_api'"

**Solution**: Make sure virtual environment is activated

```bash
source venv/bin/activate  # Run this first
pip install -r requirements.txt
```

### Issue: "APIError: Unauthorized"

**Solution**: Check your API keys in .env

1. Make sure you copied them correctly
2. No extra spaces
3. Using paper trading keys (not live keys)

### Issue: "No such file or directory: .env"

**Solution**: Copy the template first

```bash
cp .env.example .env
# Then edit .env with your keys
```

## What's Next?

Once your connection test passes, you're ready for Phase 1 development:

1. **Explore the API** - Get market data, positions, orders
2. **Historical Data** - Download bars for backtesting
3. **WebSocket Streaming** - Real-time quotes
4. **Place Orders** - Test bracket orders in paper trading
5. **Build Strategy** - Start implementing ORB strategy

## API Key Security Best Practices

### ✅ DO:
- Keep keys in .env file (git ignored)
- Use paper trading keys for development
- Rotate keys if accidentally exposed
- Use environment variables in production

### ❌ DON'T:
- Commit .env to git
- Share keys in screenshots
- Use live keys for testing
- Hard-code keys in source code

## Useful Alpaca Resources

### Documentation
- **Trading API**: https://alpaca.markets/docs/trading/
- **Market Data API**: https://alpaca.markets/docs/market-data/
- **Python SDK**: https://github.com/alpacahq/alpaca-trade-api-python

### Dashboard
- **Paper Trading**: https://app.alpaca.markets/paper/dashboard/overview
- **API Keys**: https://app.alpaca.markets/paper/dashboard/overview

### Support
- **Status Page**: https://alpaca.markets/status
- **Forum**: https://forum.alpaca.markets/
- **Documentation**: https://alpaca.markets/docs/

## Need Help?

1. Check the error message in the test script output
2. Review [memory-bank/techContext.md](memory-bank/techContext.md) for troubleshooting
3. Check Alpaca's status page: https://alpaca.markets/status
4. Review Part Time Larry's Alpaca tutorials

---

**You're ready to start building! 🚀**

Once the test passes, check out `.masterplan.md` for your Phase 1 development plan.
