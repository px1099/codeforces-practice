import heapq
from dataclasses import dataclass, field
from typing import Any, List


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)


class PriorityQueue:
    def __init__(self, queue: List[PrioritizedItem] = None, max_queue: bool = False):
        self.queue = queue or []
        heapq.heapify(self.queue)
        self.max_queue = max_queue

    def __len__(self):
        return len(self.queue)

    def push(self, item: Any, priority: int = 0):
        priority = -1 * priority if self.max_queue else priority
        heapq.heappush(self.queue, PrioritizedItem(priority, item))

    def pop(self):
        prioritized_item = heapq.heappop(self.queue)
        item = prioritized_item.item
        priority = prioritized_item.priority
        priority = -1 * priority if self.max_queue else priority
        return item, priority

    def head(self):
        prioritized_item = self.queue[0]
        item = prioritized_item.item
        priority = prioritized_item.priority
        priority = -1 * priority if self.max_queue else priority
        return item, priority


def solve():
    pass


if __name__ == "__main__":
    tc = 1
    # tc = int(input())
    for _ in range(tc):
        solve()
