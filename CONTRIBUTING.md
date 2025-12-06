# Contributing to Algorithmic Trading Platform

Thank you for your interest in contributing to this project! This is a learning-focused collaborative project for building algorithmic trading infrastructure.

## 🎯 Project Goals

- Build a production-ready algorithmic trading platform
- Learn quantitative trading concepts and implementation
- Follow best practices in software engineering
- Maintain comprehensive documentation
- Foster collaboration and knowledge sharing

## 📋 Getting Started

### 1. Read the Documentation
- **[README.md](README.md)** - Project overview
- **[.masterplan.md](.masterplan.md)** - Development roadmap
- **[memory-bank/](memory-bank/)** - Project context and decisions

### 2. Set Up Your Environment
```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/trading-app.git
cd trading-app

# Set up Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Install pre-commit hooks (future)
pre-commit install
```

### 3. Pick a Task
- Check [GitHub Issues](https://github.com/YOUR_USERNAME/trading-app/issues)
- Review [.masterplan.md](.masterplan.md) for current phase tasks
- Ask questions in [Discussions](https://github.com/YOUR_USERNAME/trading-app/discussions)

## 🔄 Development Workflow

### Branch Strategy
```
main           (production-ready code)
  └── develop  (active development)
       ├── feature/your-feature-name
       ├── bugfix/issue-description
       └── docs/documentation-update
```

### Making Changes

1. **Create a Branch**
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**
   - Write code following our standards (see below)
   - Add tests for new functionality
   - Update documentation as needed
   - Follow the style guide

3. **Test Your Changes**
   ```bash
   # Run tests
   pytest tests/
   
   # Run linting
   black src/ tests/
   flake8 src/ tests/
   
   # Run type checking
   mypy src/
   ```

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add market scanner feature"
   ```

5. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a Pull Request on GitHub.

## 📝 Commit Message Convention

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples
```bash
feat(scanner): add pre-market gap scanner
fix(ibkr): handle connection timeout errors
docs(readme): update installation instructions
test(strategy): add ORB strategy unit tests
```

## 🎨 Code Style Guidelines

### Python

**Follow PEP 8** with these specifics:

```python
# Use type hints
def calculate_position_size(account: Account, risk: float) -> int:
    """Calculate position size based on account and risk."""
    return int(account.balance * risk)

# Use docstrings
class Strategy:
    """Base class for all trading strategies.
    
    Attributes:
        params: Strategy parameters
        signals: Generated trading signals
    """
    pass

# Use meaningful variable names
# Good
opening_range_high = max(bars[:15])

# Bad
orh = max(bars[:15])
```

**Code Formatting**:
- Use `black` for formatting (line length: 88)
- Use `flake8` for linting
- Use `mypy` for type checking
- Sort imports with `isort`

### JavaScript/TypeScript (Frontend)

```javascript
// Use ES6+ features
const fetchQuote = async (symbol) => {
  const response = await api.get(`/quotes/${symbol}`);
  return response.data;
};

// Use meaningful names
// Good
const isMarketOpen = checkMarketHours();

// Bad
const flag = check();
```

## 🧪 Testing Guidelines

### Write Tests For
- All new features
- Bug fixes
- Critical business logic
- API endpoints
- Strategy calculations

### Test Structure
```python
# tests/unit/test_strategy.py
import pytest
from src.strategies import ORBStrategy

def test_orb_signal_generation():
    """Test that ORB strategy generates correct signals."""
    strategy = ORBStrategy(params={"opening_range": 15})
    
    # Setup test data
    bars = create_test_bars()
    
    # Execute
    signal = strategy.generate_signal(bars)
    
    # Assert
    assert signal.action == "BUY"
    assert signal.price > strategy.or_high
```

### Test Coverage
- Aim for >80% code coverage
- Focus on critical paths first
- Use fixtures for common test data

## 📚 Documentation Guidelines

### Code Documentation
```python
def backtest_strategy(strategy: Strategy, data: pd.DataFrame, 
                      start_date: date, end_date: date) -> BacktestResult:
    """Run backtest for a strategy over specified date range.
    
    Args:
        strategy: Trading strategy to test
        data: Historical market data
        start_date: Backtest start date
        end_date: Backtest end date
        
    Returns:
        BacktestResult with performance metrics
        
    Raises:
        ValueError: If date range is invalid
        DataError: If required data is missing
        
    Example:
        >>> result = backtest_strategy(orb, data, date(2024,1,1), date(2024,12,31))
        >>> print(result.sharpe_ratio)
        1.85
    """
    pass
```

### Memory Bank Updates
When making architectural decisions:
1. Document in relevant `memory-bank/` file
2. Update `progress.md` with status
3. Note in `activeContext.md` if currently relevant

## 🔍 Code Review Process

### For Authors
- Ensure tests pass
- Write clear PR description
- Link related issues
- Request specific feedback if needed
- Respond to reviewer comments

### For Reviewers
- Review within 24-48 hours
- Check code quality and style
- Verify tests pass
- Suggest improvements kindly
- Approve or request changes

### PR Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
How has this been tested?

## Checklist
- [ ] Tests pass locally
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] No new warnings
```

## 🐛 Reporting Bugs

### Before Reporting
1. Check existing issues
2. Verify it's reproducible
3. Test with latest code

### Bug Report Template
```markdown
**Describe the bug**
Clear description of what the bug is.

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
- OS: [e.g., macOS 14]
- Python version: [e.g., 3.10.5]
- Branch: [e.g., develop]

**Additional context**
Any other context about the problem.
```

## 💡 Suggesting Features

### Feature Request Template
```markdown
**Is your feature request related to a problem?**
Clear description of the problem.

**Describe the solution you'd like**
Clear description of desired solution.

**Describe alternatives**
Alternatives you've considered.

**Additional context**
Any other context or screenshots.

**Phase Alignment**
Which phase does this fit into? (see .masterplan.md)
```

## 📦 Dependencies

### Adding New Dependencies
1. Discuss in issue/PR first
2. Add to `requirements.txt` with version
3. Update documentation
4. Consider bundle size (frontend)

### Updating Dependencies
1. Check for breaking changes
2. Update tests if needed
3. Document changes in PR

## 🔐 Security

### Reporting Security Issues
**DO NOT** open public issues for security vulnerabilities.

Email: [your-email@domain.com]

### Security Best Practices
- Never commit API keys or secrets
- Use environment variables
- Keep dependencies updated
- Follow authentication best practices
- Validate all user inputs

## 🤝 Community Guidelines

### Be Respectful
- Welcome newcomers
- Provide constructive feedback
- Assume good intentions
- Help others learn

### Be Professional
- Keep discussions on-topic
- Avoid off-topic debates
- Respect different skill levels
- Share knowledge generously

## 📞 Communication

### Channels
- **GitHub Issues**: Bug reports, features
- **GitHub Discussions**: General questions
- **Pull Requests**: Code review
- **Memory Bank**: Project decisions

### Response Times
- Issues: 24-48 hours
- PRs: 24-48 hours for initial review
- Discussions: Best effort

## 🎓 Learning Resources

### For New Contributors
- [Part Time Larry YouTube](https://www.youtube.com/@parttimelarry)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Git Workflow](https://guides.github.com/introduction/flow/)

### For Trading Concepts
- Check `memory-bank/` documentation
- Watch Part Time Larry tutorials
- Review strategy implementations in `src/strategies/`

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Thank You!

Your contributions help make this project better for everyone. Whether it's code, documentation, bug reports, or suggestions - every contribution is valued!

---

**Questions?** Open a [Discussion](https://github.com/YOUR_USERNAME/trading-app/discussions) or check [memory-bank/](memory-bank/) documentation.

_Last Updated: 2025-12-06_
