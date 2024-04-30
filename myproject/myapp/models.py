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
