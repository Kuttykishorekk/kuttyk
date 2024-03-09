from kuttyk import __version__


def test_version():
    assert __version__ == '0.1.0'


import pytest
from kuttyk.interactive import interactive_plot
import plotly.graph_objects as Go

# Define the test function
def test_interactive_plot():
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 2, 3, 2]
    result = interactive_plot(x, y)
    assert isinstance(result, Go.Figure), "interactive_plot should return a Plotly Figure object."
