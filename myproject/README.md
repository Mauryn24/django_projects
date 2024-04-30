# Green Data Storage Solutions

## Overview

The Green Data Storage Solutions project aims to address the environmental impact of traditional cloud computing by proposing sustainable approaches to data storage in cloud environments. Leveraging energy-efficient algorithms and renewable energy integration, the project seeks to reduce carbon emissions and promote environmental sustainability in IT infrastructure.

## Installation

- To set up the Green Data Storage Solutions project on your local machine, follow these steps:


1. Create a Virtual Environment: It's recommended to use a virtual environment to manage project dependencies. You can create one using virtualenv or venv:
   ```virtualenv myenv```
    or
    ```python -m venv myenv```
2. Activate the Virtual Environment: Navigate to the project directory and activate the virtual environment:
   ```source myenv/bin/activate   # for Linux/Mac```
    or
    ```myenv\Scripts\activate   # for Window```
3. First, ensure you have Django installed. If not, you can install it using pip:

```pip install django```

4. Create a new Django project and app:

```
django-admin startproject myproject
cd myproject
python manage.py startapp myapp
```

5. Replace the code in `myapp/views.py` with the following code:

```python
from django.shortcuts import render
from .models import ExperimentalDesign

def index(request):
    exp_design = ExperimentalDesign()
    exp_design.simulate_workload_and_energy()
    exp_design.calculate_carbon_footprint()

    # Names corresponding to each carbon footprint value
    names = ['Footprint 1', 'Footprint 2', 'Footprint 3', 'Footprint 4', 'Footprint 5', 
             'Footprint 6', 'Footprint 7', 'Footprint 8', 'Footprint 9', 'Footprint 10']

    # Combine names with carbon footprint values
    carbon_footprint_data = zip(names, exp_design.carbon_footprint)

    return render(request, 'myapp/index.html', {'carbon_footprint_data': carbon_footprint_data})

```

6. Create a new file `myapp/models.py` and add the following code:

```python
from django.db import models
import numpy as np
import matplotlib.pyplot as plt

# Create your models here.

class ExperimentalDesign:
    def __init__(self):
        self.workload = None
        self.energy_consumption = None
        self.deployment_results = None
        self.carbon_footprint = None
    
    def simulate_workload_and_energy(self):
        # Simulate workload and energy consumption
        self.workload = np.random.randint(50, 200, size=10)  # Example workload data
        self.energy_consumption = np.random.uniform(100, 500, size=10)  # Example energy consumption data
    
    def calculate_carbon_footprint(self):
        # Calculate carbon footprint based on energy consumption (example calculation)
        self.carbon_footprint = self.energy_consumption * 0.5  # Example: 0.5 kgCO2/kWh emission factor
    
    def evaluate_energy_efficiency(self):
        # Evaluate energy efficiency based on simulated workload and energy consumption
        efficiency_results = np.divide(self.workload, self.energy_consumption)
        return efficiency_results
    
    def plot_simulation_results(self):
        # Plot workload and energy consumption
        plt.figure(figsize=(10, 5))
        plt.plot(range(1, 11), self.workload, marker='o', label='Workload')
        plt.plot(range(1, 11), self.energy_consumption, marker='x', label='Energy Consumption')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Simulation Results')
        plt.legend()
        plt.grid(True)
        plt.savefig('myapp/static/simulation_results.png')  # Save plot as static file for web application
        plt.close()
    
    def deploy_renewable_energy_solution(self):
        # Deploy renewable energy integration solution
        # Placeholder for real-world pilot deployment code
        self.deployment_results = np.random.rand(10)  # Example deployment results
    
    def plot_deployment_results(self):
        # Plot deployment results
        plt.figure(figsize=(10, 5))
        plt.plot(range(1, 11), self.deployment_results, marker='o', color='green')
        plt.xlabel('Time')
        plt.ylabel('Deployment Results')
        plt.title('Real-World Pilot Deployment Results')
        plt.grid(True)
        plt.savefig('myapp/static/deployment_results.png')  # Save plot as static file for web application
        plt.close()

```

7. Create a new directory named `templates` in the `myapp` directory, and within that directory, create a new HTML file named `index.html` with the following content:

```html
{% load static %} <!-- Load static files such as images -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Experimental Results</title>
</head>
<body>
    <!-- Heading for carbon footprint data -->
    <h1>Carbon Footprint:</h1> 
    <ul>
        <!-- Iterate through carbon footprint data -->
        {% for name, value in carbon_footprint_data %}
        <!-- Display name and corresponding value -->
        <li>{{ name }}: {{ value }}</li> 
        {% endfor %}
    </ul>
    
    <!-- Display images for simulation and deployment results -->
    <!-- Static image for simulation results -->
    <img src="{% static 'simulation_results.png' %}" alt="Simulation Results">
    <!-- Static image for deployment results -->
    <img src="{% static 'deployment_results.png' %}" alt="Deployment Results">
</body>
</html>
```

8. Add `'myapp'` to the `INSTALLED_APPS` list in the `myproject/settings.py` file:

```python
INSTALLED_APPS = [
    ...
    'myapp',
]
```

9. Configure the static files settings in `myproject/settings.py`:

```python
STATIC_URL = '/static/'
```

10. Finally, configure the URL routing by adding the following URL pattern in the `myproject/urls.py` file:

```python
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

11. Now, you can run the Django development server using the command:

```
python manage.py runserver
```

And visit http://127.0.0.1:8000/ in your web browser to see the results displayed in the web application.

This setup creates a simple Django web application that displays the carbon footprint along with the simulation and deployment results as plots. 

### Note
Each reload gives different footprints


## Other dependencies
- Make sure numpy is installed
- Install using the command ```pip install numpy```
- Ensure matplotlib is installed
- Install using coomand ```pip install matplotlib```