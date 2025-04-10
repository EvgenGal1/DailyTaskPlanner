import subprocess

def main():
    subprocess.run(["alembic", "revision", "--autogenerate", "-m", "init"])

if __name__ == "__main__":
    main()