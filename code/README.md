# MIT-licensed figure rendering code

Install code/requirements.txt in a Python environment, then run `python code/rebuild_figures.py` from the repository root. Paths resolve relative to the script. Output: PNG, SVG and PDF figures, and qa/figure_geometry_audit.json. Rendering is deterministic in legal content, but binary file hashes can differ by software/font versions and timestamps. Arial is used when available; font substitution requires visual review.

The standalone MIT software archive deliberately omits the separately licensed inputs. To run that archive, extract the original-materials companion from https://doi.org/10.5281/zenodo.23344007 into the same parent directory. The renderer needs `data/figure_label_matrix.csv` and `data/figure_spec.json`. These original inputs and the manuscript/figure content retain their separate CC BY-NC-ND 4.0 terms. The complete GitHub repository already contains both folders.

The code renders legal premises supplied in the labelled input; it does not infer legal validity, empirical performance, independent coding agreement or copyright liability. AI-assisted generation is disclosed. Input figures/specifications and manuscript text have a separate CC BY-NC-ND licence; this code licence does not relicense them.
