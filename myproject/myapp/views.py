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
