# Deployment Guide

## Deployment Options

### 1. Local Development

\`\`\`bash
# Install dependencies
pip install -r requirements.txt

# Run orchestrator
python scripts/run_orchestrator.py
\`\`\`

### 2. Docker

\`\`\`bash
# Build image
docker build -t voidinium:latest .

# Run container
docker run -d \
  -p 8000:8000 \
  -e VOIDINIUM_MODE=zk \
  -e PRIVACY_LEVEL=maximum \
  voidinium:latest
\`\`\`

### 3. Docker Compose

\`\`\`bash
# Start all services
docker-compose -f deployment/docker-compose.yml up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
\`\`\`

### 4. Kubernetes

\`\`\`bash
# Apply configurations
kubectl apply -f deployment/kubernetes/

# Check status
kubectl get pods -l app=voidinium

# View logs
kubectl logs -l app=voidinium -f

# Scale deployment
kubectl scale deployment voidinium-orchestrator --replicas=3
\`\`\`

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `VOIDINIUM_MODE` | Runtime mode (tee/zk/hybrid) | `zk` |
| `PRIVACY_LEVEL` | Privacy level | `high` |
| `SWARM_SIZE` | Number of agents | `5` |
| `IPFS_NODE_URL` | IPFS node URL | `http://localhost:5001` |
| `LOG_LEVEL` | Logging level | `INFO` |

## Resource Requirements

### Minimum

- CPU: 2 cores
- RAM: 4 GB
- Storage: 20 GB

### Recommended

- CPU: 8 cores
- RAM: 16 GB
- Storage: 100 GB
- Network: 1 Gbps

### Production

- CPU: 16+ cores
- RAM: 32+ GB
- Storage: 500+ GB
- Network: 10 Gbps

## Monitoring

### Health Checks

\`\`\`bash
# Check orchestrator health
curl http://localhost:8000/health

# Check agent health
curl http://localhost:8001/health
\`\`\`

### Metrics

- Prometheus metrics exposed on `/metrics`
- Grafana dashboards available
- Custom alerting rules

## Security Considerations

1. Use TLS for all external communications
2. Implement proper firewall rules
3. Enable audit logging
4. Regular security updates
5. Use secrets management
6. Implement backup strategies

## Backup & Recovery

### Backup

\`\`\`bash
# Backup data volume
docker run --rm \
  -v voidinium_data:/data \
  -v $(pwd):/backup \
  alpine tar czf /backup/voidinium-backup.tar.gz /data
\`\`\`

### Recovery

\`\`\`bash
# Restore from backup
docker run --rm \
  -v voidinium_data:/data \
  -v $(pwd):/backup \
  alpine tar xzf /backup/voidinium-backup.tar.gz -C /
\`\`\`

## Troubleshooting

### Common Issues

**Issue**: Orchestrator won't start
- Check logs: `docker logs voidinium-orchestrator`
- Verify environment variables
- Check port availability

**Issue**: Agents can't connect
- Verify network connectivity
- Check orchestrator URL
- Review firewall rules

**Issue**: Performance degradation
- Monitor resource usage
- Check swarm size
- Review logs for errors

## Support

For deployment assistance:
- Documentation: docs.voidinium.io
- GitHub Issues: github.com/voidinium/voidinium/issues
- Discord: discord.gg/voidinium
\`\`\`

\`\`\`text file="requirements.txt"
# Core dependencies
asyncio-mqtt>=0.16.1
cryptography>=41.0.0
pydantic>=2.0.0
python-dotenv>=1.0.0

# Cryptography and ZK
py-ecc>=6.0.0
coincurve>=18.0.0

# Networking
aiohttp>=3.9.0
websockets>=12.0

# Storage
py-ipfs-http-client>=0.8.0a2

# Machine Learning (for federated learning)
numpy>=1.24.0
scikit-learn>=1.3.0

# Testing
pytest>=7.4.0
pytest-asyncio>=0.21.0
pytest-cov>=4.1.0

# Development
black>=23.0.0
flake8>=6.0.0
mypy>=1.5.0
