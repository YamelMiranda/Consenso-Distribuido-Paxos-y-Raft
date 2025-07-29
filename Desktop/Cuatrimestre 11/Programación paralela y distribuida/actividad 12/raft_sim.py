import time
import random

class RaftNode:
    def __init__(self, name):
        self.name = name
        self.state = "follower"
        self.term = 0
        self.voted = False

    def request_vote(self):
        print(f"{self.name}: solicito votos para ser líder (término {self.term})")
        votes = 1  # se vota a sí mismo
        for peer in peers:
            if peer != self and peer.vote(self.term):
                votes += 1
        if votes >= 2:
            self.state = "leader"
            print(f"{self.name}: ¡Soy el líder con {votes} votos!")
            return True
        print(f"{self.name}: No fui elegido líder.")
        return False

    def vote(self, term):
        if not self.voted:
            self.voted = True
            print(f"{self.name}: voto por el candidato para el término {term}")
            return True
        return False

    def replicate_log(self, entry):
        print(f"{self.name}: replicando entrada '{entry}' a seguidores")
        for peer in peers:
            if peer != self:
                peer.receive(entry)

    def receive(self, entry):
        print(f"{self.name}: recibí la entrada '{entry}' del líder")

# Simulación
nodes = [RaftNode(f"N{i}") for i in range(3)]
peers = nodes

# Elección de líder
random.choice(nodes).request_vote()

# Replicación del valor
leader = next((n for n in nodes if n.state == "leader"), None)
if leader:
    leader.replicate_log("A=1")
