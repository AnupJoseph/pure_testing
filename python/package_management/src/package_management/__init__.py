import argparse


def start_app():
    parser = argparse.ArgumentParser(description="Start the app")
    parser.add_argument("--port", type=int, help="Port Number")
    args = parser.parse_args()
    print(f"App started at port {args.port}")
