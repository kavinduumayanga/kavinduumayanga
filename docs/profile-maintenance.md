# Profile maintenance

Edit `README.md` directly. The profile uses native GitHub Markdown, small local technology icons, and one optional contribution-snake animation. There are no banners, custom layout assets, SVG generators, typing services, or statistics widgets.

## Content sources

The four featured repositories were reviewed again for this redesign:

- [Multi-tier Linux deployment lab](https://github.com/kavinduumayanga/devops-multi-tier-deployment): seven Vagrant-managed Linux VMs; manual service configuration; Nginx, Tomcat, MySQL, Memcached, NFS, and RabbitMQ; dashboard and failover testing. Bash provisioning is explicitly experimental.
- [RideLink backend](https://github.com/kavinduumayanga/ridelink-backend): a team university project; Kavindu owns Ride Management. Spring Boot, Maven, and GitHub Actions CI are documented. This is CI, not an automated deployment pipeline.
- [CertLoop](https://github.com/kavinduumayanga/certloop): Python/FastAPI certificate generation with operator-confirmed email delivery and tracking.
- [Azure Static Web Apps demo](https://github.com/kavinduumayanga/azure-staticweb-demo): a Microsoft Learn Student Ambassadors session demo with an Azure deployment workflow.

Name, SLIIT education, community roles, LinkedIn, email, and HackerRank were retained from the existing profile. The profile's original email is used; a different email in the Azure demo README was not substituted. Docker, Kubernetes, Terraform, Ansible, Prometheus, and Grafana are described only as upcoming learning goals.

## Icons and cleanup

All 13 icons in `assets/icons/` are used by the README. They are from [Devicon](https://github.com/devicons/devicon), revision `6a37858047b0e8d9c9c0e68f4a071fc410652e89`, with their MIT license in `assets/icons/LICENSE`. The existing light icon tiles maintain contrast in both GitHub themes. They require no runtime icon service.

Removed the 16 obsolete desktop/mobile SVGs for the terminal, About, toolkit, workflow, and project cards, plus `scripts/build_profile_assets.py`. The now-empty `assets/projects/` and `scripts/` directories were removed. No unrelated content was removed.

## Contribution animation

The existing `.github/workflows/snake.yml` is unchanged. It retains its pinned actions, 12-hour schedule, push-to-main trigger, manual dispatch, timeout, concurrency control, and job-scoped publishing permission. No new token, secret, workflow, or account setting is required.

The snake is collapsed by default and uses separate light/dark images from the existing `output` branch. The adjacent contribution-history link remains usable without the animation. Upstream snake SVGs do not provide our own reduced-motion handling. No typing animation was added, keeping the existing snake as the only animated element and avoiding another external service.

## Verification

Render through GitHub's Markdown API, verify the image paths and links, and inspect the result inside the actual GitHub profile layout at desktop and phone widths in both themes. Local browser previews can substitute working-tree icons without publishing changes; this does not verify GitHub's asset cache after a push.

Run `actionlint .github/workflows/snake.yml` and `git diff --check` before committing. After publishing, confirm icon delivery and the expandable snake on the live profile. LinkedIn may block automated requests even when its URL is valid; email ownership cannot be verified by following a `mailto:` link.

### Results for this redesign

- The final README is 80 lines. All 13 local icons are referenced and valid SVG XML; no obsolete artwork references remain.
- GitHub's Markdown API rendered the page successfully. Its output was previewed in the actual public profile layout with local icon substitution: 1280 and 390 px in both light and dark modes, plus 320 and 768 px in dark mode. No article overflow, broken images, or tables were found. All four project links were retained.
- The compact technology groups were refined after visual review. The expanded snake loaded without overflow; its light and dark source URLs both returned HTTP 200.
- Project, GitHub activity, and HackerRank links returned HTTP 200. LinkedIn returned HTTP 999, an automated-access restriction; its original URL was preserved.
- `actionlint` and `git diff --check` passed. The existing snake workflow and icon sources are byte-for-byte unchanged; the latest existing snake run was successful.
- Modified `README.md` and these notes; removed only the 16 obsolete profile SVGs and their generator. No commit, push, new workflow, secret, or account-setting change was made.
