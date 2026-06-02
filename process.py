# this file will contain functions to process n clean dataset
from instance import Instance
import statistics as stats

def parse_data(filename):
    instanceID = 0
    instances = []
    try:
        with open(filename, 'r') as file:
            while True:
                line = file.readline()
                if line == '': # EOF returns blank
                    break

                parts = line.split()
                instanceClass = int(parts[0].split(".")[0])
                print(instanceClass)
                instanceFeatures = [float(feature) for feature in parts[1::]]
                instance = Instance(instanceID, instanceClass, instanceFeatures)
                instances.append(instance)
                instanceID += 1
    except FileNotFoundError:
        print(f"{filename} not found. Try again.")
        return None
    
    return instances

# z-score normalization
def normalize(dataset):
    # zip(*list) is used to change into col major order
    # https://www.geeksforgeeks.org/python/zip-in-python/ - for zip
    # https://www.tutorialspoint.com/article/how-does-operator-work-on-list-in-python - for *
        # * returns the rows individually (unpacked)
        # zip then combines them, organized by column position
    # a = [[1,2,3], [4,5,6]]
    # *a ==> [1,2,3] [4,5,6]
    # zip(*a) ==> [[1,4],[2,5],[3,6]]
    features = [instance.get_features() for instance in dataset]
    feature_cols = [list(col) for col in zip(*features)]
    feature_col_stats = [(stats.mean(col), stats.stdev(col)) for col in feature_cols]

    normalized_instances = []
    for instance in dataset:
        normalized_instance = normalize_instance(instance, feature_col_stats)
        normalized_instances.append(normalized_instance)

    return normalized_instances

def normalize_instance(instance, col_stats):
    normalized_features = []
    for col in range(len(col_stats)):
        feature = instance.get_features()[col]
        mean, std = col_stats[col]
        normalized_feature = z_score(feature, mean, std)
        normalized_features.append(normalized_feature)
    return Instance(instance.get_id(), instance.get_class(), normalized_features)

def z_score(value, mean, std):
    return ((value - mean) / std)

