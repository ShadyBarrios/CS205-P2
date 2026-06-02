from enums import AlgoChoiceEnum
from evaluator import one_fold_cross_validation

def run_algo(choice, dataset):
    feature_idxs = [idx for idx in range(len(dataset[0].get_features()))]
    if choice == AlgoChoiceEnum.FORWARD:
        forward_selection(dataset, feature_idxs)
    else:
        backward_selection(dataset, feature_idxs)

def forward_selection(dataset, feature_idxs):
    pass

def backward_selection(dataset, feature_idxs):
    pass

# using all features
def naive_algo(dataset):
    return one_fold_cross_validation(dataset)

# select features from dataset and returns
# dataset with features only containing selected features
def select_features(dataset, features):
    filtered_dataset = []
    for instance in dataset:
        filtered_instance = instance.select_features(features)
        filtered_dataset.append(filtered_instance)
    return filtered_dataset