import environs

env = environs.Env()
env.read_env("./.env")

api_id = env.int("API_ID")
bot_token = env.str("BOT_TOKEN", "5929961201:AAEAp5CMfcAlpRxE47hkui9D6-RgRrZYaaI")
api_hash = env.str("API_HASH")
BOTLOG_CHATID = env.int("BOTLOG_CHATID", 0)
db_type = env.str("DATABASE_TYPE")
db_url = env.str("DATABASE_URL", "")
db_name = env.str("DATABASE_NAME")
test_server = env.bool("TEST_SERVER", False)
modules_repo_branch = env.str("MODULES_REPO_BRANCH", "main")
