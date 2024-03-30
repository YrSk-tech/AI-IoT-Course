import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report


def process_dataset(file_path: str) -> tuple:
    data = pd.read_csv(file_path)
    inputs = data[['Budget', 'Time', 'Attraction_1', 'Attraction_2', 'Attraction_3']]
    outputs = data['Route']
    features_labeled = pd.DataFrame()

    label_encoder = {
        'Budget': LabelEncoder(),
        'Time': LabelEncoder(),
        'Attraction_1': LabelEncoder(),
        'Attraction_2': LabelEncoder(),
        'Attraction_3': LabelEncoder()
    }

    for feature_column in inputs.columns:
        fit_encoder = label_encoder[feature_column]
        features_labeled[feature_column] = fit_encoder.fit_transform(inputs[feature_column])

    return features_labeled, outputs, label_encoder


def train_model(features, target):
    training_model = DecisionTreeClassifier()
    training_model.fit(features, target)
    return training_model


def calculate_metrics(input_model, feat_test, tar_test):
    target_predicted = input_model.predict(feat_test)

    accuracy = accuracy_score(tar_test, target_predicted)
    print(f'Accuracy: {accuracy}')

    print('Metrics report:')
    print(classification_report(tar_test, target_predicted))


if __name__ == '__main__':
    features_train, target_train, train_encoders = process_dataset('attractions_routs_train.csv')
    features_test, target_test, _ = process_dataset('attractions_routs_test.csv')

    model = train_model(features_train, target_train)
    calculate_metrics(model, features_test, target_test)

    budget = '220'
    time = '4'
    attraction_1 = 'Beach'
    attraction_2 = 'Hiking_Trail'
    attraction_3 = 'Shopping_Center'

    input_data = pd.DataFrame({'Budget': [budget], 'Time': [time],
                               'Attraction_1': [attraction_1], 'Attraction_2': [attraction_2],
                               'Attraction_3': [attraction_3]})
    input_data_encoded = pd.DataFrame()

    for column in input_data.columns:
        encoder = train_encoders[column]
        input_data_encoded[column] = encoder.transform(input_data[column])

    resulting_prediction = model.predict(input_data_encoded)
    print(f'Predicted route: {resulting_prediction}')
