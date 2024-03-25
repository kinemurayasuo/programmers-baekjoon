import sys
from collections import deque

def main():
    N = int(sys.stdin.readline().strip())  # 명령의 수
    queue = deque()

    output = []
    for _ in range(N):
        command = sys.stdin.readline().split()
        if command[0] == "push":
            queue.append(int(command[1]))
        elif command[0] == "pop":
            if queue:
                output.append(queue.popleft())
            else:
                output.append(-1)
        elif command[0] == "size":
            output.append(len(queue))
        elif command[0] == "empty":
            output.append(0 if queue else 1)
        elif command[0] == "front":
            output.append(queue[0] if queue else -1)
        elif command[0] == "back":
            output.append(queue[-1] if queue else -1)

    sys.stdout.write('\n'.join(map(str, output)))

if __name__ == "__main__":
    main()