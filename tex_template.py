def fourbyfour(questions_1, questions_2, bold=False):
    if bold:
        questions_1 = ["\\textbf{" + str(q) + "}" for q in questions_1]
        questions_2 = ["\\textbf{" + str(q) + "}" for q in questions_2]
    return (
        r"""\documentclass[20pt]{article}
\usepackage{array}
\usepackage[legalpaper, portrait, margin=0in]{geometry}
\usepackage{helvet}

\begin{document}

\renewcommand{\arraystretch}{3}
\begin{table}
    \Large
    \centering
    \begin{tabular}{||m{0.2\textwidth}<{\centering}|m{0.2\textwidth}<{\centering}|m{0.2\textwidth}<{\centering}|m{0.2\textwidth}<{\centering}||}
        \hline
        \hline
"""
        + "\n".join(
            [
                "         "
                + " & ".join([str(questions_1.pop()) for _ in range(4)])
                + " \\\\ \\hline"
                for _ in range(4)
            ]
        )
        + r"""
        \hline
    \end{tabular}
\end{table}

\begin{table}
    \Large
    \centering
    \begin{tabular}{||m{0.2\textwidth}<{\centering}|m{0.2\textwidth}<{\centering}|m{0.2\textwidth}<{\centering}|m{0.2\textwidth}<{\centering}||}
        \hline
        \hline
"""
        + "\n".join(
            [
                "         "
                + " & ".join([str(questions_2.pop()) for _ in range(4)])
                + " \\\\ \\hline"
                for _ in range(4)
            ]
        )
        + r"""
        \hline
    \end{tabular}
\end{table}
\end{document}"""
    )
