"""Stream type classes for tap-pipedrive."""

from __future__ import annotations

import typing as t
from typing import Any

from singer_sdk import typing as th
from singer_sdk.helpers.types import Context

from tap_pipedrive.client import PipedriveStream, PipedriveStreamV1


class ActivitiesStream(PipedriveStream):
    """Define custom stream."""

    name = "activities"
    path = "/api/v1/activities/collection"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "update_time"
    schema = th.PropertiesList(
        th.Property("active_flag", th.BooleanType),
        th.Property("add_time", th.DateTimeType),
        th.Property("busy_flag", th.BooleanType),
        th.Property("company_id", th.IntegerType),
        th.Property("conference_meeting_client", th.StringType),
        th.Property("conference_meeting_id", th.StringType),
        th.Property("conference_meeting_url", th.StringType),
        th.Property("deal_id", th.IntegerType),
        th.Property("done", th.BooleanType),
        th.Property("due_date", th.DateTimeType),
        th.Property("due_time", th.DateTimeType),
        th.Property("duration", th.StringType),
        th.Property("id", th.IntegerType),
        th.Property("lead_id", th.StringType),
        th.Property("location", th.StringType),
        th.Property("location_admin_area_level_1", th.StringType),
        th.Property("location_admin_area_level_2", th.StringType),
        th.Property("location_country", th.StringType),
        th.Property("location_formatted_address", th.StringType),
        th.Property("location_locality", th.StringType),
        th.Property("location_postal_code", th.StringType),
        th.Property("location_route", th.StringType),
        th.Property("location_street_number", th.StringType),
        th.Property("location_sublocality", th.StringType),
        th.Property("location_subpremise", th.StringType),
        th.Property("marked_as_done_time", th.DateTimeType),
        th.Property("org_id", th.IntegerType),
        th.Property("person_id", th.IntegerType),
        th.Property("project_id", th.IntegerType),
        th.Property("public_description", th.StringType),
        th.Property("source_timezone", th.StringType),
        th.Property("subject", th.StringType),
        th.Property("type", th.StringType),
        th.Property("update_time", th.DateTimeType),
        th.Property("update_user_id", th.IntegerType),
        th.Property("user_id", th.IntegerType),
    ).to_dict()


class ActivityTypesStream(PipedriveStream):
    """Define custom stream."""

    name = "activity_types"
    path = "/v1/activityTypes"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "update_time"
    schema = th.PropertiesList(
        th.Property("active_flag", th.BooleanType),
        th.Property("add_time", th.DateTimeType),
        th.Property("color", th.StringType),
        th.Property("icon_key", th.StringType),
        th.Property("id", th.IntegerType),
        th.Property("is_custom_flag", th.BooleanType),
        th.Property("key_string", th.StringType),
        th.Property("name", th.StringType),
        th.Property("order_nr", th.IntegerType),
        th.Property("update_time", th.DateTimeType),
    ).to_dict()


class DealsStream(PipedriveStream):
    """Define custom stream."""

    name = "deals"
    path = "/v1/deals/collection"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "update_time"
    schema = th.PropertiesList(
        th.Property("acv", th.IntegerType),
        th.Property("add_time", th.DateTimeType),
        th.Property("arr", th.IntegerType),
        th.Property("channel", th.StringType),
        th.Property("channel_id", th.IntegerType),
        th.Property("close_time", th.DateTimeType),
        th.Property("creator_user_id", th.IntegerType),
        th.Property("currency", th.StringType),
        th.Property("custom_fields", th.StringType),
        th.Property("expected_close_date", th.DateTimeType),
        th.Property("id", th.IntegerType),
        th.Property("is_deleted", th.BooleanType),
        th.Property("label", th.StringType),
        th.Property("label_ids", th.ArrayType(th.StringType)),
        th.Property("local_close_date", th.DateTimeType),
        th.Property("local_lost_date", th.DateTimeType),
        th.Property("local_won_date", th.DateTimeType),
        th.Property("lost_reason", th.StringType),
        th.Property("lost_time", th.DateTimeType),
        th.Property("mrr", th.IntegerType),
        th.Property("org_id", th.IntegerType),
        th.Property("origin", th.StringType),
        th.Property("origin_id", th.IntegerType),
        th.Property("owner_id", th.IntegerType),
        th.Property("person_id", th.IntegerType),
        th.Property("pipeline_id", th.IntegerType),
        th.Property("probability", th.IntegerType),
        th.Property("stage_change_time", th.DateTimeType),
        th.Property("stage_id", th.IntegerType),
        th.Property("status", th.StringType),
        th.Property("title", th.StringType),
        th.Property("update_time", th.DateTimeType),
        th.Property("user_id", th.IntegerType),
        th.Property("value", th.NumberType),
        th.Property("visible_to", th.StringType),
        th.Property("won_time", th.DateTimeType),
    ).to_dict()


