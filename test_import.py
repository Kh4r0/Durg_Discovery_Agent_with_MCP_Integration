from agent.scientific_tools import (
    openfda_adverse_effects,
    search_papers,
    get_compound_info
)

print(openfda_adverse_effects("Paracetamol"))
print(search_papers("Paracetamol toxicity"))