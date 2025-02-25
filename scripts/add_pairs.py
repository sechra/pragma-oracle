# %% Imports
import logging
from asyncio import run
from math import ceil, log

from scripts.utils.constants import (
    COMPILED_CONTRACTS,
    currencies,
    NETWORK,
    pairs,
)
from scripts.utils.starknet import (
    dump_declarations,
    dump_deployments,
    get_declarations,
    get_eth_contract,
    get_starknet_account,
    invoke,
    deploy_v2,
    declare_v2,
    call,
)
from pragma.core.types import Currency, Pair

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


currencies_to_add = []
pairs_to_add = [
    Pair("ETH/USDT", "ETH", "USDT"),
    Pair("BTC/USDT", "BTC", "USDT"),
]


async def main():
    # Add Currencies
    for currency in currencies_to_add:
        print(currency.to_dict())
        tx_hash = await invoke(
            "pragma_Oracle",
            "add_currency",
            currency.serialize(),
        )
        logger.info(f"Added currency {currency} with tx hash {hex(tx_hash)}")

    # Add Pairs
    for pair in pairs_to_add:
        tx_hash = await invoke("pragma_Oracle", "add_pair", pair.serialize())
        logger.info(f"Added pair {pair} with tx hash {hex(tx_hash)}")


if __name__ == "__main__":
    run(main())
