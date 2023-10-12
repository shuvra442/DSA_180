# Define the lists for each person
saniyaj = [0]
sombhu = [0]
pritam = [0]
sajed = [0]
shuvra = [0]
rajat = [0]

# Create a dictionary to store the names and their corresponding lists
people = {
    "Saniyaj": saniyaj,
    "Sombhu": sombhu,
    "Pritam": pritam,
    "Sajed": sajed,
    "Shuvra": shuvra,
    "Rajat": rajat
}

# Calculate the sum of elements in each list and store in a dictionary
sums = {name: sum(lst) for name, lst in people.items()}

# Rank the people based on the sums in descending order
ranked_people = sorted(sums, key=sums.get, reverse=True)

# Create a dictionary to store the rankings
rankings = {name: rank + 1 for rank, name in enumerate(ranked_people)}

# Print the rankings
for name, rank in rankings.items():
    print(f"{name}: Rank {rank}")
