import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        rgb_path = sys.argv[1]
        depth_path = sys.argv[2]
        # Simulate the Rust executable's output format
        print(f"Processed 3D model from {rgb_path} and {depth_path}")
    else:
        print("Usage: python mock_rust_runner.py <rgb_path> <depth_path>", file=sys.stderr)
        sys.exit(1)
