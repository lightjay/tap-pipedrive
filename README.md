# tap-pipedrive

`tap-pipedrive` is a Singer tap for Pipedrive. This version is backwards compatible with [singer-io's variant](https://github.com/singer-io/tap-pipedrive/tree/master).

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

Install from GitHub:

```bash
pipx install git+https://github.com/ORG_NAME/tap-pipedrive.git@main
```

## Configuration

### Accepted Config Options

<!--
Developer TODO: Provide a list of config options accepted by the tap.

This section can be created by copy-pasting the CLI output from:

```
tap-pipedrive --about --format=markdown
```
-->

| Setting | Required | Default | Description |
|:--------|:--------:|:-------:|:------------|
| api_token | True     | None    | The token to authenticate against the API service |
| request_timeout | False    |     300 | The request timeout, default 300 seconds. |
| start_date | False    | 2024-08-13 00:00:00 | The earliest record date to sync |
| user_agent | False    | tap-pipedrive (info@doona.dev) | The user agent to send with requests. |


A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-pipedrive --about
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

This tap uses beta endpoints and as such needs an api token assigned to a global admin permissions.

## Usage

You can easily run `tap-pipedrive` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-pipedrive --version
tap-pipedrive --help
tap-pipedrive --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-pipedrive` CLI interface directly using `poetry run`:

```bash
poetry run tap-pipedrive --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

<!--
Developer TODO:
Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any "TODO" items listed in
the file.
-->

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-pipedrive
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-pipedrive --version
# OR run a test `elt` pipeline:
meltano elt tap-pipedrive target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
