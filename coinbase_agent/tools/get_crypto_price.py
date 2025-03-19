import requests
from crewai.tools import BaseTool

COINBASE_API_URL = "https://api.coinbase.com/v2"


class GetCryptoPriceTool(BaseTool):
    name: str = "get_crypto_price"
    description: str = (
        "Fetch the latest cryptocurrency price. Provide crypto symbol and currency."
    )

    def _run(self, crypto: str = "BTC", currency: str = "USD") -> str:
        """
        Fetches the current price of a cryptocurrency from Coinbase API.
        """
        url = f"{COINBASE_API_URL}/prices/{crypto.upper()}-{currency.upper()}/spot"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an error for non-200 responses

            data = response.json()
            if "data" in data and "amount" in data["data"]:
                return f"The current price of {crypto.upper()} in {currency.upper()} is {data['data']['amount']} {currency.upper()}."
            else:
                return f"Could not retrieve price data for {crypto.upper()} in {currency.upper()}."

        except requests.exceptions.HTTPError as http_err:
            return (
                f"HTTP error occurred while fetching {crypto.upper()} price: {http_err}"
            )
        except requests.exceptions.RequestException as req_err:
            return f"Network error occurred while fetching {crypto.upper()} price: {req_err}"
        except Exception as err:
            return f"Unexpected error: {err}"
