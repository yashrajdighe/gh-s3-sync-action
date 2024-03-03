import os
import argparse


def parse_inputs():
    parser = argparse.ArgumentParser(
        description="Runs aws s3 sync with specified options."
    )

    parser.add_argument(
        "--source",
        type=str,
        required=True,
        help="path to directory to sync to bucket"
    )
    parser.add_argument(
        "--delete",
        type=bool,
        default=False,
        help="delete files which does not exists at source"
    )
    parser.add_argument(
        "--include",
        type=str,
        default="*",
        nargs='+',
        help="files to include"
    )
    parser.add_argument(
        "--exclude",
        type=str,
        default="",
        nargs='+',
        help="files to exclude"
    )
    parser.add_argument(
        "--destination",
        type=str,
        required=True,
        help="S3 bucket name with directory to sync data"
    )
    parser.add_argument(
        "--dryrun",
        type=bool,
        default=True,
        help="Dry run the output"
    )

    args = parser.parse_args()
    return args


def s3_sync(inputs):
    command = ["aws", "s3", "sync"]
    command.append(inputs.source)
    command.append(inputs.destination)

    if inputs.delete:
        command.append("--delete")
    if inputs.exclude:
        command.append("--exclude")
        for pattern in inputs.exclude:
            command.append(f"\"{pattern}\"")
    if inputs.include:
        command.append("--include")
        for pattern in inputs.include:
            command.append(f"\"{pattern}\"")
    if inputs.dryrun:
        command.append("--dryrun")

    os.system(" ".join(command))


if __name__ == "__main__":
    s3_sync(inputs=parse_inputs())
