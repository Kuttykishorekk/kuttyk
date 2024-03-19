# Kutty - Advanced Data Visualization Library

## Introduction
Kutty is a Python data visualization library built to extend the capabilities of existing libraries such as Matplotlib, Plotly, and Seaborn. It provides a versatile set of plotting functions, including advanced plots, interactive plots, time series, heatmaps, and 3D visualizations, making it a useful tool for data scientists and analysts who require more sophisticated visualization capabilities.

## Installation
Kutty can be installed using pip. Ensure you have Python >= 3.9 installed on your system. Then run:

```
pip install kutty
```

Alternatively, if you are using Poetry and have already cloned the Kutty repository, you can install the package locally by running:

```
poetry install
```

## Usage
Here are some usage examples for each of the key features provided by Kutty:

### Basic Line Plot
```python
from kutty.plotter import simple_line_plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
simple_line_plot(x, y)
```

### Advanced Plot
```python
from kutty.plotter import advanced_plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 2, 3, 2]
advanced_plot(x, y)
```

### Interactive Plot
```python
from kutty.interactive import interactive_plot
x = [1, 2, 3, 4, 5]
y = [5, 3, 4, 2, 1]
interactive_plot(x, y)
```

### Time Series Plot
```python
from kutty.time_series import time_series_plot
import pandas as pd
dates = pd.date_range('2021-01-01', periods=5, freq='M')
values = [100, 120, 130, 145, 160]
time_series_plot(dates, values)
```

### Heatmap
```python
from kutty.heatmap import heatmap_plot
import numpy as np
data = np.random.rand(10, 12)
heatmap_plot(data)
```

### 3D Plot
```python
from kutty.plot_3d import plot_3d
x, y, z = [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]
plot_3d(x, y, z, plot_type='scatter')
```

### Geographical plot(GEOMAP)
```python
# Sample latitude and longitude coordinates
latitudes = [34.0522, 40.7128, 37.7749]
longitudes = [-118.2437, -74.0060, -122.4194]
titles = ['Los Angeles', 'New York', 'San Francisco']

# Visualize the locations on a map
plot_geo_locations(latitudes, longitudes, titles)
```

## Contributing
We welcome contributions to Kutty! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcomed.

## License
The code in this project is licensed under MIT license. See the `LICENSE` file for more information.

## Support
If you encounter any issues or have questions about using Kutty, please file an issue in the project's GitHub repository.
