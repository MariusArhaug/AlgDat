
class Queue:
    Q = []
    tail = 0
    head = 0
    def __init__(self, max_size):
        # Initialiser de underliggende datastrukturene her
        Q = [None for _ in range(max_size)]
        
        tail = 0
        head = 0

    def enqueue(self, value):
       # Skriv kode for Enqueue operasjonen
        self.Q[self.tail] = value
        if tail == len(self.Q):
            tail = 1
        else:
            tail = tail + 1
            
            

    def dequeue(self):
        # Skriv kode for Dequeue operasjonen
        x = self.Q[self.tail]
        if head == len(self.Q):
            head = 1
        else:
            head += 1
        return x

highscore = True

def tester(values, sequence, max_size):
    """
    Tester en oppgitt sekvens av operasjoner og sjekker at verdiene
    (values) kommer ut i riktig rekkefølge.
    """
    index = 0
    queue = Queue(max_size)
    output = []
    for action in sequence:
        if action == "enqueue":
            queue.enqueue(values[index])
            index += 1
        elif action == "dequeue":
            output.append(queue.dequeue())

    if output != values:
        print(
            "Feilet for følgende sekvens av operasjoner "
            + "'{:}' med verdiene ".format(", ".join(sequence))
            + "'{:}' og maksimal størrelse".format(", ".join(map(str, values)))
            + "'{:}'".format(max_size)
        )
        return True
    return False


tests = (
    (
        [1, 7, 3],
        ("enqueue", "dequeue", "enqueue", "dequeue", "enqueue", "dequeue"),
        3,
    ),
    (
        [1, 7, 3],
        ("enqueue", "dequeue", "enqueue", "dequeue", "enqueue", "dequeue"),
        1,
    ),
    (
        [-1, 12, 0, 99],
        (
            "enqueue",
            "enqueue",
            "dequeue",
            "dequeue",
            "enqueue",
            "enqueue",
            "dequeue",
            "dequeue",
        ),
        2,
    ),
    (
        [-1, 12, 0, 99],
        (
            "enqueue",
            "enqueue",
            "dequeue",
            "enqueue",
            "dequeue",
            "enqueue",
            "dequeue",
            "dequeue",
        ),
        2,
    ),
    (
        [-1, 12, 0, 99],
        (
            "enqueue",
            "enqueue",
            "enqueue",
            "enqueue",
            "dequeue",
            "dequeue",
            "dequeue",
            "dequeue",
        ),
        4,
    ),
)

failed = False

for values, sequence, max_size in tests:
    failed |= tester(values, sequence, max_size)

if not failed:
    print("Koden din fungerte for alle eksempeltestene.")