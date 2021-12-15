import os

from dotenv import load_dotenv
load_dotenv()

from opensea import OpenseaAPI

# create an object to interact with the Opensea API (need an api key)
api = OpenseaAPI(apikey=os.environ["OPENSEA_API_KEY"])

# fetch collection stats
result = api.collection_stats(collection_slug="cryptopunks")

# fetch multiple events
from opensea import utils as opensea_utils

period_start = opensea_utils.datetime_utc(2021, 11, 6, 14, 25)
period_end = opensea_utils.datetime_utc(2021, 11, 6, 14, 30)
result = api.events(
    occurred_after=period_start,
    occurred_before=period_end,
    limit=10,
    export_file_name="events.json",
)

# fetch multiple bundles
result = api.bundles(limit=2)
