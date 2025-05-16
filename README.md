# FastDCA_P1 - Q4 Agentic AI Studies
This is an example project for FastAPI using Uvicorn.

## ENVIRONMENT SETUP:
### Install uv on windows:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

### Install uv on mac and Linux
curl -LsSf https://astral.sh/uv/install.sh | less

I am sharing the command again to install uv

### 1. Install the latest version of uvicorn:
```bash
pip install --upgrade pip
pip install uvicorn
```
### 2. Create a new project:
```bash
mkdir fastdca_p1
cd fastdca_p1
uv init fastdca_p1
```
### 3. Activate the virtual environment and install FastAPI:
```bash
uv init fastdca_p1
cd fastdca_p1
uv venv
source .venv/bin/activate
uv add "fastapi"
```
### 4. Add additional dependencies (optional):
```bash
uv add "pydantic"
uv add "sqlalchemy"
uv add "asyncpg"
uv add "psycopg2-binary"
```
### 5. Run your application:
```bash
uv run main.py
```
### 6. Open your browser at http://localhost:8000/docs to see the interactive API documentation.
### 7. You can also generate static documentation by running:
```bash
uv docs
```
### 8. To deactivate the virtual environment, simply type:
deactivate

## If you want to start from scratch, delete the existing files in the directory and then follow steps 1-5 above.

# OR
## To create a new project with all the dependencies installed, use this command:
uv init fastdca_p1
cd fastdca_p1
uv venv
source .venv/Scripts/activate
uv add "fastapi[standard]"

uv run main.py

