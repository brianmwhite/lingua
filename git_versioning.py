import subprocess
import sys


def get_latest_tag():
    """Get the latest git tag that matches the version pattern vX.Y.Z."""
    try:
        result = subprocess.run(
            ["git", "describe", "--tags", "--match", "v*.*.*", "--abbrev=0"],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        return result.stdout.strip()
    except Exception:
        return None


def increment_version(latest_tag, part):
    """Increment major, minor, or patch version."""
    if not latest_tag:
        return "v1.0.0"

    # Extract version numbers
    tag_version = latest_tag.lstrip("v")
    major, minor, patch = map(int, tag_version.split("."))

    if part == "major":
        major += 1
        minor, patch = 0, 0
    elif part == "minor":
        minor += 1
        patch = 0
    elif part == "patch":
        patch += 1
    else:
        raise ValueError("Invalid increment type. Choose 'major', 'minor', or 'patch'.")

    return f"v{major}.{minor}.{patch}"


def main():
    if len(sys.argv) < 2:
        print("Usage: python git_versioning.py {major|minor|patch} [--dry-run]")
        sys.exit(1)

    increment_part = sys.argv[1]
    dry_run = "--dry-run" in sys.argv

    latest_tag = get_latest_tag()
    new_tag = increment_version(latest_tag, increment_part)

    print(f"Old tag: {latest_tag}")
    print(f"New tag: {new_tag}")

    if dry_run:
        print("------------------------------")
        print(f"git tag {new_tag}")
        print(f"git push origin {new_tag}")
    else:
        subprocess.run(["git", "tag", new_tag])
        subprocess.run(["git", "push", "origin", new_tag])


if __name__ == "__main__":
    main()
