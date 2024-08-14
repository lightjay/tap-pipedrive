"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_tap_test_class

from tap_pipedrive.tap import TapPipedrive

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "api_token": "fake"
}


# Run standard built-in tap tests from the SDK:
# TestTapPipedrive = get_tap_test_class(
#     tap_class=TapPipedrive,
#     config=SAMPLE_CONFIG,
# )
