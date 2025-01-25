# Name: Faye(Lifei) Wang
# Date: 01/24/2025

import pandas as pd
from matplotlib import pyplot as plt


# Step 1: Read the data
data = pd.read_csv("/Users/faye/Desktop/leaf_data.csv") 
print(data.head())  # Print the first 5 rows of the dataset


# Step 2: Plot histogram for all plants
plt.hist(data['leaf_length'], bins=10, alpha=0.7)  # Draw histogram with 10 bins
plt.title('Leaf Length', fontsize=14)  # Add title
plt.xlabel('All', fontsize=12)  # Label x-axis
plt.ylabel('Count', fontsize=12)  # Label y-axis
plt.show()  # Display the plot

# Step 3: Group data by species
groups = data.groupby("species")  # Group the data based on species name

for name, group in groups:  # Loop through each group
    print(name)  # Print the species name
    x = group.leaf_length  # Use 'leaf_length' as the data to plot
    y = group.leaf_width  # Use 'leaf_width' as the data to plot
    
    plt.hist(x, bins=10, alpha=0.7)  # Plot histogram for the species
    plt.xlabel(f'({name})', fontsize=12)  # Label x-axis for each species
    plt.ylabel('Count', fontsize=12)  # Label y-axis
    plt.legend([name])  # Add a legend for the species name
    plt.show()  # Show the histogram
    
# Step 4: Plot scatter plot for all species
colors = ['blue', 'orange', 'green']  # Define colors for each species

for (name, group), color in zip(groups, colors):  # Loop through each group with colors
    x = group.leaf_length  
    y = group.leaf_width  
    plt.scatter(x, y, color=color, label=name, alpha=0.7)  # Scatter plot with specified color

plt.xlabel("Leaf Length", fontsize=12) 
plt.ylabel("Leaf Width", fontsize=12)  
plt.legend() 
plt.title("Leaf Length vs Width", fontsize=14)  
plt.show()  

# Step 5: Plot boxplots for leaf lengths by species
all_data = [data['leaf_length']]  # all_data should be a list, so that we can append. Start with all plants' data
for _, group in groups:  # Loop through each species group
    all_data.append(group['leaf_length'])  # Add each species' data
labels = ['All','Aglaonema','Mentha','Basilicum' ] 

plt.boxplot(all_data, labels=labels) 
plt.title('Leaf Length', fontsize=14) 
plt.show()  
