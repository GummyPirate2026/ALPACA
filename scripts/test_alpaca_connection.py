#!/usr/bin/env python3
"""
Test Alpaca API Connection
This script verifies your Alpaca API credentials and displays account info.
"""

import os
import sys
from dotenv import load_dotenv

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_connection():
    """Test Alpaca API connection and display account info."""
    
    print("🦙 Testing Alpaca API Connection...\n")
    
    # Load environment variables
    load_dotenv()
    
    # Check if environment variables are set
    api_key = os.getenv('ALPACA_API_KEY')
    secret_key = os.getenv('ALPACA_SECRET_KEY')
    base_url = os.getenv('ALPACA_BASE_URL', 'https://paper-api.alpaca.markets')
    
    if not api_key or not secret_key:
        print("❌ Error: Alpaca API credentials not found!")
        print("\nPlease follow these steps:")
        print("1. Copy .env.example to .env")
        print("2. Add your Alpaca API keys to .env")
        print("3. Get keys from: https://app.alpaca.markets/paper/dashboard/overview")
        print("\nSee QUICKSTART.md for detailed instructions.")
        return False
    
    try:
        # Import Alpaca SDK
        from alpaca_trade_api import REST
        
        # Initialize API client
        api = REST(
            key_id=api_key,
            secret_key=secret_key,
            base_url=base_url
        )
        
        # Get account information
        account = api.get_account()
        
        # Display success message
        print("✅ Successfully connected to Alpaca!\n")
        
        # Display account info
        print("Account Info:")
        print(f"  Account ID: {account.id}")
        print(f"  Account Type: {'PAPER' if 'paper' in base_url else 'LIVE'}")
        print(f"  Status: {account.status}")
        print(f"  Buying Power: ${float(account.buying_power):,.2f}")
        print(f"  Cash: ${float(account.cash):,.2f}")
        print(f"  Portfolio Value: ${float(account.portfolio_value):,.2f}")
        
        # Check if trading is allowed
        if account.trading_blocked:
            print("\n⚠️  Warning: Trading is currently blocked on this account")
        
        # Display additional info
        print(f"\n📊 Additional Info:")
        print(f"  Day Trade Count: {account.daytrade_count}")
        print(f"  Pattern Day Trader: {account.pattern_day_trader}")
        
        # Test market data access
        print(f"\n📈 Testing Market Data API...")
        try:
            # Get a quote for SPY (S&P 500 ETF)
            quote = api.get_latest_quote('SPY')
            print(f"✅ Market data working! SPY: ${quote.bid_price} / ${quote.ask_price}")
        except Exception as e:
            print(f"⚠️  Market data test failed: {e}")
        
        print("\n✅ Alpaca connection test passed!")
        print("\n🎉 You're ready to start building!")
        print("\nNext steps:")
        print("1. Check out .masterplan.md for Phase 1 tasks")
        print("2. Review memory-bank/techContext.md for API patterns")
        print("3. Start with scripts/get_account_info.py")
        
        return True
        
    except ImportError:
        print("❌ Error: alpaca-trade-api not installed")
        print("\nPlease install dependencies:")
        print("  pip install -r requirements.txt")
        return False
        
    except Exception as e:
        print(f"❌ Error connecting to Alpaca: {e}")
        print("\nCommon issues:")
        print("1. Check API keys are correct (no extra spaces)")
        print("2. Make sure you're using paper trading keys")
        print("3. Verify base URL is https://paper-api.alpaca.markets")
        print("4. Check Alpaca status: https://alpaca.markets/status")
        return False


if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)
