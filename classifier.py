import math

def nearest_neighbor(instance, dataset):
    nn = None
    distance_bsf = float('inf')
    for neighbor in dataset:
        distance = distance_to(instance, neighbor)
        if distance < distance_bsf:
            nn = neighbor
            distance_bsf = distance
    
    if nn is None:
        return None
    
    return nn.get_class()


def distance_to(src, dest):
    src_features = src.get_features()
    dest_features = dest.get_features()
    dist = 0

    # sum of squares and then sqrt
    for idx in range(len(src_features)):
        dist += (src_features[idx] - dest_features[idx]) ** 2
    
    return math.sqrt(dist)
