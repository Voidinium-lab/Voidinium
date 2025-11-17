"""
Example: Simple Zero-Knowledge Computation
"""

import asyncio
from Voidinium.crypto import ZKProofSystem


async def main():
    print("🔐 Simple Zero-Knowledge Computation Example\n")
    
    # Create ZK proof system
    zk = ZKProofSystem(proof_type="snark")
    
    # Define statement and witness
    statement = {"claim": "I know x such that hash(x) = y"}
    witness = {"x": "secret_value"}
    
    # Generate proof
    print("Generating zero-knowledge proof...")
    proof = await zk.generate_proof(statement, witness)
    print(f"✅ Proof generated: {proof[:64]}...\n")
    
    # Verify proof
    print("Verifying proof without revealing witness...")
    is_valid = await zk.verify_proof(statement, proof)
    print(f"✅ Proof valid: {is_valid}\n")
    
    print("Privacy preserved! The verifier learned nothing about 'x'")


if __name__ == "__main__":
    asyncio.run(main())
