import random
import time

class PaxosNode:
    def __init__(self, name):
        self.name = name
        self.promised_id = None
        self.accepted_id = None
        self.accepted_value = None

    def prepare(self, proposal_id):
        if not self.promised_id or proposal_id > self.promised_id:
            self.promised_id = proposal_id
            print(f"{self.name}: Promise to {proposal_id}")
            return True
        print(f"{self.name}: Reject {proposal_id}")
        return False
    

    def accept(self, proposal_id, value):
        if not self.promised_id or proposal_id >= self.promised_id:
            self.promised_id = proposal_id
            self.accepted_id = proposal_id
            self.accepted_value = value
            print(f"{self.name}: Accepted {value} with id {proposal_id}")
            return True
        print(f"{self.name}: Reject accept {value} with id {proposal_id}")
        return False


nodes = [PaxosNode(f"Node{i}") for i in range(3)]


proposal_id = random.randint(1, 100)
value = "A=1"

# Fase prepare
promises = [n.prepare(proposal_id) for n in nodes]

# Fase accept
if promises.count(True) >= 2:
    accepts = [n.accept(proposal_id, value) for n in nodes]
    if accepts.count(True) >= 2:
        print(f"✔ Valor '{value}' ha sido acordado por mayoría.")
