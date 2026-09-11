import heapq

class TriageQueue:
    def __init__(self):
        self._heap = []
        self._counter = 0  # tie-breaker untuk pasien yang tingkat keparahannya sama    

    def add_patient(self, severity, patient_name):
        heapq.heappush(self._heap, (-severity, self._counter, patient_name))
        self._counter += 1

    def treat_next_patient(self):
        if not self._heap:
            return None
        _, _, name = heapq.heappop(self._heap)
        return name

    def peek_next_patient(self):
        if not self._heap:
            return None
        return self._heap[0][2]

def main():
    triage = TriageQueue()

    triage.add_patient(9, "Aday")
    triage.add_patient(7, "Aden")
    triage.add_patient(5, "Fery")
    triage.add_patient(9, "Billy")
    triage.add_patient(7, "Andhika")
    triage.add_patient(8, "Dimas")
    triage.add_patient(6, "Rizky")
    triage.add_patient(5, "Rizal")
    triage.add_patient(4, "Eureka")
    triage.add_patient(1, "Zara")

    print(triage.peek_next_patient())

if __name__ == "__main__":
    main()