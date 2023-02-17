import environs

env = environs.Env()
env.read_env("./.env")

api_id = env.int("API_ID")
bot_token = env.str("BOT_TOKEN")
api_hash = env.str("API_HASH")
BOTLOG_CHATID = env.int("BOTLOG_CHATID")
db_type = env.str("DATABASE_TYPE")
db_url = env.str("DATABASE_URL", "")
db_name = env.str("DATABASE_NAME")
MONGO_URL = env.str("MONGO_URL")
OPENAI_API = env.str("OPENAI_API")
GIT_TOKEN = env.str("GIT_TOKEN", "") #personal access token
REPO_URL = env.str("REPO_URL", "https://github.com/Onlymeriz/Ubot")
HEROKU_API_KEY = env.str("HEROKU_API_KEY", None)
HEROKU_APP_NAME = env.str("HEROKU_APP_NAME", None)
SUDO_USERS = env.int("SUDO_USERS", None)
test_server = env.bool("TEST_SERVER", False)
modules_repo_branch = env.str("MODULES_REPO_BRANCH", "main")
STRING_SESSION1 = env.str("STRING_SESSION1", "")
STRING_SESSION2 = env.str("STRING_SESSION2", "")
STRING_SESSION3 = env.str("STRING_SESSION3", "")
STRING_SESSION4 = env.str("STRING_SESSION4", "")
STRING_SESSION5 = env.str("STRING_SESSION5", "")
STRING_SESSION6 = env.str("STRING_SESSION6", "")
STRING_SESSION7 = env.str("STRING_SESSION7", "")
STRING_SESSION8 = env.str("STRING_SESSION8", "")
STRING_SESSION9 = env.str("STRING_SESSION9", "")
STRING_SESSION10 = env.str("STRING_SESSION10", "")
STRING_SESSION11 = env.str("STRING_SESSION11", "")
STRING_SESSION12 = env.str("STRING_SESSION12", "")
STRING_SESSION13 = env.str("STRING_SESSION13", "")
STRING_SESSION14 = env.str("STRING_SESSION14", "")
STRING_SESSION15 = env.str("STRING_SESSION15", "")
STRING_SESSION16 = env.str("STRING_SESSION16", "")
STRING_SESSION17 = env.str("STRING_SESSION17", "")
STRING_SESSION18 = env.str("STRING_SESSION18", "")
STRING_SESSION19 = env.str("STRING_SESSION19", "")
STRING_SESSION20 = env.str("STRING_SESSION20", "")
STRING_SESSION21 = env.str("STRING_SESSION21", "")
STRING_SESSION22 = env.str("STRING_SESSION22", "")
STRING_SESSION23 = env.str("STRING_SESSION23", "")
STRING_SESSION24 = env.str("STRING_SESSION24", "")
STRING_SESSION25 = env.str("STRING_SESSION25", "")
STRING_SESSION26 = env.str("STRING_SESSION26", "")
STRING_SESSION27 = env.str("STRING_SESSION27", "")
STRING_SESSION28 = env.str("STRING_SESSION28", "")
STRING_SESSION29 = env.str("STRING_SESSION29", "")
STRING_SESSION30 = env.str("STRING_SESSION30", "")
STRING_SESSION31 = env.str("STRING_SESSION31", "")
STRING_SESSION32 = env.str("STRING_SESSION32", "")
STRING_SESSION33 = env.str("STRING_SESSION33", "")
STRING_SESSION34 = env.str("STRING_SESSION34", "")
STRING_SESSION35 = env.str("STRING_SESSION35", "")
STRING_SESSION36 = env.str("STRING_SESSION36", "")
STRING_SESSION37 = env.str("STRING_SESSION37", "")
STRING_SESSION38 = env.str("STRING_SESSION38", "")
STRING_SESSION39 = env.str("STRING_SESSION39", "")
STRING_SESSION40 = env.str("STRING_SESSION40", "")
STRING_SESSION41 = env.str("STRING_SESSION41", "")
STRING_SESSION42 = env.str("STRING_SESSION42", "")
STRING_SESSION43 = env.str("STRING_SESSION43", "")
STRING_SESSION44 = env.str("STRING_SESSION44", "")
STRING_SESSION45 = env.str("STRING_SESSION45", "")
STRING_SESSION46 = env.str("STRING_SESSION46", "")
STRING_SESSION47 = env.str("STRING_SESSION47", "")
STRING_SESSION48 = env.str("STRING_SESSION48", "")
STRING_SESSION49 = env.str("STRING_SESSION49", "")
STRING_SESSION50 = env.str("STRING_SESSION50", "")
STRING_SESSION51 = env.str("STRING_SESSION51", "")
STRING_SESSION52 = env.str("STRING_SESSION52", "")
STRING_SESSION53 = env.str("STRING_SESSION53", "")
STRING_SESSION54 = env.str("STRING_SESSION54", "")
STRING_SESSION55 = env.str("STRING_SESSION55", "")
STRING_SESSION56 = env.str("STRING_SESSION56", "")
STRING_SESSION57 = env.str("STRING_SESSION57", "")
STRING_SESSION58 = env.str("STRING_SESSION58", "")
STRING_SESSION59 = env.str("STRING_SESSION59", "")
STRING_SESSION60 = env.str("STRING_SESSION60", "")
STRING_SESSION61 = env.str("STRING_SESSION61", "")
STRING_SESSION62 = env.str("STRING_SESSION62", "")
STRING_SESSION63 = env.str("STRING_SESSION63", "")
STRING_SESSION64 = env.str("STRING_SESSION64", "")
STRING_SESSION65 = env.str("STRING_SESSION65", "")
STRING_SESSION66 = env.str("STRING_SESSION66", "")
STRING_SESSION67 = env.str("STRING_SESSION67", "")
STRING_SESSION68 = env.str("STRING_SESSION68", "")
STRING_SESSION69 = env.str("STRING_SESSION69", "")
STRING_SESSION70 = env.str("STRING_SESSION70", "")
STRING_SESSION71 = env.str("STRING_SESSION71", "")
STRING_SESSION72 = env.str("STRING_SESSION72", "")
STRING_SESSION73 = env.str("STRING_SESSION73", "")
STRING_SESSION74 = env.str("STRING_SESSION74", "")
STRING_SESSION75 = env.str("STRING_SESSION75", "")
STRING_SESSION76 = env.str("STRING_SESSION76", "")
STRING_SESSION77 = env.str("STRING_SESSION77", "")
STRING_SESSION78 = env.str("STRING_SESSION78", "")
STRING_SESSION79 = env.str("STRING_SESSION79", "")
STRING_SESSION80 = env.str("STRING_SESSION80", "")
STRING_SESSION81 = env.str("STRING_SESSION81", "")
STRING_SESSION82 = env.str("STRING_SESSION82", "")
STRING_SESSION83 = env.str("STRING_SESSION83", "")
STRING_SESSION84 = env.str("STRING_SESSION84", "")
STRING_SESSION85 = env.str("STRING_SESSION85", "")
STRING_SESSION86 = env.str("STRING_SESSION86", "")
STRING_SESSION87 = env.str("STRING_SESSION87", "")
STRING_SESSION88 = env.str("STRING_SESSION88", "")
STRING_SESSION89 = env.str("STRING_SESSION89", "")
STRING_SESSION90 = env.str("STRING_SESSION90", "")
STRING_SESSION91 = env.str("STRING_SESSION91", "")
STRING_SESSION92 = env.str("STRING_SESSION92", "")
STRING_SESSION93 = env.str("STRING_SESSION93", "")
STRING_SESSION94 = env.str("STRING_SESSION94", "")
STRING_SESSION95 = env.str("STRING_SESSION95", "")
STRING_SESSION96 = env.str("STRING_SESSION96", "")
STRING_SESSION97 = env.str("STRING_SESSION97", "")
STRING_SESSION98 = env.str("STRING_SESSION98", "")
STRING_SESSION99 = env.str("STRING_SESSION99", "")
STRING_SESSION100 = env.str("STRING_SESSION100", "")