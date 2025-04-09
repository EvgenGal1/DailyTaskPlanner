import subprocess

def main():
    subprocess.run(["alembic", "upgrade", "head"])

if __name__ == "__main__":
    main()