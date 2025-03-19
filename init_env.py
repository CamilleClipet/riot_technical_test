import os
import secrets

from dotenv import load_dotenv


def generate_secret_key() -> str:
    secret_key = secrets.token_bytes(32)
    return secret_key.hex()


def create_or_update_env() -> None:
    env_file = ".env"

    if not os.path.exists(env_file):
        print(f"{env_file} does not exist. Creating it...")

    secret_key = generate_secret_key()

    env_content = f"PYTHONPATH=.\nSECRET_KEY={secret_key}\n"

    with open(env_file, "w") as file:
        file.write(env_content)

    print(f"Created or updated {env_file} with PYTHONPATH and SECRET_KEY.")

    load_dotenv()


# Main entry point
if __name__ == "__main__":
    create_or_update_env()
