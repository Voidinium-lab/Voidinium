# Getting Started with Voidinium

## Introduction

Voidinium is a zero-knowledge orchestrated swarm intelligence platform that enables privacy-preserving collaborative computation. This guide will help you get started quickly.

## Prerequisites

Before you begin, ensure you have:

- Python 3.9 or higher
- pip package manager
- Docker (optional, for containerized deployment)
- Git

## Installation

### Option 1: Local Installation

\`\`\`bash
# Clone the repository
git clone https://github.com/yourusername/voidinium.git
cd voidinium

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -c "import Voidinium; print(Voidinium.__version__)"
\`\`\`

### Option 2: Docker Installation

\`\`\`bash
# Build the Docker image
docker build -t voidinium:latest .

# Run the container
docker run -p 8000:8000 voidinium:latest
\`\`\`

### Option 3: Docker Compose

\`\`\`bash
# Start all services
docker-compose -f deployment/docker-compose.yml up
\`\`\`

## Quick Start

### 1. Run Your First Swarm

\`\`\`python
from Voidinium import VoidiniumOrchestrator

# Create orchestrator
orchestrator = VoidiniumOrchestrator(
    mode="zk",
    swarm_size=5,
    privacy_level="maximum"
)

# Initialize
await orchestrator.initialize_swarm()
\`\`\`

### 2. Execute a Private Workflow

\`\`\`python
from Voidinium import PrivateWorkflow

# Define workflow
workflow = PrivateWorkflow(
    name="secure_analytics",
    agents=["processor", "analyzer"]
)

# Execute
result = await orchestrator.execute(workflow)
print(f"Status: {result['status']}")
\`\`\`

### 3. Run Example Scripts

\`\`\`bash
# Run orchestrator demo
python scripts/run_orchestrator.py

# Run federated learning demo
python scripts/run_federated_learning.py
\`\`\`

## Next Steps

- Read the [Architecture Overview](./architecture.md)
- Explore [Examples](../examples)
- Check out the [API Reference](./api-reference.md)
- Learn about [Security Model](./security.md)

## Getting Help

- Documentation: [docs.voidinium.io](https://docs.voidinium.io)
- GitHub Issues: [github.com/voidinium/voidinium/issues](https://github.com/voidinium/voidinium/issues)
- Discord: [discord.gg/voidinium](https://discord.gg/voidinium)
