import os

from dotenv import load_dotenv
load_dotenv()

from opensea import OpenseaAPI

# create an object to interact with the Opensea API (need an api key)
api = OpenseaAPI(apikey=os.environ["OPENSEA_API_KEY"])

# fetch multiple events
from opensea import utils as opensea_utils

period_start = opensea_utils.datetime_utc(2021, 11, 6, 14, 25)
period_end = opensea_utils.datetime_utc(2021, 11, 6, 14, 30)
result = api.events(
    collection_slug="cryptopunks",
    occurred_after=period_start,
    occurred_before=period_end,
    limit=10,
    event_type="successful",
    export_file_name="sales.json",
)

# fetch multiple bundles
result = api.bundles(limit=2)
