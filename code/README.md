# MIT-licensed figure rendering code

Install code/requirements.txt in a Python environment, then run `python code/rebuild_figures.py` from the repository root. Paths resolve relative to the script. Output: PNG, SVG and PDF figures, and qa/figure_geometry_audit.json. Rendering is deterministic in legal content, but binary file hashes can differ by software/font versions and timestamps. Arial is used when available; font substitution requires visual review.

The code renders legal premises supplied in the labelled input; it does not infer legal validity, empirical performance, independent coding agreement or copyright liability. AI-assisted generation is disclosed. Input figures/specifications and manuscript text have a separate CC BY-NC-ND licence; this code licence does not relicense them.