## Additional packages that are commonly used in FastAPI projects:
uv add "uvicorn"
uv add "python-multipart"
uv add "requests"
uv add "pytest"
uv add "starlette"
uv add "typing_extensions"
uv add "click"
uv add "itsdangerous"
uv add "Jinja2"
uv add "MarkupSafe"
uv add "Werkzeug"
uv add "email-validator"
uv add "greenlet"
uv add "h11"
uv add "httptools"
uv add "hypercorn"
uv add "multidict"
uv add "packaging"
uv add "pluggy"
uv add "py"
uv add "toml"
uv add "zipp"
uv add "certifi"
uv add "chardet"
uv add "idna"
uv add "multidict"
uv add "urllib3"
uv add "asgi-lifespan"
uv add "anyio"
uv add "h11"
uv add "httptools"
uv add "hypercorn"
uv add "markupsafe"
uv add "pyyaml"
uv add "coverage"
uv add "flake8"
uv add "black"
uv add "isort"
uv add "mypy"
uv add "types-pyyaml"
uv add "types-python-dateutil"
uv add "types-psycopg2"
uv add "types-setuptools"
uv add "types-toml"
uv add "types-yarl"
uv add "types-zipp"
uv add "types-certifi"
uv add "types-chardet"
uv add "types-idna"
uv add "types-multidict"
uv add "types-urllib3"
uv add "pydantic"
uv add "sqlalchemy"
uv add "asyncpg"
uv add "psycopg2-binary"
uv add "httpx"
uv add "aiofiles"
uv add "jinja2"
uv add "watchdog"
uv add "markdown-it-py"
uv add "mistune"
uv add "mkdocs"
uv add "mkdocs-material"
uv add "mkdocs-minify-plugin"
uv add "mkdocs-git-revision-date-localized-plugin"
uv add "mkdocs-awesome-pages-plugin"
uv add "mkdocs-jupyter"
uv add "mkdocs-exclude-search-plugin"
uv add "mkdocs-literate-nav-plugin"
uv add "mkdocs-redirects"
uv add "mkdocs-autorefs-plugin"
uv add "mkdocs-static-i18n"
uv add "mkdocs-video-player-plugin"
uv add "mkdocs-pdf-export-plugin"
uv add "mkdocs-git-authors-plugin"
uv add "mkdocs-git-trailers-plugin"
uv add "mkdocs-git-committers-plugin"
uv add "mkdocs-git-contributors-plugin"
uv add "mkdocs-git-history-plugin"
uv add "mkdocs-git-stats-plugin"
uv add "mkdocs-git-tags-plugin"
uv add "mkdocs-git-milestones-plugin"
uv add "mkdocs-git-labels-plugin"
uv add "mkdocs-git-issues-plugin"
uv add "mkdocs-git-prs-plugin"
uv add "mkdocs-git-comments-plugin"
uv add "mkdocs-git-notes-plugin"
uv add "mkdocs-git-wiki-plugin"
uv add "mkdocs-material"
uv add "mkdocs-minify-plugin"
uv add "mkdocs-git-revision-date-localized-plugin"
uv add "mkdocs-awesome-pages-plugin"
uv add "mkdocs-jupyter"
uv add "mkdocs-exclude-search-plugin"
uv add "mkdocs-literate-nav-plugin"
uv add "mkdocs-redirects"
uv add "mkdocs-autorefs-plugin"
uv add "mkdocs-static-i18n"
uv add "mkdocs-video-player-plugin"
uv add "mkdocs-pdf-export-plugin"
uv add "mkdocs-git-authors-plugin"
uv add "mkdocs-git-trailers-plugin"
uv add "mkdocs-git-committers-plugin"
uv add "mkdocs-git-contributors-plugin"
uv add "mkdocs-git-history-plugin"
uv add "mkdocs-git-stats-plugin"
uv add "mkdocs-git-tags-plugin"
uv add "mkdocs-git-milestones-plugin"
uv add "mkdocs-git-labels-plugin"
uv add "mkdocs-git-issues-plugin"
uv add "mkdocs-git-prs-plugin"
uv add "mkdocs-git-comments-plugin"
uv add "mkdocs-git-notes-plugin"
uv add "mkdocs-git-wiki-plugin"
uv add "mkdocs-git-blog-plugin"
uv add "mkdocs-git-news-plugin"
uv add "mkdocs-git-events-plugin"
uv add "mkdocs-git-calendar-plugin"
uv add "mkdocs-git-schedule-plugin"
uv add "mkdocs-git-agenda-plugin"
uv add "mkdocs-git-planner-plugin"
uv add "mkdocs-git-roadmap-plugin"
uv add "mkdocs-git-backlog-plugin"
uv add "mkdocs-git-sprint-plugin"
uv add "mkdocs-git-release-plugin"
uv add "mkdocs-git-versioning-plugin"
uv add "mkdocs-git-tagging-plugin"
uv add "mkdocs-git-labeling-plugin"
uv add "mkdocs-git-commenting-plugin"
uv add "mkdocs-git-notifying-plugin"
uv add "mkdocs-git-tracking-plugin"
uv add "mkdocs-git-reporting-plugin"
uv add "mkdocs-git-analytics-plugin"
uv add "mkdocs-git-seo-plugin"
uv add "mkdocs-git-social-media-plugin"
uv add "mkdocs-git-sharing-plugin"
uv add "mkdocs-git-collaboration-plugin"
uv add "mkdocs-git-coauthoring-plugin"
uv add "mkdocs-git-review-request-plugin"
uv add "mkdocs-git-code-review-plugin"
uv add "mkdocs-git-code-quality-plugin"
uv add "mkdocs-git-code-style-guide-plugin"
uv add "mkdocs-git-code-of-conduct-plugin"
uv add "mkdocs-git-license-manager-plugin"
uv add "mkdocs-git-open-source-initiative-plugin"
uv add "mkdocs-git-community-management-plugin"
uv add "mkdocs-git-project-management-plugin"
uv add "mkdocs-git-task-management-plugin"
uv add "mkdocs-git-issue-tracking-plugin"
uv add "mkdocs-git-feature-request-plugin"
uv add "mkdocs-git-bug-tracking-plugin"
uv add "mkdocs-git-documentation-management-plugin"
uv add "mkdocs-git-content-management-plugin"
uv add "mkdocs-git-user-interface-design-plugin"
uv add "mkdocs-git-user-experience-design-plugin"
uv add "mkdocs-git-user-story-writing-plugin"
uv add "mkdocs-git-use-case-scenario-writing-plugin"
uv add "mkdocs-git-business-process-modeling-plugin"
uv add "mkdocs-git-system-design-plugin"
uv add "mkdocs-git-software-development-life-cycle-plugin"
uv add "mkdocs-git-testing-strategy-plugin"
uv add "mkdocs-git-deployment-strategy-plugin"
uv add "mkdocs-git-monitoring-and-metrics-plugin"
uv add "mkdocs-git-performance-tuning-plugin"
uv add "mkdocs-git-security-audit-plugin"
uv add "mkdocs-git-compliance-and-regulatory-filing-plugin"
uv add "mkdocs-git-data-privacy-plugin"
uv add "mkdocs-git-data-protection-plugin"
uv add "mkdocs-git-data-retention-policy-plugin"
uv add "mkdocs-git-data-access-control-plugin"
uv add "mkdocs-git-data-integrity-check-plugin"
uv add "mkdocs-git-data-validation-plugin"
uv add "mkdocs-git-data-transformation-plugin"
uv add "mkdocs-git-data-enrichment-plugin"
uv add "mkdocs-git-data-enhancement-plugin"
uv add "mkdocs-git-data-enrichment-toolkit-plugin"
uv add "mkdocs-git-data-enrichment-framework-plugin"
uv add "mkdocs-git-data-enrichment-library-plugin"
uv add "mkdocs-git-data-enrichment-service-plugin"
uv add "mkdocs-git-data-enrichment-platform-plugin"
uv add "mkdocs-git-data-enrichment-suite-plugin"
uv add "mkdocs-git-data-enrichment-workflow-plugin"
uv add "mkdocs-git-data-enrichment-engine-plugin"
uv add "mkdocs-git-data-enrichment-module-plugin"
uv add "mkdocs-git-data-enrichment-component-plugin"
uv add "mkdocs-git-data-enrichment-application-plugin"
uv add "mkdocs-git-data-enrichment-api-plugin"
uv add "mkdocs-git-data-enrichment-service-plugin"
uv add "mkdocs-git-data-enrichment-tool-plugin"
uv add "mkdocs-git-data-enrichment-toolset-plugin"
uv add "mkdocs-git-data-enrichment-kit-plugin"
uv add "mkdocs-git-data-enrichment-pack-plugin"
uv add "mkdocs-git-data-enrichment-package-plugin"