class FilesStream(PipedriveStreamV1):
    """Define stream."""
    name = "files"
    path = "/v1/files"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("active_flag", th.BooleanType),
        th.Property("activity_id", th.IntegerType),
        th.Property("add_time", th.DateTimeType),
        th.Property("cid", th.StringType),
        th.Property("deal_id", th.IntegerType),
        th.Property("deal_name", th.StringType),
        th.Property("description", th.StringType),
        th.Property("file_name", th.StringType),
        th.Property("file_size", th.IntegerType),
        th.Property("file_type", th.StringType),
        th.Property("id", th.IntegerType),
        th.Property("inline_flag", th.BooleanType),
        th.Property("lead_id", th.IntegerType),
        th.Property("lead_name", th.StringType),
        th.Property("log_id", th.IntegerType),
        th.Property("mail_message_id", th.IntegerType),
        th.Property("mail_template_id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("org_id", th.IntegerType),
        th.Property("org_name", th.StringType),
        th.Property("person_id", th.IntegerType),
        th.Property("person_name", th.StringType),
        th.Property("product_id", th.IntegerType),
        th.Property("product_name", th.StringType),
        th.Property("remote_id", th.StringType),
        th.Property("remote_location", th.StringType),
        th.Property("s3_bucket", th.StringType),
        th.Property("update_time", th.DateTimeType),
        th.Property("url", th.StringType),
        th.Property("user_id", th.IntegerType),
    ).to_dict()


class FiltersStream(PipedriveStream):
    """Define stream."""
    name = "filters"
    path = "/v1/filters"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "update_time"
    schema = th.PropertiesList(
        th.Property("active_flag", th.BooleanType),
        th.Property("add_time", th.DateTimeType),
        th.Property("custom_view_id", th.IntegerType),
        th.Property("id", th.IntegerType),
        th.Property("last_used_time", th.DateTimeType),
        th.Property("name", th.StringType),
        th.Property("temporary_flag", th.BooleanType),
        th.Property("type", th.StringType),
        th.Property("update_time", th.DateTimeType),
        th.Property("user_id", th.IntegerType),
        th.Property("visible_to", th.StringType),
    ).to_dict()


class LeadLabelsStream(PipedriveStream):
    """Define stream."""
    name = "lead_labels"
    path = "/v1/leadLabels"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("add_time", th.DateTimeType),
        th.Property("color", th.StringType),
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("update_time", th.DateTimeType),
    ).to_dict()


