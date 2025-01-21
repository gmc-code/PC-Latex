from pathlib import Path
import random

# Define the LaTeX diagram template with placeholders
TEMPLATE = r"""
\begin{minipage}[]{0.8\linewidth}
\begin{tikzpicture}
\coordinate (A) at (0,0);
\coordinate (B) at (<<xA>>,<<yA>>);
\coordinate (C) at (<<xC>>,<<yC>>);
\draw (A) -- (B) -- cycle;
\draw (A) -- (C) -- cycle;
\draw[-] (<<xarcAB>>,<<yarcAB>>) arc [start angle=<<AngleAB>>, end angle=<<AngleEnd>>, radius=1cm];
\node[right] at (<<ABClabelX>>,<<ABClabelY>>) {\raggedright $\theta = <<Angle>>^\circ$};
\node[] at (<<BlabelX>>,<<BlabelY>>) {B};
\node[] at (<<AlabelX>>,<<AlabelY>>) {A};
\node[] at (<<ClabelX>>,<<ClabelY>>) {C};
\end{tikzpicture}
\end{minipage}
"""

def calculate_diagram_values():
    """Calculate values for a right triangle diagram."""
    angle = random.randint(20, 85)
    angleAB = random.randint(0, 85)
    arm_length = 6

    xA = arm_length * math.cos(math.radians(angleAB))
    yA = arm_length * math.sin(math.radians(angleAB))
    xC = arm_length * math.cos(math.radians(angle + angleAB))
    yC = arm_length * math.sin(math.radians(angle + angleAB))

    return {
        "Angle": angle,
        "AngleAB": angleAB,
        "AngleEnd": angle + angleAB,
        "xA": xA,
        "yA": yA,
        "xC": xC,
        "yC": yC,
        "xarcAB": math.cos(math.radians(angleAB)),
        "yarcAB": math.sin(math.radians(angleAB)),
        "ABClabelX": 0.5 * math.cos(math.radians(angleAB)),
        "ABClabelY": 0.5 * math.sin(math.radians(angleAB)) - 0.3,
        "AlabelX": xA + 0.2 * math.cos(math.radians(angleAB)),
        "AlabelY": yA + 0.2 * math.sin(math.radians(angleAB)),
        "ClabelX": xC + 0.2 * math.cos(math.radians(angle + angleAB)),
        "ClabelY": yC + 0.2 * math.sin(math.radians(angle + angleAB)),
        "BlabelX": -0.2 * math.cos(math.radians(angle / 2 + angleAB)),
        "BlabelY": -0.2 * math.sin(math.radians(angle / 2 + angleAB)),
    }

def generate_latex_diagram(diagram_values):
    """Generate the LaTeX code for a single diagram."""
    latex_code = TEMPLATE
    for key, value in diagram_values.items():
        latex_code = latex_code.replace(f"<<{key}>>", f"{value:.2f}")
    return latex_code

def main():
    """Generate a complete LaTeX document with diagrams."""
    num_diagrams = int(input("Enter the number of diagrams to generate: "))
    diagrams = []

    for _ in range(num_diagrams):
        values = calculate_diagram_values()
        diagrams.append(generate_latex_diagram(values))

    # Create the LaTeX document
    document = "\n".join(diagrams)
    output_path = Path("output_diagrams.tex")
    with open(output_path, "w") as file:
        file.write(document)

    print(f"LaTeX document written to {output_path}")

if __name__ == "__main__":
    main()
