import random

class RaftNode:
    def __init__(self, name):
        self.name = name
        self.state = "follower"
        self.term = 0
        self.voted = False

    def request_vote(self):
        print(f"{self.name}: 🗳️ Solicita votos para ser líder (término {self.term})")
        votes = 1  # se vota a sí mismo
        for peer in peers:
            if peer != self and peer.vote(self.term):
                votes += 1
        if votes >= 2:
            self.state = "leader"
            print(f"{self.name}: ✅ Soy el líder con {votes} votos\n")
            return True
        print(f"{self.name}: ❌ No fui elegido líder\n")
        return False

    def vote(self, term):
        if self.name == "N2":
            print(f"{self.name}: ❌ Nodo simula fallo (no vota)")
            return False
        if not self.voted:
            self.voted = True
            print(f"{self.name}: ✔ Voto por el candidato en término {term}")
            return True
        return False

    def replicate_log(self, entry):
        print(f"{self.name}: 🔁 Replicando entrada '{entry}' a seguidores")
        for peer in peers:
            if peer != self:
                if peer.name == "N2":
                    print(f"{peer.name}: ❌ Nodo simula fallo (no recibe entrada)")
                    continue
                peer.receive(entry)

    def receive(self, entry):
        print(f"{self.name}: 📥 Recibí la entrada '{entry}' del líder")

# Crear nodos
nodes = [RaftNode(f"N{i}") for i in range(3)]
peers = nodes

# Elección de líder
random.choice(nodes).request_vote()

# Replicación del valor
leader = next((n for n in nodes if n.state == "leader"), None)
if leader:
    leader.replicate_log("A=1")
else:
    print("⚠️ No se eligió líder, no se puede replicar el valor.")
