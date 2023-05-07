import yaml

# Read GitLab CI/CD YAML file
with open(".gitlab-ci.yaml", "r") as f:
    gitlab_yaml = f.read()

# Parse YAML
gitlab_data = yaml.safe_load(gitlab_yaml)

# Convert to GitHub Actions YAML
github_data = {
    "name": "CI/CD Pipeline",
    "on": {
        "push": {
            "branches": ["main"]
        }
    },
    "jobs": {
        "build": {
            "runs-on": "ubuntu-latest",
            "steps": [
                {
                    "name": "Checkout code",
                    "uses": "actions/checkout@v2"
                }
            ]
        }
    }
}

for job_name, job_data in gitlab_data.items():
    github_job = {
        "runs-on": job_data.get("image"),
        "steps": [
            {"name": "Checkout code", "uses": "actions/checkout@v2"}
        ]
    }
    script = job_data.get("script")
    if script:
        github_job["steps"].append({"name": "Run script", "run": script})
    github_data["jobs"][job_name] = github_job

# Write GitHub Actions YAML to file
with open(".github/workflows/main.yaml", "w") as f:
    f.write(yaml.dump(github_data))
