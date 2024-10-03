import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define entities and attributes
entities = {
    "Student": ["Student_ID (PK)", "Name", "Email", "Phone_Number", "Enrollment_Year", "Major"],
    "NGO": ["NGO_ID (PK)", "Name", "Contact_Person", "Email", "Phone_Number", "Address"],
    "Internship": ["Internship_ID (PK)", "Title", "Description", "Start_Date", "End_Date", "NGO_ID (FK)"],
    "Faculty": ["Faculty_ID (PK)", "Name", "Email", "Phone_Number", "Department"],
    "Application": ["Application_ID (PK)", "Student_ID (FK)", "Internship_ID (FK)", "Submission_Date", "Status"]
}

# Add entities to the graph with unique attributes
for entity, attributes in entities.items():
    label = entity + "\n" + "\n".join(attributes)
    G.add_node(entity, label=label)

# Define relationships
relationships = [
    ("Student", "Application"),
    ("Internship", "Application"),
    ("NGO", "Internship"),
    ("Faculty", "NGO")
]

# Add edges to represent relationships
for source, target in relationships:
    G.add_edge(source, target)

# Position nodes in a hierarchical layout
pos = nx.spring_layout(G, seed=42)

# Draw nodes with specified colors and styles
node_labels = nx.get_node_attributes(G, 'label')
nx.draw_networkx_nodes(G, pos, node_size=4000, node_color='lightblue')
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20, edge_color='gray')

# Draw node labels with a nicer font size
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, verticalalignment='center')

# Set title and style
plt.title("Entity-Relationship Diagram (ERD) for CSSI Portal", fontsize=14)
plt.axis('off')

# Save the figure
plt.savefig('ERD_CSSI_Portal_Improved.png', format='png', bbox_inches='tight', dpi=300)
plt.show()
