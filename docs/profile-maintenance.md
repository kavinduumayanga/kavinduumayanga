# Profile maintenance

The README is a Linux Workstation × DevOps Control Center portfolio built from self-contained SVGs. It uses GitHub-supported Markdown and HTML (`picture`, `img`, `a`, `details`, and `p`). There is no JavaScript, custom README CSS, external font, image-generation service, or runtime icon CDN.

## Editing the design

Run `python3 scripts/build_profile_assets.py` from the repository after editing the generator. It uses only the Python standard library and deterministically produces 16 SVGs. It never accesses the network or changes the workflow.

The generator centralizes the charcoal, sage-green, and cyan palette; typography; panel spacing; line iconography; and layouts. Edit copy and geometry there, then regenerate rather than editing generated SVGs by hand. Keep README alternative text in sync with copy changes.

- `assets/terminal{,-mobile}.svg`: workstation hero, command reveal, blinking cursor, and a conceptual cloud/Linux/build topology on desktop. Labels describe the learning journey; none are live telemetry.
- `assets/about{,-mobile}.svg`: Neofetch-inspired identity panel with the licensed Linux penguin, education, engineering focus, and community roles.
- `assets/toolkit{,-mobile}.svg`: grouped technology tiles, current learning focus, and explicitly labeled next-lab goals. Bash provisioning remains described as experimental.
- `assets/projects/`: four individually clickable project cards, each with a mobile layout. The Linux lab is visually emphasized and includes a simplified architecture, not a complete seven-VM network map. Repository links are ordinary HTML anchors around the images; SVG-internal links are not relied on.
- `assets/devops-workflow{,-mobile}.svg`: Code → Build → Test → Deploy → Monitor, using consistent vector icons and a finite connector animation. The caption frames this as a learning lifecycle, not a claim that every stage is implemented in every project.

The narrow layout is selected at a viewport width of 900 px or below. The breakpoint accounts for GitHub's profile sidebar: the README article can be much narrower than the browser window. All artwork scales to the available article width. Panels keep their own charcoal background and text contrast in GitHub light and dark themes.

## Motion and fallback behavior

The command reveals once; the cursor blinks four times. The hero topology runs twice, and the delivery-loop animation runs twice. Each custom SVG is complete without SMIL support: text, icons, connectors, and architecture remain visible. Reduced-motion CSS inside each SVG hides decorative motion and removes command clipping. This CSS is part of the SVG image, not the README HTML. Browser support for propagating reduced-motion preferences into image documents can vary; animations are finite as an additional safeguard.

The existing GitHub contribution snake stays in an expandable section, with light/dark image selection. Its upstream animation does not use this custom reduced-motion treatment. The native contribution-history link is available within the section.

## Icons and dependencies

Technology icons come from [Devicon](https://github.com/devicons/devicon) commit `6a37858047b0e8d9c9c0e68f4a071fc410652e89`. Their MIT license is retained in `assets/icons/LICENSE`. Existing source icon files were preserved. The generator embeds their paths directly, prefixes internal IDs, and places them in consistent light tiles, so SVG images need no external requests. The Linux penguin is reused in the identity panel. Brand names and marks belong to their respective owners.

The only remotely generated image is the contribution snake, hosted on GitHub. All new portfolio artwork is stored in this repository.

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

## Existing contribution workflow

`.github/workflows/snake.yml` is unchanged by this visual redesign. It retains the 12-hour schedule, push-to-main trigger, manual dispatch, concurrency control, timeout, and pinned SVG-only Platane/snk and crazy-max/ghaction-github-pages actions. The default token permission is `contents: read`; the publishing job requests `contents: write` for the output branch. No new secrets or account settings are needed.

After committing and pushing the redesign, normal GitHub asset delivery and the existing workflow apply. To refresh the snake manually, use **Actions → Generate Snake Animation → Run workflow** on `main`.

## Visual verification

The README was rendered through GitHub's Markdown API, then inserted locally into the actual public GitHub profile article in Chromium. New asset requests were intercepted in that browser and served from the working tree. This preserved GitHub's real profile sidebar, article widths, HTML sanitization result, and theme CSS without publishing changes.

Desktop, tablet, and phone layouts were inspected; improvements included larger mobile technology labels, shorter mobile copy, more space between panels, adjusted typography, and a breakpoint matched to the profile layout. The browser's sticky navigation behavior was suppressed for final artifact-only screenshots so it would not cover the top of the hero. Preview tooling and screenshots live outside the repository.

This is a local simulation in the real GitHub page, not verification of a deployed redesign. After pushing, manually confirm GitHub's image caching, source selection, animation behavior in your preferred browser, and the links on the published profile. In particular, browser support for reduced-motion propagation into SVG images should be checked on your target devices.


### Validation results

- GitHub Markdown API render: passed; all four image-card anchors and responsive picture sources retained.
- Actual profile-layout previews: 1280 and 390 px in light/dark themes, plus 320, 768, 1000, and 1024 px in dark mode. Measured article widths ranged from 238 to 846 px. No article overflow or broken images; screenshots were visually reviewed and refined.
- All 16 generated SVGs: no overlapping text boxes or out-of-bounds text. XML, unique IDs, image alt text, local references, and the absence of scripts or external embedded assets passed checks.
- Normal animation sampling confirmed the command reveal and cursor changes. Reduced-motion checks hid decorative animation and removed typing clipping. Static variants with the SMIL animation elements removed retained their text and complete diagrams.
- Regeneration produced byte-identical SVGs. All local SVGs together total approximately 206 KB, including source icons and both layout variants.
- Project links, GitHub activity links, both snake images, and HackerRank returned HTTP 200. LinkedIn returned HTTP 999 (automated-access restriction); its verified original URL is preserved. No email was sent.
- `actionlint` 1.7.12 and `git diff --check` passed. The workflow and existing icon sources are unchanged. No workflow dispatch, account-setting change, commit, or push was performed.
