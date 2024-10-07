import subprocess, time

def wait_for_postgres(host: str, max_retries: int = 5, delay_seconds: int = 5) -> bool:
    retries=0
    while retries < max_retries:
        try:
            result = subprocess.run(
                ["pg_isready", "-h", host], check=True, capture_output=True, text=True
            )
            if "accepting conditions" in result.stdout:
                print ("Successfully connected to Postgres")
                return
        except subprocess.CalledProcessError as err:
            print(f"Error connecting to Postgres with error: {err}")
            retries += 1
            print(f"Retrying in {delay_seconds} seconds... Attempt number: {retries}")
            time.sleep(delay_seconds)
    print("Max retries reached. Exiting")
    return False

if not wait_for_postgres(host="source_postgres"):
    exit(1)

print("Starting ELT Script")

source_config = {
    'dbname': 'source_db',
    'user': 'postgres',
    'password': 'secret',
    'host': 'source_postgres'
}

destination_config = {
    'dbname': 'destination_db',
    'user': 'postgres',
    'password': 'secret',
    'host': 'destination_db'
}

dump_command = [
    'pg_dump',
    '-h', source_config['host'],
    '-u', source_config['user'],
    '-d', source_config['dbname'],
    '-f', 'data_dump.sql',
    '-w'
]

subprocess_env = dict(PGPASSWORD=source_config['password'])

subprocess.run(dump_command, env=subprocess_env, check=True)


load_command = [
    'psql',
    '-h', destination_config['host'],
    '-u', destination_config['user'],
    '-d', destination_config['dbname'],
    '-a', '-f', 'data_dump.sql',
    '-w'
]

subprocess_env = dict(PGPASSWORD=destination_config['password'])

subprocess.run(load_command, env=subprocess_env, check=True)

print("Ending ELT Script")