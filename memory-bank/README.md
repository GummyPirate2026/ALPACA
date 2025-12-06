# Memory Bank

This folder contains the Cline Memory Bank - a structured documentation system that allows Cline to maintain context across sessions.

## Files Overview

1. **projectbrief.md** - Foundation document with core requirements and goals
2. **productContext.md** - Why this project exists and problems it solves
3. **activeContext.md** - Current work focus and recent changes (updated frequently)
4. **systemPatterns.md** - System architecture and technical decisions
5. **techContext.md** - Technologies, setup, and dependencies
6. **progress.md** - Current status, what works, and what's left to build

## How to Use

### Starting a New Session
Ask Cline to **"follow your custom instructions"** - this tells Cline to read the Memory Bank files and continue where you left off.

### During Development
Cline will automatically update these files as you work. You can also request updates with **"update memory bank"**.

### Next Steps
1. Fill in the `projectbrief.md` with your project details
2. Update other files as your project develops
3. Let Cline help maintain these files as you work together

## File Hierarchy

```
projectbrief.md (foundation)
    ├── productContext.md
    ├── systemPatterns.md
    └── techContext.md
            └── activeContext.md
                    └── progress.md
```

---

*Memory Bank initialized on 2025-12-06*
