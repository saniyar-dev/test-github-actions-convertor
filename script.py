import yaml

# Read GitLab CI/CD YAML file
with open(".gitlab-ci.yml", "r") as f:
    gitlab_yaml = f.read()

# Parse YAML
gitlab_data = yaml.safe_load(gitlab_yaml)

# Convert to GitHub Actions YAML
github_data = {
    "name": "CI/CD Pipeline",
    "on": {
        "push": {
            "branches": []
        }
    },
    "jobs": {
    }
}

for job_name, job_data in gitlab_data.items():
    github_data["on"]["push"]["branches"].append(
        job_data.get("only").get("refs")[0])
    github_job = {
        "runs-on": "ubuntu-latest",
        "container": job_data.get("image"),
        "steps": [
        ]
    }
    scripts = job_data.get("script")
    for script_data in scripts:
        if script_data:
            github_job["steps"].append(
                {"name": "Run script", "run": script_data})

    github_data["jobs"][job_name] = github_job


github_data["on"]["push"]["branches"] = list(
    set(github_data["on"]["push"]["branches"]))

# Write GitHub Actions YAML to file
with open(".github/workflows/main.yaml", "w") as f:
    f.write(yaml.dump(github_data))
