"""Pipedrive tap class."""

from __future__ import annotations

import datetime

from singer_sdk import Tap
from singer_sdk import typing as th

from tap_pipedrive import streams


class TapPipedrive(Tap):
    """Pipedrive tap class."""

    name = "tap-pipedrive"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_token",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "request_timeout",
            th.IntegerType,
            required=False,
            default=300,
            description="The request timeout, default 300 seconds.",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            required=False,
            default=datetime.datetime.today().strftime("%Y-%m-%d 00:00:00"),
            description="The earliest record date to sync",
        ),
        th.Property(
            "user_agent",
            th.StringType,
            required=False,
            default="tap-pipedrive (info@doona.dev)",
            description="The user agent to send with requests.",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.PipedriveStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.ActivitiesStream(self),
            streams.ActivityTypesStream(self),
            streams.DealsStream(self),
            streams.FilesStream(self),
            streams.FiltersStream(self),
            streams.LeadsStream(self),
            streams.LeadLabelsStream(self),
            streams.NotesStream(self),
            streams.OrganizationsStream(self),
            streams.PermissionSetsStream(self),
            streams.PersonsStream(self),
            streams.PipelinesStream(self),
            streams.ProductsStream(self),
            streams.ProjectsStream(self),
            streams.ProjectTemplatesStream(self),
            streams.RolesStream(self),
            streams.StagesStream(self),
            streams.TasksStream(self),
            streams.UsersStream(self),
        ]


if __name__ == "__main__":
    TapPipedrive.cli()
