import random


num_points = 9999
catagories = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
num_features = 4

# total_points, total_values, K, max_iterations, has_name;
with open ("generated_data.txt", 'w') as f:
    header = str(num_points) + " " + str(num_features) + " " + "100 " + "1" + "\n"
    f.write(header)
    for i in range(len(catagories)):
        local_n = int(num_points / len(catagories))


        for _ in range(local_n):
            f.write(str(round(random.uniform(4,6), 1)))
            f.write(" ")
            f.write(str(round(random.uniform(2,4), 1)))
            f.write(" ")
            f.write(str(round(random.uniform(4,6), 1)))
            f.write(" ")
            f.write(str(round(random.uniform(0,2), 1)))
            f.write(" ")
            f.write(catagories[i])
            f.write("\n")


