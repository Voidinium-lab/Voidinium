# API Reference

## Core Classes

### VoidiniumOrchestrator

Main orchestrator for coordinating swarm intelligence.

\`\`\`python
class VoidiniumOrchestrator:
    def __init__(
        self,
        mode: str = "zk",
        swarm_size: int = 5,
        privacy_level: str = "high"
    )
\`\`\`

**Parameters**:
- `mode`: Runtime mode ("tee", "zk", "hybrid")
- `swarm_size`: Number of agents in swarm
- `privacy_level`: Privacy protection level ("standard", "high", "maximum")

**Methods**:

#### initialize_swarm()
\`\`\`python
async def initialize_swarm()
\`\`\`
Initialize the swarm of secure agents.

#### execute()
\`\`\`python
async def execute(workflow: PrivateWorkflow) -> Dict
\`\`\`
Execute a private workflow across the swarm.

**Returns**: Execution result with ZK proof

#### shutdown()
\`\`\`python
async def shutdown()
\`\`\`
Gracefully shutdown the swarm.

---

### PrivateWorkflow

Defines a privacy-preserving workflow.

\`\`\`python
class PrivateWorkflow:
    def __init__(
        self,
        name: str,
        agents: List[str],
        privacy_constraints: Optional[Dict] = None
    )
\`\`\`

**Parameters**:
- `name`: Workflow identifier
- `agents`: List of agent names to execute workflow
- `privacy_constraints`: Optional privacy requirements

---

### ZKProofSystem

Zero-knowledge proof generation and verification.

\`\`\`python
class ZKProofSystem:
    def __init__(self, proof_type: str = "snark")
\`\`\`

**Methods**:

#### generate_proof()
\`\`\`python
async def generate_proof(
    statement: Dict,
    witness: Dict
) -> str
\`\`\`
Generate a zero-knowledge proof.

#### verify_proof()
\`\`\`python
async def verify_proof(
    statement: Dict,
    proof: str
) -> bool
\`\`\`
Verify a zero-knowledge proof.

---

### FederatedTrainer

Train models using federated learning.

\`\`\`python
class FederatedTrainer:
    def __init__(
        self,
        model: str,
        nodes: int,
        encryption: str = "homomorphic"
    )
\`\`\`

**Methods**:

#### train_federated()
\`\`\`python
async def train_federated() -> Dict
\`\`\`
Train model across distributed nodes with privacy.

---

### IPFSClient

Interface to IPFS for decentralized storage.

\`\`\`python
class IPFSClient:
    def __init__(self, node_url: str = "http://localhost:5001")
\`\`\`

**Methods**:

#### add()
\`\`\`python
async def add(data: bytes, encrypt: bool = True) -> str
\`\`\`
Add encrypted data to IPFS.

**Returns**: Content identifier (CID)

#### get()
\`\`\`python
async def get(cid: str) -> Optional[bytes]
\`\`\`
Retrieve data from IPFS.

## Environment Variables

- `VOIDINIUM_MODE`: Runtime mode (default: "zk")
- `PRIVACY_LEVEL`: Privacy level (default: "high")
- `SWARM_SIZE`: Number of agents (default: 5)
- `IPFS_NODE_URL`: IPFS node URL (default: "http://localhost:5001")
