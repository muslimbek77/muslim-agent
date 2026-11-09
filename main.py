
from agent import MuslimAgent


def main():
    """Application entry point."""
    try:
        agent = MuslimAgent()
        agent.run()
    except Exception as error:
        print(f"Startup error: {error}")


if __name__ == "__main__":
    main()
