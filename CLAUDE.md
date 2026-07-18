# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Project Overview

This is a Skills IL category repository containing AI agent skills for travel: trip planning in Israel and abroad, flights from Israel, visas, passport logistics, and travel advisories for Israeli travelers. Each subdirectory is a self-contained skill following the open Agent Skills standard.

## Repository Structure

```
travel/
├── .github/                     # CI workflows, issue/PR templates
├── <skill-slug>/                # One folder per skill
│   ├── SKILL.md                 # Required skill definition (English)
│   ├── SKILL_HE.md              # Hebrew companion
│   ├── metadata.json            # Skills IL metadata
│   └── references/              # Optional documentation
├── CLAUDE.md                    # This file
├── CODEOWNERS                   # @skills-il/maintainers
├── LICENSE                      # MIT
├── README.md
├── SECURITY.md
└── scripts/validate-skill.sh    # Structural validation
```

## Conventions

- Skill slugs are kebab-case, matching the folder name.
- Metadata lives in `metadata.json` (NOT SKILL.md frontmatter): display names, tags, author, version, category, supported_agents.
- SKILL.md frontmatter carries only `name`, `description`, `license`.
- Default branch is `master`.
- No em dashes in any file or language.

## License

MIT
