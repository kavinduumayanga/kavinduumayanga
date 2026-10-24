# Profile maintenance

The profile combines GitHub-native Markdown with four small, self-hosted SVGs. It uses no JavaScript, custom README CSS, external fonts, statistics widgets, or runtime icon CDN.

## Design assets

- `assets/hero.svg` and `assets/hero-mobile.svg` form the responsive Linux terminal header.
- `assets/devops-pipeline.svg` and `assets/devops-pipeline-mobile.svg` show the Code → Build → Test → CI/CD → Deploy → Monitor learning path.
- The mobile assets are selected at browser widths of 900 px or below. This accounts for GitHub's profile sidebar, which can leave a narrow README column before the site itself switches to its phone layout.
- All custom visuals use a charcoal panel with green, cyan, and blue accents so they remain readable in GitHub light and dark themes.
- The SVGs include titles, descriptions, view boxes, and meaningful README alternative text.

The header's command reveal runs once and its cursor blinks four times. The pipeline highlight runs twice. The underlying text, cards, connectors, and fallback image remain complete when SMIL animation is unsupported. Embedded reduced-motion media rules remove the typing clip and hide decorative motion when the browser propagates that preference into image documents.

## Technology icons

The 13 icons under `assets/icons/` come from [Devicon](https://github.com/devicons/devicon) revision `6a37858047b0e8d9c9c0e68f4a071fc410652e89`. Their MIT license is retained at `assets/icons/LICENSE`. The files are local and require no third-party image request at profile-render time.

## Evidence behind the content

Reviewed on 2026-10-24:

- [Multi-tier Linux deployment lab](https://github.com/kavinduumayanga/devops-multi-tier-deployment): seven Vagrant-managed Linux VMs; manual service configuration; Nginx, Tomcat, MySQL, Memcached, NFS, and RabbitMQ; Java dashboard and failover testing. The project's Bash provisioning is explicitly experimental.
- [RideLink backend](https://github.com/kavinduumayanga/ridelink-backend): a four-service university project. Kavindu owns Ride Management. The repository documents Java 21, Spring Boot, MongoDB, Maven, JWT security, REST integration, and GitHub Actions CI.
- [CertLoop](https://github.com/kavinduumayanga/certloop): Python/FastAPI certificate generation with operator-confirmed email delivery and delivery tracking.
- [Azure Static Web Apps demo](https://github.com/kavinduumayanga/azure-staticweb-demo): an MLSA session demo with a GitHub Actions deployment workflow for Azure Static Web Apps.

Name, SLIIT education, community roles, LinkedIn, HackerRank, and email were retained from the existing profile. Docker, Kubernetes, Terraform, Ansible, Prometheus, and Grafana are labeled as roadmap technologies. RHEL was omitted because the inspected repositories do not establish its use.

## Contribution animation

The existing `.github/workflows/snake.yml` remains unchanged. It retains its pinned actions, 12-hour schedule, push-to-main trigger, manual dispatch, timeout, concurrency control, and job-scoped `contents: write` permission for publishing to the `output` branch. The repository default stays `contents: read`.

The README selects separate light and dark snake assets and keeps the animation collapsed by default. The snake generator does not provide this profile's reduced-motion handling, so the native contribution-history link is also available.

No new secret, token, GitHub Pages site, workflow, or account setting is required. After publishing, a push to `main` triggers the existing workflow. It can also be refreshed through **Actions → Generate Snake Animation → Run workflow**.

## Verification

Render the README through GitHub's Markdown API, then inspect it inside the public profile layout at realistic browser widths. Local previews can replace working-tree image URLs before the changes are published. This reproduces GitHub's HTML sanitization and profile layout, but it does not verify post-push asset caching.

Before committing:

1. Parse every local SVG as XML and check local image references and alternative text.
2. Preview desktop and mobile layouts in light and dark themes.
3. Confirm the narrow profile terminal does not require horizontal scrolling.
4. Verify both pipeline layouts, reduced-motion behavior, and static animation fallbacks.
5. Check project, social, activity, and snake URLs.
6. Run `actionlint .github/workflows/snake.yml` and `git diff --check`.

LinkedIn may reject automated requests even when the profile URL works normally. A `mailto:` link cannot verify mailbox ownership.

## Results for this redesign

- GitHub's Markdown API rendered the README successfully and retained both responsive image sources, all four project links, the terminal block, and the contribution details section.
- The rendered README was placed inside the actual public GitHub profile layout for visual review. Desktop and mobile previews passed at browser widths of 1280, 1024, 768, 390, and 320 px across light and dark themes. The measured README column ranged from 846 to 238 px with no page overflow or broken images.
- The narrow terminal copy was shortened after the first mobile review so every line remains readable without horizontal scrolling. The mobile pipeline connector was also corrected to preserve the six-stage sequence.
- All four custom SVGs parse as XML, keep their text within their view boxes, use unique IDs, and contain no scripts, `foreignObject`, or external embedded images. Normal animation sampling, reduced-motion rules, and animation-free fallback checks passed.
- All GitHub project, activity, workflow, and snake URLs plus HackerRank returned HTTP 200. LinkedIn returned HTTP 999 to the automated request; the established profile URL was retained.
- `actionlint` and `git diff --check` passed. The workflow and licensed Devicon sources are unchanged. The latest three inspected snake workflow runs succeeded.
- Modified `README.md` and this maintenance guide; created four responsive SVG assets. No unrelated files, secrets, account settings, commits, pushes, or remote workflow runs were changed.
