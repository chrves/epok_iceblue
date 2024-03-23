from dydx3.constants import API_HOST_SEPOLIA, API_HOST_MAINNET
from decouple import config

# !!!! SELECT MODE !!!!
MODE = "PRODUCTION"

# Close all open positions and orders
ABORT_ALL_POSITIONS = False

# Find Cointegrated Pairs
FIND_COINTEGRATED = True

# Manage Exits
MANAGE_EXITS = True

# Place Trades
PLACE_TRADES = True

# Resolution
RESOLUTION = "30MINS"

# Stats Window
WINDOW = 12

# Thresholds - Opening
MAX_HALF_LIFE = 12
ZSCORE_THRESH = 1.4
USD_PER_TRADE = 40
USD_MIN_COLLATERAL = 200

# Thresholds - Closing
CLOSE_AT_ZSCORE_CROSS = True

# Ethereum Address - CHANGE THIS WHEN SWITCHING BETWEEN PROD AND DEV
ETHEREUM_ADDRESS = "0xa143E7153DeC7A0Ea7f35307FEAD2d4c067792cE"

# KEYS - PRODUCTION
# Must be on Mainnet in DYDX
STARK_PRIVATE_KEY_MAINNET = config("STARK_PRIVATE_KEY_MAINNET")
DYDX_API_KEY_MAINNET = config("DYDX_API_KEY_MAINNET")
DYDX_API_SECRET_MAINNET = config("DYDX_API_SECRET_MAINNET")
DYDX_API_PASSPHRASE_MAINNET = config("DYDX_API_PASSPHRASE_MAINNET")

# KEYS - DEVELOPMENT
# Must be on Testnet in DYDX
STARK_PRIVATE_KEY_TESTNET = config("STARK_PRIVATE_KEY_TESTNET")
DYDX_API_KEY_TESTNET = config("DYDX_API_KEY_TESTNET")
DYDX_API_SECRET_TESTNET =config("DYDX_API_SECRET_TESTNET")
DYDX_API_PASSPHRASE_TESTNET = config("DYDX_API_PASSPHRASE_TESTNET")

# KEYS - Export
STARK_PRIVATE_KEY = STARK_PRIVATE_KEY_MAINNET if MODE == "PRODUCTION" else STARK_PRIVATE_KEY_TESTNET
DYDX_API_KEY = DYDX_API_KEY_MAINNET if MODE == "PRODUCTION" else DYDX_API_KEY_TESTNET
DYDX_API_SECRET = DYDX_API_SECRET_MAINNET if MODE == "PRODUCTION" else DYDX_API_SECRET_TESTNET
DYDX_API_PASSPHRASE = DYDX_API_PASSPHRASE_MAINNET if MODE == "PRODUCTION" else DYDX_API_PASSPHRASE_TESTNET

# HOST - Export
HOST = API_HOST_MAINNET if MODE == "PRODUCTION" else API_HOST_SEPOLIA

# HTTP PROVIDER
HTTP_PROVIDER_MAINNET = "https://eth-mainnet.g.alchemy.com/v2/Eo8jFivpL6jfx8JlwaAIajMYvqb4o1et"
HTTP_PROVIDER_TESTNET = "https://eth-sepolia.g.alchemy.com/v2/N6Mioefqut6yPepeH4dN_etDwkf4AkRe"
HTTP_PROVIDER = HTTP_PROVIDER_MAINNET if MODE == "PRODUCTION" else HTTP_PROVIDER_TESTNET