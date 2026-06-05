from enums import AlgoChoiceEnum
from evaluator import one_fold_cross_validation

def run_algo(choice, dataset):
    feature_idxs = [idx for idx in range(len(dataset[0].get_features()))]
    if choice == AlgoChoiceEnum.FORWARD:
        forward_selection(dataset, feature_idxs)
    else:
        backward_selection(dataset, feature_idxs)

def forward_selection(dataset, feature_idxs):
    # track features selected, best feature set and best accuracy overall
    currFeatures = []  
    bestSet = []
    ovrAccuracy = 0 
    depths = len(feature_idxs)
    maxDecrease = 2
    decreaseCount = 0

    print("\nBeginning search.\n")
    while depths > 0:
        bestFeature = None     # best feature and accuracy at depth
        bestAccuracy = -1
        
        # adding features not in set
        for feature in feature_idxs:
            if feature not in currFeatures:
                feat = currFeatures + [feature]
                filterDataset = select_features(dataset, feat)
                accuracy = one_fold_cross_validation(filterDataset)
                print(f"\tUsing feature(s) {[f + 1 for f in feat]} accuracy is {accuracy * 100:.2f}%")
            
                # finds best feature to add
                if accuracy > bestAccuracy:
                    bestAccuracy = accuracy
                    bestFeature = feature
        currFeatures.append(bestFeature)
        print(f"\nFeature set {[f + 1 for f in currFeatures]} was best, accuracy is {bestAccuracy * 100:.2f}%\n")

        # update best if accuracy increased
        if bestAccuracy > ovrAccuracy:
            ovrAccuracy = bestAccuracy
            bestSet = currFeatures.copy()
            decreaseCount = 0
        else:
            # decreased accuracy, continue search (local maxima case)
            decreaseCount += 1
            print("(Warning, Accuracy has decreased! Continuing search in case of local maxima)")
            if decreaseCount >= maxDecrease:
                break

        depths -= 1
    print(f"\nFinished search!! The best feature subset is {[f + 1 for f in bestSet]}, which has an accuracy of {ovrAccuracy * 100:.2f}%")

def backward_selection(dataset, feature_idxs):
    # start with all features and evaluate its accuracy
    currFeatures = feature_idxs.copy()
    filterDataset = select_features(dataset, currFeatures)
    ovrAccuracy = one_fold_cross_validation(filterDataset)
    bestSet = currFeatures.copy()
    depths = len(feature_idxs)
    maxDecrease = 2
    decreaseCount = 0

    print("\nBeginning search.\n")
    while depths > 1:
        # best feature to remove and accuracy at depth
        removeFeat = None
        bestAccuracy = -1

        # removing features in set
        for feature in currFeatures:
            feat = currFeatures.copy()      
            feat.remove(feature)
            filterDataset = select_features(dataset, feat)
            accuracy = one_fold_cross_validation(filterDataset)
            print(f"\tUsing feature(s) {[f + 1 for f in feat]} accuracy is {accuracy * 100:.2f}%")

            # remove feature if accuracy is better
            if accuracy > bestAccuracy:
                bestAccuracy = accuracy
                removeFeat = feature
        currFeatures.remove(removeFeat)
        print(f"\nFeature set {[f + 1 for f in currFeatures]} was best, accuracy is {bestAccuracy * 100:.2f}%\n")

        # update best accuracy and set
        if bestAccuracy > ovrAccuracy:
            ovrAccuracy = bestAccuracy
            bestSet = currFeatures.copy()
            decreaseCount = 0
        else:
            decreaseCount += 1
            print("(Warning, Accuracy has decreased! Continuing search in case of local maxima)")
            if decreaseCount >= maxDecrease:
                break

        depths -= 1
    print(f"\nFinished search!! The best feature subset is {[f + 1 for f in bestSet]}, which has an accuracy of {ovrAccuracy * 100:.2f}%")

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