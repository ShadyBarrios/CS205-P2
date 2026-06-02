# represents an instance in the dataset

class Instance:
    def __init__(self, instanceID, instanceClass, instanceFeatures):
        self.instanceID = instanceID
        self.instanceClass = instanceClass
        self.instanceFeatures = instanceFeatures
    
    def get_id(self):
        return self.instanceID
    
    def get_class(self):
        return self.instanceClass

    def get_features(self):
        return self.instanceFeatures
    
    def select_features(self, feature_idxs):
        features = [self.instanceFeatures[i] for i in feature_idxs]
        return Instance(self.instanceID, self.instanceClass, features)