import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder


def process_dataset(file_path: str) -> tuple:
    data = pd.read_csv(file_path)
    features = data[['Budget', 'Time', 'Attraction_1', 'Attraction_2', 'Attraction_3']]
    labels = data['Route']
    encoded_features = pd.DataFrame()

    label_encoders = {}

    for feature_column in features.columns:
        label_encoders[feature_column] = LabelEncoder()
        encoded_features[feature_column] = label_encoders[feature_column].fit_transform(features[feature_column])

    label_encoder_route = LabelEncoder()
    encoded_labels = label_encoder_route.fit_transform(labels)

    return encoded_features, encoded_labels, label_encoders, label_encoder_route


def create_nn_model(input_shape, output_shape):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=input_shape),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(output_shape, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model


if __name__ == '__main__':
    train_file_path = "attractions_routs_train.csv"
    test_file_path = "attractions_routs_test.csv"

    features_train, labels_train, train_encoders, label_encoder_route_train = process_dataset(train_file_path)
    features_test, labels_test, _, _ = process_dataset(test_file_path)

    input_shape = (features_train.shape[1],)
    output_shape = len(label_encoder_route_train.classes_)

    model = create_nn_model(input_shape=input_shape, output_shape=output_shape)

    model.fit(features_train, labels_train, epochs=50, validation_split=0.2)

    loss, accuracy = model.evaluate(features_test, labels_test)

    print('Test Loss route:', loss)
    print('Test Accuracy route:', accuracy)