class LeadsStream(PipedriveStreamV1):
    """Define stream."""
    name = "leads"
    path = "/v1/leads"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("add_time", th.DateTimeType),
        th.Property("cc_email", th.StringType),
        th.Property("channel", th.IntegerType),
        th.Property("channel_id", th.IntegerType),
        th.Property("creator_id", th.IntegerType),
        th.Property("expected_close_date", th.DateTimeType),
        th.Property("id", th.StringType),
        th.Property("is_archived", th.BooleanType),
        th.Property("label_ids", th.ArrayType(th.StringType)),
        th.Property("next_activity_id", th.IntegerType),
        th.Property("organization_id", th.IntegerType),
        th.Property("origin", th.StringType),
        th.Property("origin_id", th.StringType),
        th.Property("owner_id", th.IntegerType),
        th.Property("person_id", th.IntegerType),
        th.Property("source_name", th.StringType),
        th.Property("title", th.StringType),
        th.Property("update_time", th.DateTimeType),
        th.Property("value", th.ObjectType(
            th.Property("amount", th.IntegerType),
            th.Property("currency", th.StringType),
        )),
        th.Property("visible_to", th.StringType),
        th.Property("was_seen", th.BooleanType),
    ).to_dict()


class NotesStream(PipedriveStream):
    """Define stream."""
    name = "notes"
    path = "/v1/notes"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    next_page_token_jsonpath = "$.additional_data.pagination.next_start"  # noqa: S105
    replication_key = "update_time"
    schema = th.PropertiesList(
        th.Property("active_flag", th.BooleanType),
        th.Property("add_time", th.DateTimeType),
        th.Property("content", th.StringType),
        th.Property("deal", th.ObjectType(
            th.Property("title", th.StringType),
        )),
        th.Property("deal_id", th.IntegerType),
        th.Property("id", th.IntegerType),
        th.Property("last_update_user_id", th.IntegerType),
        th.Property("lead", th.ObjectType(
            th.Property("title", th.StringType),
        )),
        th.Property("lead_id", th.StringType),
        th.Property("org_id", th.IntegerType),
        th.Property("organization", th.ObjectType(
            th.Property("name", th.StringType),
        )),
        th.Property("person", th.ObjectType(
            th.Property("name", th.StringType),
        )),
        th.Property("person_id", th.IntegerType),
        th.Property("pinned_to_deal_flag", th.BooleanType),
        th.Property("pinned_to_lead_flag", th.BooleanType),
        th.Property("pinned_to_organization_flag", th.BooleanType),
        th.Property("pinned_to_person_flag", th.BooleanType),
        th.Property("pinned_to_project_flag", th.BooleanType),
        th.Property("project_id", th.IntegerType),
        th.Property("update_time", th.DateTimeType),
        th.Property("user", th.ObjectType(
            th.Property("email", th.StringType),
            th.Property("icon_url", th.StringType),
            th.Property("is_you", th.BooleanType),
            th.Property("name", th.StringType),
        )),
        th.Property("user_id", th.IntegerType),
    ).to_dict()

    def get_url_params(
            self,
            context: Context | None,  # noqa: ARG002
            next_page_token: Any | None,  # noqa: ANN401
    ) -> dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """
        params: dict = {"limit": 500}
        if next_page_token:
            params["start"] = next_page_token
        if self.replication_key:
            params[self.replication_param] = self.config.get("start_date")
        return params


class OrganizationsStream(PipedriveStream):
    """Define stream."""
    name = "organizations"
    path = "/v1/organizations/collection"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "update_time"
    schema = th.PropertiesList(
        th.Property("active_flag", th.BooleanType),
        th.Property("add_time", th.DateTimeType),
        th.Property("address", th.StringType),
        th.Property("address_admin_area_level_1", th.StringType),
        th.Property("address_admin_area_level_2", th.StringType),
        th.Property("address_country", th.StringType),
        th.Property("address_formatted_address", th.StringType),
        th.Property("address_locality", th.StringType),
        th.Property("address_postal_code", th.StringType),
        th.Property("address_route", th.StringType),
        th.Property("address_street_number", th.StringType),
        th.Property("address_sublocality", th.StringType),
        th.Property("address_subpremise", th.StringType),
        th.Property("cc_email", th.StringType),
        th.Property("delete_time", th.DateTimeType),
        th.Property("id", th.IntegerType),
        th.Property("label", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("owner_id", th.IntegerType),
        th.Property("update_time", th.DateTimeType),
    ).to_dict()


# todo: organization relationships
# https://developers.pipedrive.com/docs/api/v1/OrganizationRelationships


class PermissionSetsStream(PipedriveStream):
    """Define stream."""
    name = "permission_sets"
    path = "/v1/permissionSets"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("app", th.StringType),
        th.Property("assignment_count", th.IntegerType),
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("type", th.StringType),
    ).to_dict()


class PersonsStream(PipedriveStream):
    """Define stream."""
    name = "persons"
    path = "/v1/persons/collection"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "update_time"
    schema = th.PropertiesList(
        th.Property("active_flag", th.BooleanType),
        th.Property("add_time", th.DateTimeType),
        th.Property("cc_email", th.StringType),
        th.Property("delete_time", th.DateTimeType),
        th.Property("email", th.ArrayType(th.ObjectType(
            th.Property("primary", th.BooleanType),
            th.Property("value", th.StringType),
            th.Property("label", th.StringType),
        ))),
        th.Property("id", th.IntegerType),
        th.Property("label", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("org_id", th.IntegerType),
        th.Property("owner_id", th.IntegerType),
        th.Property("phone", th.ArrayType(th.ObjectType(
            th.Property("primary", th.BooleanType),
            th.Property("value", th.StringType),
            th.Property("label", th.StringType),
        ))),
        th.Property("picture_id", th.IntegerType),
        th.Property("update_time", th.DateTimeType),
        th.Property("visible_to", th.StringType),
    ).to_dict()


class PipelinesStream(PipedriveStream):
    """Define stream."""
    name = "pipelines"
    path = "/api/v2/pipelines"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("add_time", th.DateTimeType),
        th.Property("id", th.IntegerType),
        th.Property("is_deal_probability_enabled", th.BooleanType),
        th.Property("is_deleted", th.BooleanType),
        th.Property("name", th.StringType),
        th.Property("order_nr", th.IntegerType),
        th.Property("update_time", th.DateTimeType),
    ).to_dict()


class ProductsStream(PipedriveStream):
    """Define stream."""
    name = "products"
    path = "/api/v2/products"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("add_time", th.DateTimeType),
        th.Property("billing_frequency", th.StringType),
        th.Property("billing_frequency_cycles", th.StringType),
        th.Property("category", th.StringType),
        th.Property("code", th.StringType),
        th.Property("custom_fields", th.ObjectType(
            th.Property("dummy", th.StringType),
        )),
        th.Property("description", th.StringType),
        th.Property("id", th.IntegerType),
        th.Property("is_deleted", th.BooleanType),
        th.Property("is_linkable", th.BooleanType),
        th.Property("name", th.StringType),
        th.Property("owner_id", th.IntegerType),
        th.Property("prices", th.ArrayType(th.ObjectType(
            th.Property("cost", th.IntegerType),
            th.Property("currency", th.StringType),
            th.Property("direct_cost", th.IntegerType),
            th.Property("notes", th.StringType),
            th.Property("price", th.IntegerType),
            th.Property("product_id", th.IntegerType),
        ))),
        th.Property("tax", th.IntegerType),
        th.Property("unit", th.StringType),
        th.Property("update_time", th.DateTimeType),
        th.Property("visible_to", th.IntegerType),
    ).to_dict()


class ProjectsStream(PipedriveStream):
    """Define stream."""
    name = "projects"
    path = "/v1/projects"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("add_time", th.DateTimeType),
        th.Property("add_archive_timetime", th.DateTimeType),
        th.Property("board_id", th.IntegerType),
        th.Property("deal_ids", th.ArrayType(th.IntegerType)),
        th.Property("description", th.StringType),
        th.Property("end_date", th.DateTimeType),
        th.Property("id", th.IntegerType),
        th.Property("labels", th.ArrayType(th.IntegerType)),
        th.Property("org_id", th.IntegerType),
        th.Property("owner_id", th.IntegerType),
        th.Property("person_id", th.IntegerType),
        th.Property("persophase_idn_id", th.IntegerType),
        th.Property("start_date", th.DateTimeType),
        th.Property("status", th.StringType),
        th.Property("status_change_time", th.DateTimeType),
        th.Property("title", th.StringType),
        th.Property("update_time", th.DateTimeType),
    ).to_dict()


class ProjectTemplatesStream(PipedriveStream):
    """Define stream."""
    name = "project_templates"
    path = "/v1/projectTemplates"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("add_time", th.DateTimeType),
        th.Property("description", th.StringType),
        th.Property("id", th.IntegerType),
        th.Property("owner_id", th.IntegerType),
        th.Property("projects_board_id", th.IntegerType),
        th.Property("title", th.StringType),
        th.Property("update_time", th.DateTimeType),
    ).to_dict()


class RolesStream(PipedriveStream):
    """Define stream."""
    name = "roles"
    path = "/v1/roles"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("active_flag", th.BooleanType),
        th.Property("assignment_count", th.StringType),
        th.Property("description", th.StringType),
        th.Property("id", th.IntegerType),
        th.Property("level", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("parent_role_id", th.IntegerType),
        th.Property("sub_role_count", th.StringType),
    ).to_dict()


class StagesStream(PipedriveStream):
    """Define stream."""
    name = "stages"
    path = "/api/v2/stages"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("add_time", th.DateTimeType),
        th.Property("days_to_rotten", th.IntegerType),
        th.Property("deal_probability", th.IntegerType),
        th.Property("id", th.IntegerType),
        th.Property("is_deal_rot_enabled", th.BooleanType),
        th.Property("is_deleted", th.BooleanType),
        th.Property("name", th.StringType),
        th.Property("order_nr", th.IntegerType),
        th.Property("pipeline_id", th.IntegerType),
        th.Property("update_time", th.DateTimeType),
    ).to_dict()


# todo: Subscriptions
# https://developers.pipedrive.com/docs/api/v1/Subscriptions#findSubscriptionByDeal


class TasksStream(PipedriveStream):
    """Define stream."""
    name = "tasks"
    path = "/v1/tasks"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("add_time", th.DateTimeType),
        th.Property("assignee_id", th.IntegerType),
        th.Property("creator_id", th.IntegerType),
        th.Property("description", th.StringType),
        th.Property("done", th.IntegerType),
        th.Property("due_date", th.DateTimeType),
        th.Property("id", th.IntegerType),
        th.Property("marked_as_done_time", th.DateTimeType),
        th.Property("parent_task_id", th.IntegerType),
        th.Property("project_id", th.IntegerType),
        th.Property("title", th.StringType),
        th.Property("update_time", th.DateTimeType),
    ).to_dict()


class UsersStream(PipedriveStream):
    """Define stream."""
    name = "users"
    path = "/v1/users"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "modified"
    schema = th.PropertiesList(
        th.Property("access", th.ArrayType(th.ObjectType(
            th.Property("admin", th.BooleanType),
            th.Property("app", th.StringType),
            th.Property("permission_set_id", th.StringType),
        ))),
        th.Property("active_flag", th.BooleanType),
        th.Property("created", th.DateTimeType),
        th.Property("default_currency", th.StringType),
        th.Property("email", th.StringType),
        th.Property("has_created_company", th.BooleanType),
        th.Property("icon_url", th.StringType),
        th.Property("id", th.IntegerType),
        th.Property("is_admin", th.IntegerType),
        th.Property("is_deleted", th.BooleanType),
        th.Property("is_you", th.BooleanType),
        th.Property("lang", th.IntegerType),
        th.Property("last_login", th.DateTimeType),
        th.Property("locale", th.StringType),
        th.Property("modified", th.DateTimeType),
        th.Property("name", th.StringType),
        th.Property("phone", th.StringType),
        th.Property("role_id", th.IntegerType),
        th.Property("timezone_name", th.StringType),
        th.Property("timezone_offset", th.StringType),
    ).to_dict()


# todo: Webhooks:
# https://developers.pipedrive.com/docs/api/v1/Webhooks#getWebhooks
