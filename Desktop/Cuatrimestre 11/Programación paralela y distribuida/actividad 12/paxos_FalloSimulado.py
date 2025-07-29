import random

class PaxosNode:
    def __init__(self, name):
        self.name = name
        self.promised_id = None
        self.accepted_id = None
        self.accepted_value = None

    def prepare(self, proposal_id):
        if self.name == "Node1":
            print(f"{self.name}: ❌ Nodo simula fallo (no responde en prepare)")
            return False
        if not self.promised_id or proposal_id > self.promised_id:
            self.promised_id = proposal_id
            print(f"{self.name}: ✔ Promise to {proposal_id}")
            return True
        print(f"{self.name}: ❌ Rechaza prepare {proposal_id}")
        return False

    def accept(self, proposal_id, value):
        if self.name == "Node1":
            print(f"{self.name}: ❌ Nodo simula fallo (no responde en accept)")
            return False
        if not self.promised_id or proposal_id >= self.promised_id:
            self.promised_id = proposal_id
            self.accepted_id = proposal_id
            self.accepted_value = value
            print(f"{self.name}: ✔ Accepted {value} con id {proposal_id}")
            return True
        print(f"{self.name}: ❌ Rechaza accept {value} con id {proposal_id}")
        return False


nodes = [PaxosNode(f"Node{i}") for i in range(3)]


proposal_id = random.randint(1, 100)
value = "A=1"

print(f"\n🟡 Propuesta: id={proposal_id}, valor='{value}'\n")

# Fase 1: Prepare
promises = [n.prepare(proposal_id) for n in nodes]

# Fase 2: Accept si hay mayoría
if promises.count(True) >= 2:
    accepts = [n.accept(proposal_id, value) for n in nodes]
    if accepts.count(True) >= 2:
        print(f"\n✅ Valor '{value}' ha sido acordado por mayoría.\n")
    else:
        print(f"\n❌ No se alcanzó mayoría en fase Accept.\n")
else:
    print(f"\n❌ No se alcanzó mayoría en fase Prepare.\n")
