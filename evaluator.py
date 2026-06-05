# k-fold cross validation where k = 1
from classifier import nearest_neighbor

def one_fold_cross_validation(dataset):
    num_success = 0
    num_runs = 0

    for test_idx in range(len(dataset)):
        test_dataset = dataset[:test_idx] + dataset[test_idx+1:]
        expected = dataset[test_idx].get_class()
        prediction = nearest_neighbor(dataset[test_idx], test_dataset)
        if prediction == expected:
            num_success += 1
        num_runs += 1
    
    return (num_success / num_runs)