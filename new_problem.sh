#!/bin/bash

# Check for argument
if [ -z "$1" ]; then
    echo "Usage: $0 <problem_number>"
    exit 1
fi

# Format number with leading zeros (e.g., 5 -> 005)
NUM=$(printf "%03d" "$1")
DIR="solvers/p${NUM}"

# Create directories
mkdir -p "${DIR}/python"

# Create solver.py with boilerplate content
cat > "${DIR}/python/solver.py" << EOF
import time


def main():
    pass  # TODO


if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f"Finished in {elapsed_time:.3f} seconds.")
EOF

echo "Created ${DIR}/python/solver.py"
