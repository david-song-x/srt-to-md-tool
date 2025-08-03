# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.0.0] - 2025-08-02
### Added
- Initial release of the **SRT to Markdown Tool**.
- `srt_to_md.py`:
  - Converts `.srt` files into structured Markdown articles with:
    - Introduction, Main Discussion, Additional Insights
    - Key Takeaways section
    - Condensed one-page summary
    - Full vs condensed comparison
    - Highlighted full version
  - Recursive folder processing.
  - Dual-save outputs (in-place + mirrored `output` folder).
- `srt_to_text.py`:
  - Lightweight script that cleans `.srt` into plain readable transcripts without extra formatting.
  - Recursive folder processing and dual-save outputs.
- `README.md` with:
  - Badges, example usage, and embedded flowchart diagram.
  - Script descriptions for both workflows.
- `.gitignore` tailored for Python projects, ignoring output folder contents except `.gitkeep`.
- `LICENSE` (MIT) for open-source usage.
- `flowchart.png` visualizing the processing workflow.
- Sample `.srt` file for quick testing.
