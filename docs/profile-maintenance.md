# Profile maintenance

The profile uses standard GitHub Markdown, HTML image/picture/details elements, and standalone SVG images. It has no JavaScript, external fonts, runtime icon service, analytics widget, or generated statistics counter.

## Artwork and motion

- `assets/terminal.svg` and `assets/terminal-mobile.svg`: custom desktop and narrow-screen terminal headers. A command reveals once, the cursor blinks four times, and an accent line draws once. The mobile source is selected below 600 px.
- `assets/devops-workflow.svg` and `assets/devops-workflow-mobile.svg`: custom desktop and narrow-screen lifecycle diagrams with numbered steps and arrows. The connector animation runs twice, then stops.
- All four SVGs have titles, descriptions, explicit viewBoxes, and dark panels with readable text on either GitHub theme. Essential content and arrows are present without animation. Reduced-motion CSS inside the SVG disables decorative motion and command clipping. This CSS belongs to the SVG image, not the README HTML.
- The contribution snake is behind an expandable section, with light and dark sources. Its animation is supplied by the existing snake generator; it does not have our custom reduced-motion handling. The native contribution-history link remains available independently.
- Keep profile text in the README as well as image alternative text so the identity remains readable without images.

## Technology icons

The icons are vendored from [Devicon](https://github.com/devicons/devicon) at commit `6a37858047b0e8d9c9c0e68f4a071fc410652e89`. The original MIT license is retained in `assets/icons/LICENSE`. All use the `original` variant except Linux, which uses the smaller `plain` SVG. Each icon is padded inside a light rounded tile for contrast in both GitHub themes. Brand names and marks belong to their respective owners.

Vendoring avoids a third-party icon request on every profile view. To update, download the corresponding `icons/<name>/<name>-<variant>.svg` files from a reviewed Devicon revision and preserve its license.

## Evidence behind the profile

Reviewed on 2026-10-24. These links explain the choices; this is not an independent certification of skill or deployment uptime.

| Claim | Repository evidence |
| --- | --- |
| Name, SLIIT undergraduate, Microsoft Learn Student Ambassador, Postman Student Expert, social links and email | Existing profile README before this redesign |
| Linux, Ubuntu, CentOS Stream, Vagrant, Nginx, Tomcat, Java, Maven, MySQL, Memcached | [Deployment lab README](https://github.com/kavinduumayanga/devops-multi-tier-deployment) and [VM definitions](https://github.com/kavinduumayanga/devops-multi-tier-deployment/blob/main/manual_provisioning/Vagrantfile) |
| Bash automation is experimental | Deployment lab README and `Automated_provisioning/scripts/`; the lab explicitly identifies manual provisioning as the completed version |
| Java/Spring Boot, REST, Maven, GitHub Actions; Kavindu owns Ride Management | [RideLink README](https://github.com/kavinduumayanga/ridelink-backend) and [CI workflow](https://github.com/kavinduumayanga/ridelink-backend/blob/main/.github/workflows/ci.yml) |
| Python/FastAPI certificate automation | [CertLoop](https://github.com/kavinduumayanga/certloop), its backend source tree, and `pyproject.toml` |
| Azure Static Web Apps demo | [Demo repository](https://github.com/kavinduumayanga/azure-staticweb-demo) and its `.github/workflows/azure-static-web-apps-thankful-river-0239ab810.yml` |

Docker, Kubernetes, Terraform, Ansible, Prometheus, and Grafana are explicitly learning-roadmap items. The README does not claim completed projects with those tools. RHEL was omitted because the inspected evidence did not establish its use. RideLink is credited as a team project, not sole authorship.

## Contribution workflow

The existing `.github/workflows/snake.yml` remains scheduled every 12 hours and supports a push to `main` or a manual run. It uses the SVG-only [Platane/snk](https://github.com/Platane/snk) generator and [crazy-max/ghaction-github-pages](https://github.com/crazy-max/ghaction-github-pages) to write the generated SVGs to the `output` branch. Both actions are pinned to the verified commit of the existing version. Concurrency prevents simultaneous publishing jobs.

The workflow defaults to `contents: read`. Only the publishing job requests `contents: write`; all unspecified permissions are disabled. It uses the repository's automatic `GITHUB_TOKEN`, with no PAT, added secret, or pull-request trigger.

At inspection, Actions was enabled, the account had repository administration access, the default token policy was read-only, and the latest three snake runs had succeeded. Both generated SVG URLs were checked during validation.

After committing and pushing the redesign to `main`, the workflow runs automatically. No GitHub Pages site, new secret, or broader default write permission is required. To refresh manually, open **Actions → Generate Snake Animation → Run workflow** on `main`. If repository policy later blocks publishing, review the failed run and allow this job to write to `output`; do not broaden token permissions unnecessarily.

## Validation and future edits

Check relative asset paths, meaningful image alt text, external project links, SVG XML, and the workflow with `actionlint`. Review at desktop and phone widths, in light and dark themes, and with reduced motion enabled. Check actual GitHub rendering again after publishing: a local preview cannot fully reproduce GitHub image caching or the surrounding profile UI.

The README's only remotely generated image is the contribution snake hosted on GitHub. Devicon is a source dependency, not a runtime service. LinkedIn, HackerRank, and email are retained from the existing profile; automated access restrictions or a `mailto:` link cannot establish account or mailbox ownership.

### Redesign validation results

- GitHub's Markdown API rendered the README successfully and retained the picture sources, local images, details sections, and technology table.
- Chromium previews using that rendered HTML and GitHub-style Markdown CSS passed at 320, 390, and 1280 px in both light and dark mode: no page overflow or broken images. Desktop and mobile screenshots were visually reviewed. Preview files and tooling were kept outside the repository.
- All local SVGs parsed as XML; local image references and fenced blocks passed validation. The custom assets' text stayed inside each viewBox. The four custom SVGs respected reduced-motion media settings when checked directly; the terminal reveal and cursor were also sampled during normal animation.
- All GitHub project/activity links, both generated snake assets, and HackerRank returned HTTP 200. LinkedIn returned HTTP 999 (automated-access restriction); the original profile URL was preserved. Email was not sent or tested.
- `actionlint` 1.7.12 and `git diff --check` passed. The updated workflow has not been executed remotely; the pre-existing workflow's successful runs were inspected.
- Changes are limited to the profile README, its existing snake workflow, local artwork/icons/license, and these maintenance notes. No commit, push, account-setting change, or workflow dispatch was performed.
